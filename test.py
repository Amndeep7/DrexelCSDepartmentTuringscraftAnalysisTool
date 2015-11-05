#!/usr/bin/env python

import csv
import sys

f1 = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f1)
    for row in reader:
        print row
finally:
    f1.close()

