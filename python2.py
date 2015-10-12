#!/usr/bin/python
while True:
	s=raw_input('Input:')
	if s=='quit':
		break
	if len(s)<3:
		continue
	print 'Input is ok!'
