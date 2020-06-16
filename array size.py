'''
Write a Python program to get the array size of types unsigned integer and float.
'''
from array import array
c=array('i',[12,120])
print(c.itemsize)
c=array('f',[12.1,120.1])
print(c.itemsize)