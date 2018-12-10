#!/usr/bin/python
import re
import numpy as np

dane = np.zeros((1000,1000))

file = open('input','r')
file_strings = []
file_strings = file.read().splitlines()

'''
#123 @ 3,2: 5x4 <- [ID, 3 od lewej, 2 od gory, 5 szerokosci, 4 dlugosci]
'''
lista = []

for x in file_strings:
	identify = int(re.search(r'#(.*?)\s',x).group(1))
	left = int(re.search(r'@\s(.*?),',x).group(1))
	right = int(re.search(r',(.*?):',x).group(1))
	width = int(re.search(r':\s(.*?)x',x).group(1))
	height = int(re.search(r'x(.*?)$',x).group(1))
	lista.append([identify,left,right,width,height])
	
for a,b,c,d,e in lista:
	dane[c:c+e,b:b+d] += 1

#print dane

print 'Wszystkie jedynki: ' + str(len(np.where(dane == 1)[0]))

print 'ID: ',
for a,b,c,d,e in lista:
	if np.all(dane[c:c+e,b:b+d] == 1):
		print a