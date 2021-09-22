while [ -n "$1" ]; do
case "$1" in
  --regexp) regexp="--regexp $2";;
  --year_from) year_from="--year_from $2";;
  --year_to) year_to="--year_to $2";;
  -N) number="-N $2";;
  --genres) genres="--genres $2";;
esac
shift
done

python3 mapper.py  < "movies.csv" "$regexp"  "$year_from" "$year_to"  "$genres" |
python3 shuffler-sorter.py |
python3 reducer.py "$number"  |
python3 finalizer.py
