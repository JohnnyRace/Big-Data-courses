# Csv to Parquet Converter

This is a python script that allows you to convert csv to parquet and vice versa.

## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) (pip for Windows) to install required packages.

```bash
pip3 install pandas
pip3 install pyarrow
```
## Project requirements
```
numpy==1.21.0
pandas==1.2.5
pyarrow==4.0.1
python-dateutil==2.8.1
pytz==2021.1
six==1.16.0
```

## Usage

```bash
#If you need convert csv to parquet
python3 converter.py --csv2parquet csv_name.csv parquet_name.parquet
# If you need convert parquet to csv
python3 converter.py --parquet2csv parquet_name.csv csv_name.parquet
# To get schema of parquet file use it
python3 converter.py --get-schema parquet_name.parquet
# Also you can call help in console
python3 converter.py --help
```
Use ```python converter.py``` for Windows. 
You can insert the file name if it is in the project folder, or enter the full path to the file.
#### Usage scheme:
```bash
python3 converter.py [--csv2parquet | --parquet2csv <src-filename> <dst-filename>] | [--get-schema <filename>] | [--help]
```

### Support

Write me -> [Ilya Sokolov](https://t.me/r0ck6t)
