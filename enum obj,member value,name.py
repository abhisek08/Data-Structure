'''
Write a Python program to create an Enum object and display a member name and value.
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
Antarctica = 672
Expected Output :
Member name: Albania
Member value: 355
'''
from enum import Enum
class A(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print(A.Angola.name)
print(A.Angola.value)