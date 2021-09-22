import time
import argparse
import mysql.connector
from dask import dataframe as dd

username = input('Input MySQL username: ')
password = input('Input MySQL password: ')

start_time = time.time()

parser = argparse.ArgumentParser(
    description="""This is a python script that allows you to get movies from csv using SQL by your own filters with 
    CSV like output.""",
    epilog="""Example: python3 get-movies.py -N 10 --regexp war --genres "Documentary|Children" --year_from 2000 
    --year_to 2005""")

parser.add_argument('-N', nargs='?', help='the number of top rated films for each genre. optional')
parser.add_argument('--genres', nargs='?',
                    help='user-defined genre filter. may be plural. For example, Comedy | Adventure or Comedy & '
                         'Adventure. optional')
parser.add_argument('--year_from', nargs='?', help='from the year. optional')
parser.add_argument('--year_to', nargs='?', help='till the year. optional')
parser.add_argument('--regexp', nargs='?', help='filter (regular expression) for the title of the movie. optional')
args = parser.parse_args()

CONFIG = {
    'host': 'localhost',
    'user': username,
    'passwd': password
}

mydb = mysql.connector.connect(**CONFIG)
cursor = mydb.cursor()

cursor.execute("""
    DROP DATABASE IF EXISTS movies_db
""")
cursor.execute("""
    CREATE DATABASE movies_db
""")

CONFIG['database'] = 'movies_db'

cursor.execute("""
    USE movies_db
""")

uri = f"mysql+mysqlconnector://{CONFIG['user']}:{CONFIG['passwd']}@{CONFIG['host']}/{CONFIG['database']}"

df = dd.read_csv('movies.csv')
df.to_sql('movies', uri=uri, if_exists='replace', index=False)  # try chunksize on big dataset
df = dd.read_csv('ratings.csv')
df.to_sql('ratings', uri=uri, if_exists='replace', index=False)

cursor.execute("""
    ALTER TABLE movies
    ADD year INT
""")
cursor.execute("""
    ALTER TABLE ratings
    RENAME COLUMN movieId TO r_movieId;
""")

cursor.execute("""
    UPDATE movies 
    SET `year` = REGEXP_SUBSTR(title, '[0-9]{4}'),
        title = REGEXP_REPLACE(title, '[()]|[0-9]{4}', '');
""")
mydb.commit()

cursor.execute("""
    SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
""")

N = args.N
if N:
    N = int(N)
else:
    N = '0,18446744073709551615'

genres = args.genres
if genres:
    genres = 'genres LIKE "%' + '%" or "%'.join(genres.split('|')) + '%"'
else:
    genres = 'movieId IS NOT NULL'

year_from = args.year_from
if year_from:
    year_from = int(year_from)
else:
    year_from = 0

year_to = args.year_to
if year_to:
    year_to = int(year_to)
else:
    year_to = 5000

regexp = args.regexp
if not regexp:
    regexp = '.'
# if not regexp and not
order_by = 'rating DESC, genres, title, year'
select = f"""
    SELECT genres, title, `year` year, ROUND(AVG(rating), 2) rating
    FROM movies, ratings
    WHERE movieId = r_movieId
        AND ({genres})
        AND (`year` BETWEEN {year_from} AND {year_to})
        AND (title REGEXP "{regexp}")
    GROUP BY r_movieId
    ORDER BY {order_by}
    LIMIT {N}
"""
cursor.execute(select)

rows = cursor.fetchall()
print('genre,title,year,rating')
for row in rows:
    for i in range(len(row)):
        if i == 1:
            print(row[i][:-1], end=',')
        elif i == 3:
            print(row[i], end='\n')
        else:
            print(row[i], end=',')
    # print(f'{row[0]},{row[1][:-1]},{row[2]},{row[3]},{row[4]}')

print(f"\n\tCompleted at: {time.time() - start_time} sec")
