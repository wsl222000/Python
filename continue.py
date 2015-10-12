#!/usr/bin/python
while True:
  s=raw_input('Enter something : ')
  if s == 'quit':
    break
  elif len(s)<3:
    continue
  else:
    print 'Input is of sufficient length'
