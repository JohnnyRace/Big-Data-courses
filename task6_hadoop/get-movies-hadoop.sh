hdfs dfs -rm /movies/*
hdfs dfs -rmdir /movies
hdfs dfs -mkdir /movies
hdfs dfs -put movies.csv /movies

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

hdfs dfs -rm /movies/output/*
hdfs dfs -rmdir /movies/output
hdfs dfs -rm /movies/output2/*
hdfs dfs -rmdir /movies/output2


yarn jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /movies/movies.csv \
                                                        -output movies/output \
                                                        -file mapper.py reducer.py \
                                                        -mapper "python3 mapper.py $regexp \
                                                                                   $year_from \
                                                                                   $year_to  \
                                                                                   $genres" \
                                                        -reducer "python3 reducer.py $number"

yarn jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /movies/output\
                                                        -output movies/output2 \
                                                        -files finalizer.py \
                                                        -mapper "python3 finalizer.py" \
