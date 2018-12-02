#!/usr/bin/python
from collections import Counter
import itertools
import sys

def hamming_distance(s1,s2):
	return sum(el1 != el2 for el1, el2 in zip(s1, s2))

file = open('input.txt','r')
file_strings = []
file_strings = file.read().splitlines()

countery = []

for x in file_strings:
	countery.append(Counter(x).most_common(2))
	
def check(text):
	table = [0] * 2
	if text[0][1] == text[1][1]:
		if text[0][1] == 3:
			table[1] += 1
		elif text[0][1] == 2:
			table[0] += 1
		return table
	elif text[0][1] == 2:
		table[0] += 1
	elif text[0][1] == 3:
		table[1] += 1
	if text[1][1] == 2:
		table[0] += 1
	elif text[1][1] == 3:
		table[1] += 1
	return table
		
double = 0 
three = 0
for x in countery:
	double += check(x)[0]
	three += check(x)[1]	
	
result = double * three
print str(result)

similar = []

for a, b in itertools.combinations(file_strings, 2):
	if hamming_distance(a, b) == 1:
		similar.append(a)
		similar.append(b)
		
for x in range(len(similar[0])):
	if similar[0][x] == similar[1][x]:
		sys.stdout.write(similar[0][x])
