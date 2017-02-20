import collections
# this is in order to make a quick class,database record can use the model.
#you can verify it via Card('7','diamonds')
# or,you can use C = collections.namedtuple('Dard', ['rank', 'suit'])
#d=C('7','d')
#print(d) will print  Dard(rank='7', suit='d')
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
    '''
    >>> deck = FrenchDeck()
    >>> len(deck)
    52
    >>> deck[:3]
    [Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
    '''
    def __getitem__(self, position):
        return self._cards[position]




