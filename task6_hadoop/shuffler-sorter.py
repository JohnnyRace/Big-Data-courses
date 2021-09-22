import sys
from operator import itemgetter


def get_sorted(data):
    data = sorted(data, key=itemgetter(1))
    data = sorted(data, key=itemgetter(2), reverse=True)
    return sorted(data, key=itemgetter(0))


def shuffle(data, num_reducers=1):
    shuffled_items = []

    prev_key = None
    values = []

    for line in data:
        key, title, year = line
        value = (title, year)

        if key != prev_key and prev_key != None:
            shuffled_items.append((prev_key, values))
            values = []
        prev_key = key
        values.append(value)

    result = []
    num_items_per_reducer = len(shuffled_items) // num_reducers
    if len(shuffled_items) / num_reducers != num_items_per_reducer:
        num_items_per_reducer += 1
    for i in range(num_reducers):
        result.append(shuffled_items[num_items_per_reducer * i:num_items_per_reducer * (i + 1)])

    return result


def main():
    data = []
    for line in sys.stdin:
        genre, title = line.split('\t')
        if title.find('"') >= 0:
            title = title.replace('"', '')
        else:
            title = title.replace("'", '')
        title, year = title[1:-8], title[-6:-2]
        row = [genre, title, int(year)]
        data.append(row)

    data = get_sorted(data)
    for group in shuffle(data):
        for key, value in group:
            print(f'{key}\t{value}')


if __name__ == '__main__':
    main()
