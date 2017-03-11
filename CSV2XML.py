import csv
reader = csv.reader(open('C:\\Users\\Eyr3\\visual\\data.txt','r'),delimiter = ',')
f = open('C:\\Users\\Eyr3\\visual\\data.xml','w')

f.write('<weather_data>' + '\n')

for row in reader:
    f.write('<observation>' + '\n')
    f.write('<data>' + row[0] + '</data>' + '\n')
    f.write('<temperature>' + row[1] + '</temperature>' + '\n')
    f.write('</oberservation>' + '\n')

f.write('</weather_data>' + '\n')

f.close()