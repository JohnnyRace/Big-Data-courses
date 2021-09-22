# Get Movies from CSV script

This is a python script that allows you to get movies from csv by your own filters with CSV like output.

## Installation

Just install Python 3.7+ and run the script.
```bash
# Usage scheme
python3 get-movies.py [--genres <"Genre1|Genre2|...GenreN"][--regexp <"regular expression">][--year_from and/or --year_to <year>][--N <number>]
```
## Usage

```bash
# Return all films with "love" word
python3 get-movies.py --regexp love
# Return all films with Action and/or Comedy genre
python3 get-movies.py --genres "Action|Comedy"
# Return all films from 2000 till 2005 year
python3 get-movies.py --year_from 2000 --year_to 2005
# Return 3 most rating films
python3 get-movies.py -N 3
```
Use ```python get-movies.py``` for Windows.

### Support

Write me -> [Ilya Sokolov](https://t.me/r0ck6t)
