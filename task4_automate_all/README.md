# Get Movies from CSV using MySQL script

This is a python script that allows you to get movies from csv using SQL by your own filters with CSV like output.

## Installation

Just install [Python 3.7+](https://www.python.org/downloads/)

If you want test it with big dataset, you need to download it and unzip in directory with `big_ratings_generator.py`.


## Usage

```bash
# Usage scheme
sudo ./get-movies.sh [--genres <"Genre1|Genre2|...GenreN"][--regexp <"regular expression">][--year_from and/or --year_to <year>][-N <number>][-setupdb]
```
You need to use the script as an administrator (root user) because Dask uses technologies and resources, access to which is closed to a regular user.
```bash
# Download data and prepare database
sudo ./get-movies.sh -setupdb
# Return all films with "war" word
sudo ./get-movies.sh --regexp war
# Return all films with Action and/or Comedy genre
sudo ./get-movies.sh --genres "Action|Comedy"
# Return all films from 2000 till 2005 year
sudo ./get-movies.sh --year_from 2000 --year_to 2005
# Return 3 most rating films
sudo ./get-movies.sh -N 3
```
You can combine all the parameters above.
If you try it, the result will be like:
```
genre,title,year,rating
Action|Adventure|Drama,Warriors of Heaven and Earth Tian di ying xiong,2003,3.25
Action|Adventure|Drama|War,Musa the Warrior Musa,2001,4.5
Action|Adventure|Fantasy|Sci-Fi,Godzilla: Final Wars Gojira: Fainaru uôzu,2004,3.0
```

### Support
Write me -> [Ilya Sokolov](https://t.me/r0ck6t)
