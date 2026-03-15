# list is like array which store multiple values in single variable in []

'''

always flow willb be from left to right direction. ----->
but if we mentaion -1 like this [-3:-2:-1]  then direction will be the 
change right to left oreder <--------

'''

# List = Ordered collection of items means a container that can store multiple values.


'''
MIMP Things about List 

1.list can store values of any data type.
2.ordered
3.mutable(we Can Change The Value.)
4.it also store duplicate values.
5.if index is not include in list then this will give error "OUT OF RANGE"

note :

list function are return nothing means return none.
and :
string function are return updated strings .

'''


numbers=[10,20,30,40,50,60]
print("list", numbers)
print(type(numbers))
print(len(numbers))
print(numbers[5])


students=['khushi',20/11/2004,'surat',7.08]
print(students)

# mutable

print(students[0])
students[0]='khushali'
print("Mutable",students[0])

# print("out of range",students[5])




# slicing :
'''
in slice [] use : colon not , comma .
last index should not be include .
always flow willb be from left to right direction. ----->
but if we mentaion -1 like this [-3:-2:-1]  then direction will be the 
change right to left oreder <--------




syntax.

list_name[start index : last index]

'''


numbers=[10,20,30,40,50,60]
print("Slicing",numbers[0:3])
print("Slicing",numbers[:3])         # here starting index is missing out 
print("Slicing",numbers[0:])         # here last  index is missing out 
# in the above case the last index is len(numbers)
print('negative indexing:',numbers[-1:-3:-1])





# indexing 

'''
indexing always start with 0

'''

print("Index",numbers[2])



'''

================================== job related methods ================================

'''


# append()

'''
We can add items in list 
it can add only one items

'''

fruits=['apple','banana','gavava','cherry']
print(fruits)
fruits.append('Mango')
print("append",fruits)




# remove()

'''
it can remove the value from the list  .
it can remove only single values .

'''

car=['BMW','Thar','toyoto']
car.remove('toyoto')
print("remove ",car)




# len()  -- define the length .

'''
it can count the items in the list with space also .
'''

marks=[10,20,30]
print("length of marks ",len(marks))


# methods :

list=[2,1,3]
list.append(4)    #add one  items in the last 
print(list)


# methods :

list.sort()   # this function return NONE 
print("short",list)
list.sort(reverse=True)
print("Des",list)

fruits=['abc','def','acb','aac']
fruits.sort()
print(fruits)


# methods :

alphabet=['a','b','c','d','e']
alphabet.reverse()
print(alphabet)
alphabet.sort(reverse=True)
print(alphabet)


nums = [3, 1, 4, 1,2]
nums.reverse()
print("reverse the list",nums)   # [2, 4, 1, 3]

nums.sort(reverse=True)
print("sort in descending order   " ,nums)   # [4, 3, 2, 1]


# methods :

nums.insert(4,5)
print("insert method ",nums)



# methods :

nums.remove(1)
print("after remove",nums)    #remove element on first occurence 


nums.pop(0)
print("remove using pop",nums)

