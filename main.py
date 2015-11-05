import csv
import sys
from random import randint


#This script creates and writes to a csv file

f = open(sys.argv[1], 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('ID', 'Name', 'Grade') )
    for i in range(10):
        writer.writerow( (i+1, chr(ord('a') + i), randint(0,100)) )
finally:
    f.close()

print(open(sys.argv[1], 'rt').read())
