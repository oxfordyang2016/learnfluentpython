'''
Sorting is expensive, so once you have a sorted sequence, 
it’s good to keep it that way. That is why bisect.insort was created.
insort(seq, item) inserts item into seq so as to keep seq in ascending order.
'''


import bisect
import random
SIZE = 7
random.seed(1729)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2) 
    bisect.insort(my_list, new_item) 
    print('%2d ->' % new_item, my_list)
    