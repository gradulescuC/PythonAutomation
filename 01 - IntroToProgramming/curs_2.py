"""

Lists

A list is an ordered and mutable Python container
To create a list, the elements are placed inside square brackets ([]), separated by commas.
"""

print("THE FOLLOWING ARE THE RESULTS FOR THE LIST EXERCISES: ")
print()
a = [1, 2, 3]  # Defining a new list containing numbers. Unlike with variables, lists can be defined without assigning values to them. ex: myList = []
b = ['banane', 'mere', 'gutui'] # we can also define a list containing only text
c = [4, 'struguri', True] # or define a list containing various types of data

print("Here we display each list individually:")
print(f"The first list is:  {a}")
print(f"The second list is  {b}")
print(f"The third list is:  {c}")

print("But we can also print all the lists at the same time:")
print(f"The lists are: {a, b, c}")

print("Each element in a list can be found at a certain index. In any list, the first element can be found at index 0")
print("In the following statements we print on the screen the first element in each list individually, then all at the same time")
print(f"The first element in list a is : {a[0]}")
print(f"The first element in list b is : {b[0]}")
print(f"The first element in list c is : {c[0]}")
print(f"The first element in each list a is: {a[0]} in list a, {b[0]} in list b and {c[0]} in list c")

print(f"The last character in each list is: {a[-1]} in list a,  {b[-1]} in list b and {c[-1]} in list c")
print("Here we displayed the character at index 2 -  the third element in the list which happened to be the last also: ", a[2], b[2], c[2])
# print(a[3])  # It will return error: IndexError: list index out of range because the element at index 3 does not exist
                            # (the third element in the list is at index 2)
                            # in this case the execution will stop and the rest of the instructions will not be executed
                            # The same thing will be available when the automated tests will run
print("The first two elements in list a are: ", a[0:2])  # Here we applied slicing technique
print("The elements in list a are: ", a[0:3])  # It displays all the elements in the list. It doesn't return error if we apply a number larger than the size of the list
                                                # it is not recommended to hardcode the size of the list, since it can increase at some point and lose data
                                                    # In this case we can use the len method as below (checkout curs_1 for more details about len function)
print("The elements in list a are: ", a[0:len(a)])  # displays all elements in a list through slicing as above,
                                                        # but it is a much better option because we do not hardcode the length of the list
print(b.count("mere"))  # the count function displays how many of the elements specified between paranthesis exist in the list
c[-1] = "Portocale"  # Here we modify one single element in the list (the last one), so the value TRUE will be replaced with the value (PORTOCALE)
print(c)

print(sum(a))  # calculates the sum of all the elements inside of list a. It works only with numeric data types, otherwise it returns error: TypeError: unsupported operand type(s) for +: 'int' and 'str'
# a = [1, 2, 3,'test']
# print(sum(a)) # This will return the error specified at line 44, because we cannot sum an int with a string

a.clear()
print(f"The list a now has no value, so it will only display the square brackets: {a}")

print("Here we add a new element to list a called 'banane': ")
a.append("banane")
print(a)

print("Here we add a new element to list a called '3': ")
a.append(3)  # Se pot adauga mai multe elemente cu flow control, intr-un curs viitor
print(a)
print() # this way we can print an empty row so we can see the results better
print("Now we check if the number 3 exists in list a. It can return TRUE or FALSE: ")
print(3 in a)

print()
print()
print()


"""
Tuples

Tuples are a collection of values separated by comma and enclosed in parenthesis. 
Unlike lists, tuples are immutable. The immutability can be considered as the identifying feature of tuples
Each element of a typle is placed at a certain position, starting with index 0
You can't add elements to a tuple because of their immutable property. There's no append() or extend() method for tuples.
You also can't remove elements from a tuple because of their immutability.
"""

print("THE FOLLOWING ARE THE RESULTS FOR THE TUPLES EXERCISES: ")
print()

print("Declaring and initializing a tuple. Same as lists, tuples can be created without assigning values to them. Example: myTuple = ()")
myTuple = (1, 2, 5, 7, 5)
print(myTuple)
print(f"We print here the element at index 3, which is 7: {myTuple[3]}")
# print(myTuple[5])  -> This will return error: IndexError: tuple index out of range because we try to access an element that does not exist

print("Check how many elements do we have in the tuple. We can use the len function just as with lists: ")
print(len(myTuple))

print("Check if the number 5 exists in the tuple. Return TRUE or FALSE: ")
print(5 in myTuple)

print("Just as with lists, we can check how many times an element appears in the tuple")
print(myTuple.count(5))


# myTuple[0] = 8  -> This will return error TypeError: 'tuple' object does not support item assignment - because a tuple is an immutable data type

