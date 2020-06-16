'''
Write a Python program to get the unique enumeration values. Go to the editor
Expected Output:
Afghanistan = 93
Albania = 355
Algeria = 213
Andorra = 376
Angola = 244
'''
from enum import Enum
class A(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    India = 355
    USA = 213
for i in A:
    print(i.name,i.value)