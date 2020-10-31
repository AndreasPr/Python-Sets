# Sets is a collection data type, unordered, mutable, no duplicates

myset1 = {1,2,3,6,7,2,1}
print (myset1)

myset2 = set([1,2,3])
print(myset2) #{1, 2, 3}

myset3 = set("Hello")
print(myset3) #{'e', 'H', 'o', 'l'}

#--------------------------------------------------Empty Set (I CANNOT TO DO THIS: myset4={} because the type is dictionary)------------------------
myset4 = set()
print(type(myset4)) #<class 'set'>

#---------------------------------------------------Mutable: add, remove, discard, pop, clear elements--------------------------------------
myset5 = set()

myset5.add(1)
myset5.add(2)
myset5.add(3)

myset5.remove(3)  #If the element does not exist, then we have an Exception 
myset5.discard(4) #If the element does not exist, then we don't have any exception

#   myset5.clear() That clear our Set
#   myset5.pop() #Remove an element arbitrary

print(myset5)

#-----------------------------------------------------Iterate in Set----------------------------------------
myset6 = set()
myset6.add(3)
myset6.add(6)
myset6.add(2)

for i in myset6:
    print(i)

if 1 in myset6:
    print("Yes")

#------------------------------------------------Union & Intersection--------------------------------
odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

# Unions combines elements from two Sets without duplicates
u = odds.union(evens)
print(u) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#Intersections take the elements that exist in both Sets
i = odds.intersection(primes)
print(i) # {3, 5, 7}

#------------------------------Difference, symmetric_difference, update, intersection_update, difference_update, symmetric_difference_update--------------------------------------
set1 = {1,2,3,4,5,6,7,8,9}
set2 = {1,2,3,10,11,12}

# ----difference: Return the elements of the first Set that are not in the second Set
diff = set1.difference(set2)
print(diff) # {4, 5, 6, 7, 8, 9}

# ----symmetric_difference: Return all the elements from set A & B, but not the elements that are on both Sets
diff_sym = set1.symmetric_difference(set2)
print(diff_sym) # {4, 5, 6, 7, 8, 9, 10, 11, 12}

# -----update (for inplace changes)
set1.update(set2)
print(set1) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

#------intersection_update (for inplace changes)
set3 = {1,2,3,4,5,6,7,8,9}
set4 = {1,2,3,10,11,12}

set3.intersection_update(set4)
print(set3) #{1, 2, 3}

#--------difference_update (for inplace changes)
set5 = {1,2,3,4,5,6,7,8,9}
set6 = {1,2,3,10,11,12}

set5.difference_update(set6)
print(set5) # {4, 5, 6, 7, 8, 9}

# -------symmetric_difference_update (for inplace changes)
set7 = {1,2,3,4,5,6,7,8,9}
set8 = {1,2,3,10,11,12}

set7.symmetric_difference_update(set8)
print(set7) #{4, 5, 6, 7, 8, 9, 10, 11, 12}

#-----------------------------------------------Subset-----------------------------
set9 = {1,2,3,4,5,6}
set10 = {1,2,3}

print(set9.issubset(set10)) #False
print(set10.issubset(set9)) #True

# ----superset
print(set10.issuperset(set9)) #False because set10 does not contain all the elements of the set9 

#----isdisjoint
print(set9.isdisjoint(set10)) #False because they have common elements
set11 = {7,8}
print(set9.isdisjoint(set11)) #True because they dont have any common elements

#----------------------------------------------------Copying in Sets----------------------------------------
setA = {1,2,3,4,5}
setB = setA

setB.add(8)
print(setB) #{1, 2, 3, 4, 5, 8}
print(setA) #{1, 2, 3, 4, 5, 8}

# In order to make an ACTUAL COPY you have to use copy() OR set() method
setC = {1,2,3,4,5}
setD = setA.copy()

setD.add(8)
print(setD) #{1, 2, 3, 4, 5, 8}
print(setC) #{1, 2, 3, 4, 5}

#----------------------------------Frozen Set---------------------------------------
a = frozenset([1,2,3,4]) #It is immutable the specific set, so if I add, remove, use update methods, it throws an exception. 
# It works in unions, intersections and difference
print(a) #frozenset({1, 2, 3, 4})