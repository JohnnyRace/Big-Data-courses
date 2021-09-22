import pandas as pd
import pyarrow.parquet as pq
import sys
import argparse

parser = argparse.ArgumentParser(
    description="""This is a python script that allows you to convert csv to parquet and vice versa.
    You can insert the file name if it is in the project folder, or enter the full path to the file.""",
    epilog="""Example: python3 converter.py --csv2parquet csv_name.csv parquet_name.parquet""")

parser.add_argument('--csv2parquet', help='insert next <csv_filename> (and optional: <output_filename.parquet>) '
                                          'used to convert csv to parquet')
parser.add_argument('--parquet2csv', help='insert next <parquet_filename> (and optional: <output_filename.csv>) '
                                          'used to convert parquet to csv')
parser.add_argument('--get-schema', help="insert next <parquet_filename> to get it's schema")
args = parser.parse_args()


def csv2parquet(src, dst=None):
    df = pd.read_csv(src)
    if dst:
        df.to_parquet(dst)
    else:
        df.to_parquet(src.replace('.csv', '.parquet'))


def parquet2csv(src, dst=None):
    df = pd.read_parquet(src)
    if dst:
        df.to_csv(dst)
    else:
        df.to_parquet(src.replace('.parquet', '.csv'))


def get_schema(src):
    schema = pq.read_schema(src, memory_map=True)
    print(schema)


if __name__ == '__main__':

    arguments = sys.argv[1:]

    if arguments[0] == '--csv2parquet':
        if len(arguments) == 3:
            csv2parquet(arguments[1], arguments[2])
        elif len(arguments) == 2:
            csv2parquet(arguments[1])
        else:
            raise SyntaxWarning('Pass 1 or 2 arguments.')
    elif arguments[0] == '--parquet2csv':
        if len(arguments) == 3:
            parquet2csv(arguments[1], arguments[2])
        elif len(arguments) == 2:
            parquet2csv(arguments[1])
        else:
            raise SyntaxWarning('Pass 1 or 2 arguments.')
    elif arguments[0] == '--get-schema':
        get_schema(arguments[1])
