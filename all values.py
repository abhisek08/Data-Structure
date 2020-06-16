'''
 Write a Python program to get all values from an enum class.
Expected output:
[93, 355, 213, 376, 244, 672]
'''
from enum import Enum
class A(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
l=[]
for i in A:
    l.append(i.value)
print(l)