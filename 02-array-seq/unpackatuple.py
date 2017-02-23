#fp28
#unpack a tuple 's advanced usage
#simple
a,b,c=(1,2,3)
#related a list
a,*b,c=(1,23,3,4,56,7,8,99,9)
#b= [23, 3, 4, 56, 7, 8, 99] is a list


def unpackatuple(a,b,c):
    return(a+b+c)
#The % formatting operator understands tuples and treats each item as a separate field
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

a=(1,2,3)
print(unpackatuple(*a))
a,b,c=(1,2,3)
#note it is  a tuple
print(a,b,c)
#but in the console,the a,b,c is a tuple,but the above is 1,2,3

#how to split a file path to two part (dir,filename)
#_ like placeholder usage
#unpack a tuple
import os
#Sometimes when we only care about certain parts of a tuple when unpacking, a dummy
#variable like _ is used as placeholder %, as in the example above.seem a things a,*c,d=range(6)
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print filename#idrsa.pub
'''
powerful *,list,parallel assignment 
In Python 3 this idea was extended to apply to parallel assignment as well.
>>> a, b, *rest = range(5)
>>> a, b, rest
(0, 1, [2, 3, 4])
>>> a, b, *rest = range(3)
>>> a, b, rest
(0, 1, [2])
>>> a, b, *rest = range(2)
>>> a, b, rest
(0, 1, [])
In the context of parallel assignment, the * prefix can be applied to exactly one variable,
but it can appear in any position:
>>> a, *body, c, d = range(5)
>>> a, body, c, d
(0, [1, 2], 3, 4)
>>> *head, b, c, d = range(5)
>>> head, b, c, d
([0, 1], 2, 3, 4)
Finally, a powerful feature of tuple unpacking is that it works with nested structures
'''


'''
unpack a nested tupe and print format contorl
In [114]: metro_areas = [
     ...:  ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), #
     ...:  ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
     ...:  ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
     ...:  ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
     ...:  ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),]


In [115]: print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
     ...: fmt = '{:15} | {:9.4f} | {:9.4f}'
     ...: for name, cc, pop, (latitude, longitude) in metro_areas: #
     ...:     if longitude <= 0: #
     ...:         print(fmt.format(name, latitude, longitude))


                |   lat.    |   long.
Mexico City     |   19.4333 |  -99.1333
New York-Newark |   40.8086 |  -74.0204
Sao Paulo       |  -23.5478 |  -46.6358
'''