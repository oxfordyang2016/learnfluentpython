import collections
# this is in order to make a quick class,database record can use the model.
#you can verify it via Card('7','diamonds')
# or,you can use C = collections.namedtuple('Dard', ['rank', 'suit'])
#d=C('7','d')
#print(d) will print  Dard(rank='7', suit='d')
#you can refer to http://book.pythontips.com/en/latest/collections.html
#about doctest ,you can use http://pythontesting.net/framework/doctest/doctest-introduction/#example
# from now 's experience ,doctest in .py file ,you can only place in function,but in separte file you
#not need manage ,in seprate file,i can konow only >>> do make effect
#but i find ,in a separate file,your test get more simple
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
	#about the following var,what i want to say is i donot undestand .
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    #this will produce a list split by space ,['spades', 'diamonds', 'clubs', 'hearts']
    suits = 'spades diamonds clubs hearts'.split()
    '''
    about the list comprehension .it will produce a list,that is ,for example
    [a+b for a in range(2) for b in range(3)] 
    Out[67]: [0, 1, 2, 1, 2, 3]
    it is a nested loop  when you len(the above list) it will be 6
    ''' 
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    '''
    when you implemment a __len__ method in a instance ,you can use a len(instance)
    for example,a=FrenchDeck(),you can use len(a)
    '''
    def __len__(self):
        return len(self._cards)
    # this is used to implement the list[positon],a[3]
 
    def __getitem__(self, position):
        '''
        >>> deck = FrenchDeck()
        >>> len(deck)
        52
        
        '''
        return self._cards[position]


def testfunction():
    '''
    #this is a test you must note test position
    >>> deck = FrenchDeck()
    >>> len(deck)
    52
    '''
    print('hello')
    def spades_high(card):
        '''
        >>> spades_high(Card('2', 'clubs'))
        0
        >>> spades_high(Card('A', 'spades'))
        51
        >>> a=[1,2,3,4,5,6]
        >>> print(a.index(6))
        5
        >>> print(dict(spades=3, hearts=2, diamonds=1, clubs=0))
        {'spades': 3, 'clubs': 0, 'diamonds': 1, 'hearts': 2}
        '''
        #it used to get card.rank,eg(2,3,4,5,6....A)
        suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)#it will get  a dict
        rank_value = FrenchDeck.ranks.index(card.rank)# this is order to get index of value
        # will use
        return rank_value * len(suit_values) + suit_values[card.suit]
        #index*




'''
how to get list value's index
a=[1,2,3,4,5,6]
a.index(1)

when get len(dictionary),you will gety lenth of 
dictioarty,it will equeal to the number of keys
In [160]: print(dict(spades=3, hearts=2, diamonds=1, clubs=0))
{'spades': 3, 'clubs': 0, 'diamonds': 1, 'hearts': 2}
In [161]: a=dict(spades=3, hearts=2, diamonds=1, clubs=0)
In [162]: len(a)
Out[162]: 4


'''