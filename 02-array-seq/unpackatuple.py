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



# namedtuple fp 30 how to think the use of named tuple
#method 1
Card = collections.namedtuple('Card', ['rank', 'suit'])
#method 2
'''
Example 2-9. Defining and using a named tuple type
>>> from collections import namedtuple
>>> City = namedtuple('City', 'name country population coordinates')
>>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
>>> tokyo
City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
>>> tokyo.population
36.933
>>> tokyo.coordinates
(35.689722, 139.691667)
>>> to
Two parameters are required to create a named tuple: a class name and a list of
field names, which can be given as an iterable of strings or as a single spacedelimited
string.
Data must be passed as positional arguments to the constructor (in contrast, the
tuple constructor takes a single iterable).
You can access the fields by name or position.
'''
'''
#namedtuple as records.
Example 2-10. Named tuple attributes and methods (continued from Example 2-9)
>>> City._fields
('name', 'country', 'population', 'coordinates')
>>> LatLong = namedtuple('LatLong', 'lat long')
>>> delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
>>> delhi = City._make(delhi_data)
>>> delhi._asdict()
OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population',
21.935), ('coordinates', LatLong(lat=28.613889, long=77.208889))])
>>> for key, value in delhi._asdict().items():
        print(key + ':', value)
name: Delhi NCR
country: IN
population: 21.935
coordinates: LatLong(lat=28.613889, long=77.208889)
_fields is a tuple with the field names of the class.
_make() lets you instantiate a named tuple from an iterable; City(*delhi_da
ta) would do the same.
_asdict() returns a collections.OrderedDict built from the named tuple
instance. That can be used to produce a nice display of city data
'''

#slicing
'''
Every Python programmer knows that sequences can be sliced using the s[a:b] syntax.
We now turn to some less well-known facts about slicing.

'''

#how to split  pagraph to lines????
invoice = """
0.....6.................................40........52...55........
1909  Pimoroni PiBrella                      $17.50  3    $52.50
1489  6mm Tactile Switchx20                   $4.95  2    $9.90
1510  Panavise Jr. - PV-201                  $28.00  1    $28.00
1601  PiTFT Mini Kit 320x240                 $34.95  1    $34.95
 """

line_items = invoice.split('\n')[3:]
print(line_items)
'''
['1489  6mm Tactile Switchx20                   $4.95  2    $9.90',
 '1510  Panavise Jr. - PV-201                  $28.00  1    $28.00',
 '1601  PiTFT Mini Kit 320x240                 $34.95  1    $34.95',
 ' ']
'''

invoicetest = """
1909  Pimoroni PiBrella                      $17.50  3    $52.50
1489  6mm Tactile Switchx20                   $4.95  2    $9.90
1510  Panavise Jr. - PV-201                  $28.00  1    $28.00
1601  PiTFT Mini Kit 320x240                 $34.95  1    $34.95
 """
print(invoicetest.split('\n'))
'''
['',
 '1909  Pimoroni PiBrella                      $17.50  3    $52.50',
 '1489  6mm Tactile Switchx20                   $4.95  2    $9.90',
 '1510  Panavise Jr. - PV-201                  $28.00  1    $28.00',
 '1601  PiTFT Mini Kit 320x240                 $34.95  1    $34.95',
 ' ']
'''
 a=invoicetest.split('\n')#note that a[0]='',a[-1]='' for invoice test spicial first line last line format
 print(a[1:len(a)-1])
 '''
 ['1909  Pimoroni PiBrella                      $17.50  3    $52.50',
 '1489  6mm Tactile Switchx20                   $4.95  2    $9.90',
 '1510  Panavise Jr. - PV-201                  $28.00  1    $28.00',
 '1601  PiTFT Mini Kit 320x240                 $34.95  1    $34.95']
  '''
'''
 In [45]: for k in a[1:len(a)-1]:
    ...:     print(k[slice(0,2)])
19
14
15
16 
'''
'''
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)

>>> UNIT_PRICE = slice(40, 52)#use this mwthod ,only for get a string certain position refer to the above
>>> QUANTITY = slice(52, 55)
>>> ITEM_TOTAL = slice(55, None)
>>> line_items = invoice.split('\n')[2:]
>>> for item in line_items:
        print(item[UNIT_PRICE], item[DESCRIPTION])
 $17.50 Pimoroni PiBrella
 $4.95 6mm Tactile Switch x20
 $28.00 Panavise Jr. - PV-201
 $34.95 PiTFT Mini Kit 320x240
 '''

 #list slice 
 '''
 Assigning to slices
Mutable sequences can be grafted, excised and otherwise modified in-place using slice
notation on the left side of an assignment statement or as the target of a del statement.
The next few examples give an idea of the power of this notation.
>>> l = list(range(10))
>>> l
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> l[2:5] = [20, 30]
>>> l
[0, 1, 20, 30, 5, 6, 7, 8, 9]
>>> del l[5:7]
>>> l
[0, 1, 20, 30, 5, 8, 9]
>>> l[3::2] = [11, 22]
>>> l
[0, 1, 20, 11, 5, 22, 9]
>>> l[2:5] = 100
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
>>> l[2:5] = [100]
>>> l
[0, 1, 100, 22, 9]
When the target of the assignment is a slice, the right-hand side must be an
iterable object, even if it has just one item
 '''