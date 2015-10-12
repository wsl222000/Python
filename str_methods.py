#!/usr/bin/python
name='hello'
if name.startswith('he'):
  print 'yes,the string starts with "he"'
if 'o' in name:
  print 'yes,it contaings the string "o"'
if name.find('ll') != -1:
  print 'yes,it contains the string "ll"'
delimiter='_*_'
mylist=['a','b','c','d']
print delimiter.join(mylist)
