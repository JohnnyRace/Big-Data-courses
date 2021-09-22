#!/usr/bin/python
# -*- codingTF-8 -*-

import sys
from operator import itemgetter
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='The script returns filtered data from the DataSet')
    parser.add_argument('-N', nargs='?', help='the number of top rated films for each genre. optional')
    return parser


def parse_value(line):
    movie = line.replace('[', '').replace(']', '').replace(', (', '').replace('(', '')
    if movie.find('"') >= 0:
        movie = movie.replace('"', '')
    else:
        movie = movie.replace("'", "")
    title, year = movie.rsplit(',')
    year = int(year[1:5])
    return title, year


def reduce():
    for line in sys.stdin:
        key, value = line.split('\t')
        movies = []
        for movie in value[0:-3].split(')'):
            title, year = parse_value(movie)
            movies.append((title, year))
        movies = sorted(movies, key=itemgetter(0))
        movies = sorted(movies, key=itemgetter(1), reverse=True)

        yield key, movies


def main():
    parser = create_parser()
    namespace = parser.parse_args()

    print('genre,title,year')

    for key, value in reduce():
        if namespace.N:
            num_movies = namespace.N[0]
            count = 0
            for title, year in value:
                if count >= num_movies:
                    break
                count += 1
                print(f'{key}\t{(title, year)}')
        else:
            for title, year in value:
                print(f'{key}\t{(title, year)}')


if __name__ == '__main__':
    main()
