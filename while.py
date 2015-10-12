#!/usr/bin/python
num=23
while True:
  guess=int(raw_input('enter an integer:'))
  if guess == num:
    print 'you guessed it'
    break
  elif guess < num:
    print 'lower'
  else:
    print 'higher'
print 'loop is over'
