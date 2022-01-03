#Sets in python



fruits = {"apple","banana","phinaple","papaya","lemon"}
items = {1,"Keyboard","Laser"}

#This add an item to the set
fruits.add("cherry")
print(fruits)

fruits.remove("apple")
print(fruits)

"""This method remove a item from the set and 
if not exist it doesnt return and error like remove"""
fruits.discard("phinaple") 
print(fruits)

#This method remove one item of the set
fruits.pop()
print(fruits)

"""Sets are unordered, so when using the pop() 
method, you do not know which item will remove."""

#This both method exclude any duplicate items
fruits.union(items)
fruits.update(items)
print(fruits)


# #This method keep only the items that are in both sets
# fruits.intersection_update(items) 
# print(fruits)

# #This is like intersection_update() but it return a new set with the values
# fruits.intersection(items)
# print(fruits)


#this method will keep only the elements that are NOT present in both sets.
fruits.symmetric_difference_update(items)
print(fruits)

#method will return a new set, that contains only the elements that are NOT present in both sets.
fruits.symmetric_difference(items)
print(fruits)


#This method return True if all items in set fruits are present in set items
response = fruits.issubset(items)
print(response)

products_1 = {"Phone","Tv"}
products_2 = {"Tv","Pc"}

#this find an intersection or match between one or more sets
print(products_1.intersection(products_2))


# add()	                           Adds an element to the set
# clear()	                       Removes all the elements from the set
# copy()	                       Returns a copy of the set
# difference()	                   Returns a set containing the difference between two or more sets
# difference_update()	           Removes the items in this set that are also included in another, specified set
# discard()	                       Remove the specified item
# intersection()	               Returns a set, that is the intersection of two other sets
# intersection_update()	           Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	                   Returns whether two sets have a intersection or not
# issubset()	                   Returns whether another set contains this set or not
# issuperset()	                   Returns whether this set contains another set or not
# pop()	                           Removes an element from the set
# remove()	                       Removes the specified element
# symmetric_difference()	       Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	   inserts the symmetric differences from this set and another
# union()	                       Return a set containing the union of sets
# update()	                       Update the set with the union of this set and others


set_1 = {"cantar","correr","jugar"}
set_2 = {"saltar","jugar","cantar"}
set_3 = {"jugar","cantar","pintar"}
set_4 = {"cantar","jugar","programar"}

set_list = [set_2,set_3,set_4]
match_list = []

for s in set_list:
    if set_1.intersection(s):
        match_list.append(s)

print(match_list)

    