#encoding:utf-8

#BeautifulStoneSoup 用于解析更为广泛的 XML

from bs4 import BeautifulStoneSoup

f1 = open('C:\\Users\\Eyr3\\visual\\data.xml','r')
xml = f1.read()
f2 = open('C:\\Users\\Eyr3\\visual\\data_2.txt','w')

soup = BeautifulStoneSoup(xml)
oberservations = soup.findAll('oberservation')

for o in oberservations:
    f2.write(o.data.string + ',' + o.temperature.string + '\n')

f1.close()
f2.close()
