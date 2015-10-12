#!/usr/bin/python
filename=raw_input('file name:')
fobj=open(filename,'r')
for line in fobj:
  print line,
fobj.close()
