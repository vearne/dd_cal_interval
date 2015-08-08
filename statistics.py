def judge(l):
	for i in range(28):
		if l >= i and l <= i + 1:
			return i 
	
dd = {}
fp = open('result.txt', 'r')
sum = 0
count = 0
for i in range(28):
	dd[i] = 0


for line in fp:
	uid, interval = line.split()	
	#print interval
	level = judge(float(interval))
	#print level
	dd[level] += 1
	
	sum += float(interval)
	count += 1
	

print '--------distribute---------'
print dd
print '--------statistics---------'
print sum / count 
fp.close()
	

