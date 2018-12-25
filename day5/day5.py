#!/usr/bin/python
import re

file_input=open('input','r')
file_content = file_input.read()

def polym(input_file_content):
	pairs = []
	for x in xrange(0x5a-0x40):
		pairs.append(chr(0x41+x) + chr(0x41+x+0x20))
		pairs.append(chr(0x41+x+0x20) + chr(0x41+x))
	prev = 0
	while len(input_file_content) != prev:
		prev = len(input_file_content)
		for x in pairs:
			input_file_content = input_file_content.replace(x,'')
	return input_file_content

print 'Solution #1: ' + str(len(polym(file_content)))

results = {}

for x in xrange(0x5a-0x40):
	temp = file_content
	temp = temp.replace(chr(0x41+x),'')
	temp = temp.replace(chr(0x41+x+0x20),'')
	results[chr(0x41+x)] = len(polym(temp))

min_value = min(results.keys(), key=(lambda k: results[k]))
print 'Solution #2: ' + str(results[min_value])
