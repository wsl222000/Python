#!/usr/bin/python
class FooClass(object):
version = 0.1 # class (data) attribute
def showver(self):
  """display class(static) attribute"""
  print self.version # references FooClass.version
