"""
19.04.11
onurcan koken
check: https://docs.python.org/2/tutorial/datastructures.html
"""

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

print(listA.sort()) # none
print(listA) # sorted listA
print(listA.insert(0, 100)) # insert 100 to 0th index, return none
print(listA)
listA.remove(3) # remove 3th index element
print(listA)
listA.append(7) # insert '7' to the end of the list
print(listA)
print(listA + listB)
listB.sort()
print(listB)
listB.pop() # remove the last element of the list
print(listB.count('a')) # returns number of 'a'
print(listB)
listA.extend([4, 1, 6, 3, 4]) # add these elements
print(listA)
listA.count(4)
print(listA.index(4))
listA.pop(4)
print(listA)
listA.reverse()
print(listA)