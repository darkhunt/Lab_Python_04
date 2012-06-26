g = ['banana','strawberries','apples','bread' ]
g.append('champagne')
print g
g.remove('bread')
print g
g.sort()
print g

#question 2
#i would do dictionary as my data structure because it becomes easier to search a
#grocery


h={'apples':7.3,'bananas':5.5,'bread':1.0,'carrots':10.0,'champagne':20.90,'strawberries':32.6}
print h

#the price of strawberries goes upin the winter to 63.43

h['strawberries']=63.43
print h


#adding price of 6.5 to data structure

h['chicken']=6.5
print h

#question 3
#(a)i will use the list structure since it helps in indexing various items to be
#located very easily

#(b).
in_stock=h.keys()
print in_stock

#(c)coverting data to tuple
always_in_stock=tuple(in_stock)
print always_in_stock

#D
#advertisement needs to run
print"come to shoprite! we always sell:"
for t in always_in_stock:
    print t
    
#question 4
#(a).
    