tup = 2, 3, 4 # the tuple can also be defined like this, because by default a succession of numbers assigned to a memory space will be treated as a tuple
print(type(tup))  # you can check the above with the type function to see what is the data type that was assgined to 'tup'

"""
Sets
Sets are a collection of unorganized data with unique elements separated by coma and included inside brackets
Just as with lists and tuples, we can define an empty set. Example: mySet = {}
Set items are unchangeable, but you can remove and/or add items whenever you like.

"""
print("Here is a set containing 4 elements: ")
mySet = {13, 5, 67, 5} # Here we defined a set with four elements
print(mySet)

print("We can add elements to a set with the help of add function")
mySet.add(7);
mySet.add(7.5);
mySet.add(9);
print(mySet)
# print(mySet[0]) -> Returns error: TypeError: 'set' object is not subscriptable
                        # because sets are unordered, therefore the concept of index does not exist in a set
print("We can also transform a list in a set: ")

print("a) Define the list: ")
myList = [13, 5, 67, 5]
print(myList)

print("b) Convert the list into a set")
print(set(myList))

print("We can also do multiple conversions (although there is no applicability for this): ")
print(list(set(myList)))

"""

Dictionaries

Dictionaries are unordered and changeable collections of data which store key:value pairs of data
Dictionaries do not allow duplicated keys
As of Python version 3.7, dictionaries are ordered
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.


"""

print("There are two ways of defining a dictionary: ")
print("a) By in-line defining of key:value pairs")
myDict1 = dict(a=1, b="Bella Ciao")
print(myDict1)

print("b) Through standard dictionary sintax")
myDict = {"a": "My data for a",
          "b": "My data for b",
          7: "Python",
          True: [5, 16, 45],
          "c": [dict(a=1, b="Bella"), dict(a=1, b="Ciao"), dict(a=1, b="aloha")]
          } #  As with lists, we can assign multiple types of values to a dictionary
print(myDict)

print("Let's print the first element in the dictionary myDict: ")

print(myDict[1])
# Posibilitati de extragere a unui element dintr-un dictionar:
print(myDict["a"])
print(myDict1["b"])
print(myDict[True][0])
print(myDict["c"][2]["b"])
print(myDict.get(7))

print("Here are some instructions to work with indexed dictionaries as of python 3.7")
from collections import OrderedDict
"""
OrderedDict defines a dictionary that remembers insertion order
    # An inherited dict maps keys to values.
    # The inherited dict provides __getitem__, __len__, __contains__, and get.
"""
d1 = OrderedDict()  #  defines an object of the class OrderedDict()
d1['a'] = 0 # Assign a value to each key in the dictionary
d1['b'] = 1 # Assign a value to each key in the dictionary
d1['c'] = 2 # Assign a value to each key in the dictionary
print("Let's see how our dictionary looks like: ")
print(d1)

print("In order to access the index of a dictionary we will need to create a list of keys from the dictionary and then access a specific key by index")
keys = list(d1.keys())
print(keys[1])
print()
print("We can do the same thing with the values: ")
values = list(d1.values())
print(values[1])
print()
print("And also with an entire item: ")
items = list(d1.items())
print(items[1])


"""
Let's see how we can iterate through the elements of a dictionary (for loop to be covered in depth in future courses)
"""

# k,v = key, value

for k,v  in myDict.items(): # here it will iterate through all the elements (key:value) of the dictionary
    print("Next element in the iteration is: ",  k,v) # before doing any checks, it will print the element that is found
    if k == 7: # Here it checks if the key that was found is '7'
        print(f"Item found. The value for element 7 is :  {v}. ") # if it is 7, it will print on the screen Item found. The value for element 7 is : Python.
    elif k == "c": # If the item is not 7, it will check if the key item is c.
        print (f"Item found. The value for the element c is: {v}.") #If it is it will display on the screen: Item found. The value for the element c is: [{'a': 1, 'b': 'Bella'}, {'a': 1, 'b': 'Ciao'}, {'a': 1, 'b': 'aloha'}].
                                # Basically it will display the value for element c, which is a list of dictionaries, so it will display them
    else: # if the key item is not neither 7 nor c, it will print: Not what we were looking for. Move to the next value
        print("Not what we were looking for. Move to the next value")

# In the above iteration it execute the instructions from line 204 until line 2011 for element "a": "My data for a"
# Then it will execute them again for element "b": "My data for b"
# Then again for element 7: "Python" (and here it will print something because it found a match for the key)
# Then again for element True: [5, 16, 45]
# Then again for element "c": [dict(a=1, b="Bella"), dict(a=1, b="Ciao"), dict(a=1, b="aloha")] (and here it will again print something because it found a match for the key)






