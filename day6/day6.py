#!/usr/bin/python
#coding: -utf-8-
import numpy as np

def manhattan_distance(a,b):
	return abs(b[0]-a[0]) + abs(b[1]-a[1])

entries = [[int(x) for x in x.split(", ")] for x in open("input.txt","r").read().splitlines()]

max_x = max([x[0] for x in entries])+1
max_y = max([x[1] for x in entries])+1

result_matrix = np.zeros((max_x,max_y))
for y in xrange(max_y):
	for x in xrange(max_x):
		temp = []
		for i in entries:
			manh = manhattan_distance([x,y], i)
			if manh not in temp: temp.append(manh)
			else: break
		if len(temp) > 1:
			if sorted(temp)[0] == sorted(temp)[1]:	
				result_matrix[x,y] = -1
			else:
				result_matrix[x,y] = temp.index(min(temp))

infinite = set()
[infinite.add(x) for x in np.unique(result_matrix[0])]
[infinite.add(x) for x in np.unique(result_matrix[-1])]
[infinite.add(x) for x in np.unique(result_matrix[:,[-1]])]
[infinite.add(x) for x in np.unique(result_matrix[:,[0]])]

unique, counts = np.unique(result_matrix, return_counts=True)
result = dict(zip(unique, counts))

print 'Solution #1: ' + str(max(sorted([result[x] for x in [x for x in result if x not in infinite and x != -1]])))

minimum = 10000

distances = set()
for y in xrange(max_y):
	for x in xrange(max_x):
		suma = 0
		for i in entries:
			manh = manhattan_distance([x,y], i)
			suma += manh
			if suma > minimum:
				break
		if suma < minimum: 
			distances.add((x,y))

print 'Solution #2: ' + str(len(distances))
