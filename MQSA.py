#coding = utf-8

import threading, random

def rand_pcb(i):
	a = {}
	a['duration'] = random.randint(1, 20)
	a['priority'] = random.randint(1, 10)
	a['wait_time'] = 0
	a['pid'] = i
	a['not_run'] = True
	return a

def son_thread(given_time, flag):
	local_pcb = LPCB[turn]
	print('%s sum: %d' % (threading.current_thread().name, local_pcb['duration']))
	for i in range(given_time):
		print('    %s: %d' % (threading.current_thread().name, now_time + i +1))
	if flag:
		local_pcb['not_run'] = False
		
FCFS = []
SJF = []
PRIO = []
RR = []
LPCB = []

for i in range(20):
	temp = rand_pcb(i)
	LPCB.append(temp)
	if i < 5:
		FCFS.append(temp)
	elif i < 10:
		SJF.append(temp)
	elif i < 15:
		PRIO.append(temp)
	else:
		RR.append(temp)

now_time = 0

for x in FCFS: #FCFS
	turn = x['pid']
	t = threading.Thread(target = son_thread, name = 'Thread-%d' % (x['pid'] + 1), args = (x['duration'], True))
	t.start()
	t.join()
	now_time += x['duration']
	for y in list(filter(lambda d:d['not_run'], LPCB)):
		y['wait_time'] += x['duration']

for x in sorted(SJF, key = lambda d:d['duration']): #SJF
	turn = x['pid']
	t = threading.Thread(target = son_thread, name = 'Thread-%d' % (x['pid'] + 1), args = (x['duration'], True))
	t.start()
	t.join()
	now_time += x['duration']
	for y in list(filter(lambda d:d['not_run'], LPCB)):
		y['wait_time'] += x['duration']	
for x in sorted(PRIO, key = lambda d:d['priority']): #Priority
	turn = x['pid']
	t = threading.Thread(target = son_thread, name = 'Thread-%d' % (x['pid'] + 1), args = (x['duration'], True))
	t.start()
	t.join()
	now_time += x['duration']
	for y in list(filter(lambda d:d['not_run'], LPCB)):
		y['wait_time'] += x['duration']
ts = random.randint(5, 12)
print('time slice: %d' % ts)
#print(list(map(lambda x:x['pid'], LPCB)))
while len(RR) > 0: #RR
	turn = RR[0]['pid']
	temp = LPCB[turn]['duration']
	flag = (temp <= ts)
	if flag:
		given_time = RR[0]['duration']
	else:
		given_time = ts
	t = threading.Thread(target = son_thread, name = 'Thread-%d' % (turn + 1), args = (given_time, flag))
	t.start()
	t.join()
	for y in list(filter(lambda d:d['not_run'], LPCB)):
		y['wait_time'] += x['duration']
	LPCB[turn]['duration'] -= ts
	if not flag:
		RR.append(RR[0])
	now_time += ts
	RR.pop(0)

#print(list(map(lambda x:x['wait_time'], LPCB)))
sum_time = 0
for x in list(map(lambda x:x['wait_time'], LPCB)):
	sum_time += x
print('MQSA avr_time: ', sum_time/20)
