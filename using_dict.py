#!/usr/bin/python
ab={'a':1,
    'b':2,
    'c':3,
    'd':4,
}
print "b's num is %d" % ab['b']
ab['e']=5
del ab['a']
print "there are %d contacts" % len(ab)
for name,num in ab.items():
  print "contact %s at %d" % (name,num)
if 'c' in ab:
  print "c's num is %d" % ab['c']
