# Get Movies from CSV using MySQL script

This is a python script that allows you to get movies from csv using SQL by your own filters with CSV like output.

## Installation

Install [Python 3.7+](https://www.python.org/downloads/) and requirements.
```bash
# use pip for Windows and pip3 for Linux
pip3 install -r requirements.txt
```

## Usage
You need to use the script as an administrator (root user) because Dask uses technologies and resources, access to which is closed to a regular user.
```bash
# Return all films with "war" word
sudo python3 get-movies.py --regexp war
# Return all films with Action and/or Comedy genre
sudo python3 get-movies.py --genres "Action|Comedy"
# Return all films from 2000 till 2005 year
sudo python3 get-movies.py --year_from 2000 --year_to 2005
# Return 3 most rating films
sudo python3 get-movies.py -N 3
```
Use ```python get-movies.py``` for Windows and run Command Prompt as Administrator.

If you use all the above parameters, then the result will be like:
```
genre,title,year,rating
Action|Adventure|Drama,Warriors of Heaven and Earth Tian di ying xiong,2003,3.25
Action|Adventure|Drama|War,Musa the Warrior Musa,2001,4.5
Action|Adventure|Fantasy|Sci-Fi,Godzilla: Final Wars Gojira: Fainaru uôzu,2004,3.0
```

### Support
Write me -> [Ilya Sokolov](https://t.me/r0ck6t)
