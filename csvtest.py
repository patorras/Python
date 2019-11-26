import os
from os import walk
import csv

f = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    f.extend(filenames)
    break

for i in f:
    print(i)


row = f
with open('test.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(row)

csvFile.close()
