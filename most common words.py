'''
Write a Python program to count the most common words in a dictionary.
Expected Output:
[('pink', 6), ('black', 5), ('white', 5), ('red', 4)]
'''
from collections import Counter
words = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
]
print(Counter(words).most_common(4))