#encoding:utf-8

#CSV to JSON “计算机喜欢多样性”

import csv
reader = csv.reader(open('C:\\Users\\Eyr3\\visual\\data.txt','r'),delimiter = ',')

print "{ oberservations: ["
rows_so_far = 0
for row in reader:
    rows_so_far += 1

    print '{'
    print '"data":' + '"' + row[0] + '",'
    print '"temperature":' + '"' + row[1]

    if rows_so_far < 365:
        print ' },'
    else:
        print ' }'

print "] }"