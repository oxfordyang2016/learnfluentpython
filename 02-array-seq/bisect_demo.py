# BEGIN BISECT_DEMO
#list comprehension
#this is list comprelist ,you can use it do such as cartesian product
#about cartesian product https://en.wikipedia.org/wiki/Cartesian_product
'''
>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> tshirts = [(color, size) for color in colors for size in sizes]
>>> tshirts
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
'''
'''
fp 25
from my opinion,generator's key is to invoke generator object
for example ,((a,b) for a in 'srting' for b in 'ming') will produce a generator object
such as  <generator object <genexpr> at 0x00000000050107E0>
but when you use [k for k in ((a,b) for a in 'srting' for b in 'ming') ],it will produce a list
'''

# sort a list 2 (fp 27)
'''
>>> traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]
>>> sorted(traveler_ids) 
[('BRA', 'CE342567'), ('ESP', 'XDA205856'), ('USA', '31195855')]
'''
import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # <1>
        offset = position * '  |'  # <2>
        print(ROW_FMT.format(needle, position, offset))  # <3>


if __name__ == '__main__':

    if sys.argv[-1] == 'left':    # <4>
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)  # <5>
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

# END BISECT_DEMO











