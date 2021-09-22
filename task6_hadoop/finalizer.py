import sys


def main():
    print('genre,title,year')

    for line in sys.stdin:
        line = line.replace('\n', '')
        genre = line.split('\t')[0]
        first = line.find('(')
        last = line.rfind(')')
        movie = line[first + 1:last + 1]
        title = movie.rsplit(',')[0]
        year = movie[-5:-1]

        print(f'{genre},{title},{year}')


if __name__ == '__main__':
    main()
