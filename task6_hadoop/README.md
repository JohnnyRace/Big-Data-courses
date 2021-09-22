# Get Movies from CSV using MySQL and Hadoop

This is a python script that allows you to get movies from csv using only SQL or with Hadoop with your own filters with CSV like output.

## Installation

Just install [Python 3.7+](https://www.python.org/downloads/)


## Usage

```bash
# Usage scheme
sudo bash get-movies.sh [--genres <"Genre1|Genre2|...GenreN"][--regexp <"regular expression">][--year_from and/or --year_to <year>][-N <number>][-setupdb]
```
```bash
# Return all films with "war" word
sudo bash get-movies.sh --regexp war
# Return all films with Action and/or Comedy genre
sudo bash get-movies.sh --genres "Action|Comedy"
# Return all films from 2000 till 2005 year
sudo bash get-movies.sh --year_from 2000 --year_to 2005
# Return 3 most rating films
sudo bash get-movies.sh -N 3
```
You can combine all the parameters above.
If you try it, the result will be like:
```
genre,title,year,rating
Action|Adventure|Drama,Warriors of Heaven and Earth Tian di ying xiong,2003,3.25
Action|Adventure|Drama|War,Musa the Warrior Musa,2001,4.5
Action|Adventure|Fantasy|Sci-Fi,Godzilla: Final Wars Gojira: Fainaru uôzu,2004,3.0
```
## Usage hadoop distribution file system

```bash
sudo bash get-movies-hadoop.sh
```
```bash
sudo bash get-movies-hadoop.sh 'action'
```
```bash
sudo bash get-movies-hadoop.sh --regexp father --year_from 1990 --year_to 2000
```
```bash
sudo bash get-movies-hadoop.sh -N 5 --genres 'action|comedy' --year_from 2000 --year_to 2020
```
### Support
Write me -> [Ilya Sokolov](https://t.me/r0ck6t)