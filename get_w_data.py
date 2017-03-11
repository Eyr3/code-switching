import random

f = open('C:\\Users\\Eyr3\\visual\\data.txt','w')

for m in range(1,13):
	for d in range(1,32):
		if (m == 2 and d > 28):
			break
		elif (m in [4,6,9,11] and d > 30):
			break
			
		if len(str(m)) < 2:
			mstamp = '0' + str(m)
		else:
			mstamp = str(m)
		
		if len(str(d)) < 2:
			dstamp = '0' + str(d)
		else:
			dstamp = str(d)
		
		timestamp = '2016' + mstamp + dstamp
		
		daytemp = random.randint(0,40)
		
		f.write(timestamp + ',' + str(daytemp) + '\n')

f.close()