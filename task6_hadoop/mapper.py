#!/usr/bin/python
# -*- codingTF-8 -*-

import argparse
import sys
import re


def create_parser():
    parser = argparse.ArgumentParser(
        description="""This is a python script that allows you to get movies from csv.""",
        epilog="""Example: python3 get-movies.py -N 10 --regexp war --genres "Documentary|Children" --year_from 2000 
        --year_to 2005""")
    parser.add_argument('--genres', nargs='?',
                        help='user-defined genre filter. may be plural. For example, Comedy | Adventure or Comedy & '
                             'Adventure. optional')
    parser.add_argument('--year_from', nargs='?', help='from the year. optional')
    parser.add_argument('--year_to', nargs='?', help='till the year. optional')
    parser.add_argument('--regexp', nargs='?', help='filter (regular expression) for the title of the movie. optional')
    return parser


def get_split_line(line):
    first_comma = int(line.find(','))
    last_comma = int(line.rfind(','))
    all_title = line[first_comma + 1:last_comma].replace('"', '').replace('(', '').replace(')', '')
    try:
        year = int(re.findall(r'\d{4}', all_title)[-1])
        title = all_title[:-5]
        genres = line[last_comma + 1:-2]
        return genres, title, year
    except:
        pass


def regexp_filter(title, regexp):
    return True if title.lower().find(regexp[0].lower()) >= 0 else False


def year_filter(year, year_from=None, year_to=None):
    if year_from and year_to:
        return True if year_from[0] <= year <= year_to[0] else False
    elif year_from:
        return True if year_from[0] <= year else False
    elif year_to:
        return True if year <= year_to[0] else False


def get_genres(genres, parse_genres):
    selected_genres = []
    if parse_genres:
        parse_genres = set(parse_genres[0].split('|'))
        for genre in genres.split('|'):
            if genre in parse_genres:
                selected_genres.append(genre)
    else:
        for genre in genres.split('|'):
            selected_genres.append(genre)

    return selected_genres


def mapper(line):
    line = get_split_line(line)
    if line is None:
        return
    genres, title, year = line
    suitable = True
    if namespace.regexp:
        suitable = regexp_filter(title=title, regexp=namespace.regexp)
    if suitable and (namespace.year_from or namespace.year_to):
        suitable = year_filter(year=year, year_from=namespace.year_from, year_to=namespace.year_to)
    if suitable:
        for genre in get_genres(genres=genres, parse_genres=namespace.genres):
            yield genre, (title, year)


def main():
    for line_number, line in enumerate(sys.stdin):
        for key, value in mapper(line):
            print("{}\t{}".format(key, value))


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    main()
