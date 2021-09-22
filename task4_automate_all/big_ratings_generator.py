import random
import numpy as np
import os
import csv

name_files = os.listdir(path='/home/johnrace/Develop/Big_Data_School/task5_big_dataset/ml-20mx16x32')

with open('ratings.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['userId', 'movieId', 'rating', 'timestamp'])
    for file in name_files:
        if file.split('x')[0] == 'train':
            data = np.load(f'/home/johnrace/Develop/Big_Data_School/task5_big_dataset/ml-20mx16x32/{file}', mmap_mode='r')
            for row in data['arr_0']:
                line = list(row)
                line.append(random.choice([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]))
                line.append(1)
                writer.writerow(line)
