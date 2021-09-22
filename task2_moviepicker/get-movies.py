import re
import csv
import argparse
import operator


parser = argparse.ArgumentParser(
    description="""This is a python script that allows you to get movies from csv by your own filters with CSV like output.""",
    epilog="""Example: python3 get-movies.py -N 10 --regexp war --genres "Documentary|Children" --year_from 2000 --year_to 2005""")

parser.add_argument('-N', nargs='?', help='the number of top rated films for each genre. optional')
parser.add_argument('--genres', nargs='?', help='user-defined genre filter. may be plural. For example, Comedy | Adventure or Comedy & Adventure. optional')
parser.add_argument('--year_from', nargs='?', help='from the year. optional')
parser.add_argument('--year_to', nargs='?', help='till the year. optional')
parser.add_argument('--regexp', nargs='?', help='filter (regular expression) for the title of the movie. optional')

args = parser.parse_args()

genres = args.genres
if genres:
    genres = genres.split('|')

year_from = args.year_from
if year_from:
    year_from = int(year_from)

year_to = args.year_to
if year_to:
    year_to = int(year_to)

N = args.N
if N:
    N = int(N)

def year_condition(row):
    year_template = re.findall(' \(\d\d\d\d\)', row[1])
    if year_template:
        year = int(year_template[0][2:6])
        if year_from and year_to:
            if year_from <= year <= year_to:
                return True
            else:
                return False
        elif year_from:
            if year_from <= year:
                return True
            else:
                return False
        elif year_to:
            if year <= year_to:
                return True
            else:
                return False
        else:
            return True
    else:
        return True


def add_to_dict(row):
    title = row[1].replace('"', '').strip()
    year_template = re.findall(' \(\d\d\d\d\)', title)
    if year_template:
        year = int(year_template[0][2:6])
        title = title.replace(year_template[0], '')
    else:
        return None
    if ", The" in title:
        title = title.replace(", The", '')
        title = 'The ' + title
    if ", Le)" in title:
        title = title.replace(", Le) ", '')
        title = title.replace("(", "(Le ") + ")"
    movies_dict[row[0]] = {'title': title, 'year': year, 'genre': row[2], 'rating': []}

with open('movies.csv', encoding='utf-8') as movies_file:
        file_reader = csv.reader(movies_file, delimiter=',')
        next(file_reader)
        file_reader = sorted(file_reader, key=operator.itemgetter(2))
        movies_dict = {}
        if args.regexp:
            for row in file_reader:
                template = re.findall(args.regexp, ', '.join(row))
                if genres:
                    for genre in genres:
                        if template and (genre in row[2]) and year_condition(row):
                            add_to_dict(row)
                else:
                    if template and year_condition(row):
                        add_to_dict(row)
        else:
            for row in file_reader:
                if genres:
                    for genre in genres:
                        if genre in row[2] and year_condition(row):
                            add_to_dict(row)
                else:
                    add_to_dict(row)

with open('ratings.csv', encoding='utf-8') as ratings_file:
    file_reader = csv.reader(ratings_file, delimiter=',')
    for row in file_reader:
        if row[1] in movies_dict:
            if row[2]:
                movies_dict[row[1]]['rating'] += [float(row[2])]
            else:
                movies_dict[row[1]]['rating'] += float(0)


for movie_id in movies_dict:
    rating = 0
    for num in movies_dict[movie_id]['rating']:
        rating += num
    if len(movies_dict[movie_id]['rating']) > 0:
        rating /= len(movies_dict[movie_id]['rating'])
        movies_dict[movie_id]['rating'] = round(rating, 2)
    else:
        movies_dict[movie_id]['rating'] = None

conditions = [args.regexp is not None and args.N is not None and args.genres is not None and args.year_to is not None and year_from is not None]
if conditions:
    movie_rating_dict = {}
    for movie in movies_dict.items():
        movie_rating_dict[movie[0]] = movie[1]['rating']
        movie_rating_dict = dict(sorted(movie_rating_dict.items(), key=lambda item: item[1], reverse=True))


def csv_like_output():
    print('genre,title,year,rating')
    if N is None or N > len(movies_dict):
        for movie_id in movies_dict:
            movie = movies_dict[movie_id]
            print(f"{movie['genre']},{movie['title']},{movie['year']},{movie['rating']}")
    elif conditions or N is not None:
        for i in range(N):
            movie = movies_dict[list(movie_rating_dict.keys())[i]]
            print(f"{movie['genre']},{movie['title']},{movie['year']},{movie['rating']}")


csv_like_output()
