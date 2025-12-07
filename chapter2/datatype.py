# dataType that is determined by the value assigned to the varibale .
# if i want to know the type of the data 
# use type() function.

# in PYTHON there are 8 mainlly data types.
"""
1.int   (whole numbers without decimal numbers . negative ,positive,zero)
2.float (decimal numbers.)
3.str   (sequence of character.)
4.bool  (True,False)
5.None. (missing value.)


6.list [same like array]  -----> these are changeable 
7.tuple (value,value,value)   -----> these are Unchangeable 
8.dict {key:"value",key:"value"}

"""



name="alias"
print(type(name))

age=21
print(type(age))

money=199.00
print(type(money))

isLoggin=True
print(type(isLoggin))


x=None
print(type(x))


list=['apple','mango','banana']
print(type(list))

tuple=('ramji','sitaji', 'mummy','papa','krishnaji',)
print(type(tuple))

dic={
    "name":"khushi",
    "age":21,
    "course":"BCA"

}

print(type(dic))


# lets try to change the value of list:
print(list[1])
list[1]="changeValue"
print(list[1])

'''
here we observe that list values are changable.
first print mango then i was change the value of list[1] to changeValue
and after that i print the value of it and it is now change.
'''






# now try to change the value of tuples()

print(tuple[1])
# tuple[1]="tupleChange"   here this will throw an error.
# print(tuple[1])     object does not supports the item assignment:
 
import sys



print(sys.getsizeof(list))     # list ka size
print(sys.getsizeof(tuple))     # tuple ka size
print(sys.getsizeof(name))  # string ka size



# NOW WHAT ARE RESERVED KEYWORDS IN PYTHON .

'''
reserved keywords that have specifoc meaning like and class for True false while or etc.
'''



# =================================== Assinment 1.=================================


number1=55
number2=10
sum=number1+number2
print(sum)





# ========================= comments in python ==================================

'''
comments in any program that is not read by our compiler and interpreter 
this comments are written for the programmers and coder to undertsand the code 

1.for one line comment press #
2. for mutltiple line coments use tripple comma '''  '''

in vs code there are short cut to comment out code simultaneously just press 
------> ctrl + /

'''