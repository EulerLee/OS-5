#coding=utf-8

import threading, random

PCB = threading.local()
def rand_pcb(i):
	PCB = {}
	PCB['duration'] = random.randint(1, 20)
	PCB['priority'] = random.randint(1, 10)
	PCB['wait_time'] = 0
	PCB['pid'] = i
	PCB['not_been_run'] = True
	return PCB
def son_thread():
	thread_pcb = LPCB[turn]
	print(threading.current_thread().name, "sum: ", thread_pcb['duration'])
	for i in range(now_time, now_time + thread_pcb['duration']):
		print('    ', threading.current_thread().name, ': ', i + 1)

now_time = 0
running_time = 0
turn = -1
LPCB = []
for i in range(20):
	LPCB.append(rand_pcb(i))
#print(list(map(lambda x:x['priority'], LPCB)))
Lt = []
for i in range(20):
	t = threading.Thread(target = son_thread)
	Lt.append(t)

for x in sorted(LPCB, key = lambda x:x['priority']):
	turn = x['pid']
	Lt[turn].start()
	Lt[turn].join()
	LPCB[turn]['not_been_run'] = False
	now_time += x['duration']
	for y in list(filter(lambda d:d['not_been_run'], LPCB)):
		y['wait_time'] += x['duration']
sum_wait_time = 0
for x in LPCB:
	sum_wait_time += x['wait_time']
print('Priority avr_wait_time: ', sum_wait_time/20)
