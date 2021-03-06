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
turn = -1
LPCB = []
for i in range(20):
	LPCB.append(rand_pcb(i))
#print(LPCB)
Lt = []
for i in range(20):#这里例化了20个线程存在了Lt里，其实没必要，可以在循环里例化
	t = threading.Thread(target = son_thread)
	Lt.append(t)

for x in LPCB:
	turn = x['pid']
	Lt[turn].start()
	Lt[turn].join()
	LPCB[turn]['not_been_run'] = False
	now_time += x['duration']
	for y in list(filter(lambda d:d['not_been_run'], LPCB)):
		y['wait_time'] += x['duration']
sum_wait_time = 0
for x in LPCB:
	#print(x['wait_time'])
	sum_wait_time += x['wait_time']
print('FCFS avr_wait_time: ', sum_wait_time/20)
