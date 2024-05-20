# What does this piece of code do?
# Answer:This code works by increasing progress until it reaches 100 and adding a random integer and prints out the culmulative sum 
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
total_random_number=0
while progress<100:
 progress+=1
 n = randint(1,10)
 total_random_number = total_random_number+n

print(total_random_number)
