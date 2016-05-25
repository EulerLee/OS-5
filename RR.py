#coding = utf-8

import threading, random

def rand_pcb(i):
	a = {}
	a['duration'] = random.randint(1, 20)
	a['priority'] = random.randint(1, 10)
	a['wait_time'] = 0
	a['pid'] = i + 1
	return a

def son_thread():
	thread_pcb = FIFO[0]
	print('thread-', thread_pcb['pid'], 'sum: ', thread_pcb['duration'])
	if thread_pcb['duration'] <= ts:
		for i in range(now_time, now_time + thread_pcb['duration']):
			print('thread-', thread_pcb['pid'], ': ', i + 1)
		thread_pcb['duration'] = 0
		LPCB[thread_pcb['pid'] - 1]['duration'] = 0
	else:
		for i in range(now_time, now_time + ts):
			print('thread-', thread_pcb['pid'], ': ', i + 1)
		thread_pcb['duration'] -= ts
		FIFO.append(thread_pcb)
	FIFO.pop(0)

LPCB = []
FIFO = []
for i in range(20):
	temp = rand_pcb(i)
	LPCB.append(temp)
	FIFO.append(temp)

ts = int(input('set time slice: '))
now_time = 0
while len(FIFO) > 0:
	t = threading.Thread(target = son_thread)
	temp = FIFO[0]['duration']
	flag = (temp > ts)
	for x in LPCB:
		if x['pid'] != FIFO[0]['pid'] and x['duration'] > 0:
			if flag:
				x['wait_time'] += ts
			else:
				x['wait_time'] += temp
	t.start()
	t.join()
	if flag:
		now_time += ts
	else:
		now_time += temp
sum_time = 0
for x in LPCB:
	sum_time += x['wait_time']
print('RR avr_time: ',sum_time/20)
