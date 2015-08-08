from datetime import datetime

def cal_interval(ll):
	count = len(ll)
	return (28 - count)/float(count)


# ---------------------------------------------

base_date = datetime(2015, 7, 11)

# source
fp = open('temp.txt', 'r')
# result
result_fp = open('result.txt', 'w')

ll = []
curr_uid = '#'
for line in fp:
	uid, t = line.split()	
	t = datetime.strptime(t,'%Y-%m-%d')
	t = (t - base_date).days 
	if curr_uid == '#':
		curr_uid = uid

	if  curr_uid == uid:
		ll.append(t)	
	else:
		interval = cal_interval(ll)		
		result_fp.write(curr_uid + " " + str(interval))
		result_fp.write('\n')
		# another user
		ll = []
		curr_uid = uid
		ll.append(t)
	#print uid, (t - base_date).days

# last user
interval = cal_interval(ll)		
result_fp.write(curr_uid + " " + str(interval))

fp.close()
result_fp.close()



			
			



