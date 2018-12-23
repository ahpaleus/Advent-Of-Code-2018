#!/usr/bin/python
import re
import numpy as np

np.set_printoptions(suppress=True)

file_input = open('input.txt','r')
file_content = file_input.read()
file_strings = file_content.splitlines()

guards = re.findall(r'(?<=#)\d*',file_content)
guards = list(set(guards))
days = list(set(re.findall(r'(?<=\-)[^ ]+',file_content)))

r = re.compile(r'(?<=-)(.*)(?=])')
sorted_input = sorted(file_strings, key=lambda x:r.search(x).group(1))

data = np.zeros((len(file_strings)+1,62))

iteration = 0
number = 0
previous_iteration = 0
previous_minute = 0

for x in sorted_input:
	figure = re.findall(r'(?<=#)\d*',x)
	if figure:
		number = figure
	day = re.findall(r'(?<=\-)[^ ]+',x)

	day = int((day[0]).replace('-',''))
	data[iteration,0] = day
	data[iteration,1] = int(number[0])
	
	if 'falls asleep' in x:
		minute = int(re.findall(r'(?<=:)\w\w',x)[0])
		previous_minute = minute
		previous_iteration = iteration
		
	elif 'wakes up' in x:
		minute = int(re.findall(r'(?<=:)\w\w',x)[0])
		data[iteration-1,minute+2] = 2		
		it = 0
		while data[iteration-1,previous_minute+2+it] != 2:
			data[iteration-1,previous_minute+2+it] = 1
			it+=1
	iteration +=1

data = data[~np.all(data[:,2:] == 0, axis=1)]

results = []

for x in data: 
	results.append([int(x[1]),x[np.where(x == 1)].size])
	
r = {}
for k, v in results:
	r[k] = r.get(k, 0) + v
r = r.items()

sorted_input = sorted(r, key=lambda x: x[1], reverse=True)

most_sleepy_guard = sorted_input[0][0]

most_sleepy_array = np.arange(62)
for x in data: 
	if x[1] == most_sleepy_guard: 
		most_sleepy_array = np.vstack([most_sleepy_array,x])

for x in xrange(60):
	a = list(most_sleepy_array[:,x+2])
	results.append(a.count(1))

most_sleepy_minute = results.index(max(results))

print 'Result #1: ' + str(most_sleepy_minute*most_sleepy_guard)

matrix = [[0]*61 for i in range(len(guards))]

for i,guard in enumerate(guards):
	a = data[data[:,1] == int(guard)]
	matrix[i][0] = guard
	for x in xrange(60):
		b = a[:,x+2]
		occurences = np.count_nonzero(b == 1)
		matrix[i][x+1] = occurences

maxy = 0
minute = 0
guard = 0
for x in matrix:
	if max(x[1:]) > maxy:
		maxy = int(max(x[1:]))
		minute = int(x.index(max(x[1:]))-1)
		guard = int(x[0])

result = minute*guard

print 'Result #2: ' + str(result)