#!/bin/bash

if [[ ! -e "temp/venv" ]]; then
  mkdir -p "temp"
  cd "temp"
  pip3 install --user pip --no-warn-script-location -q
  pip3 install --user virtualenv -q
  python3 -m venv venv
  source venv/bin/activate

  pip3 install -r ../requirements.txt -q
  pip3 install "dask[dataframe]" -q
  cp ../get-movies.py .
  wget https://files.grouplens.org/datasets/movielens/ml-latest-small.zip -q
  unzip -q ml-latest-small.zip
  cp -u ml-latest-small/movies.csv ml-latest-small/ratings.csv .
  rm -r -f ml-latest-small*
  cd ..
fi
cd "temp"
source venv/bin/activate
python3 get-movies.py "$@"
deactivate
