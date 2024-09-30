import random
from time import process_time_ns

print(random.randint(5, 20))  # line 1
#Max:20 Min:5
print(random.randrange(3, 10, 2))  # line 2
#Max:9 Min:3 unable to produce a 4
print(random.uniform(2.5, 5.5))  # line 3
#Max:5.5 Min:2.5

print(random.randint(1,100))
