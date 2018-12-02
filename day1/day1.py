#!/usr/bin/python

file = open('input','r')

result = []

for x in file:
	result.append(int(x))

freq = 0
for x in result:
	freq += x

print str(freq)

i = 0
frequencies = set()
sum_freq = 0

while True:
	if i == len(result):
		i = 0
	if sum_freq in frequencies:
		print str(sum_freq)
		break
	frequencies.add(sum_freq)
	sum_freq += result[i]
	
	i += 1
	