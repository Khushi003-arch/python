'''
tuples are inmutable sequence of values or  data type that can not be add , remove .delete just like strings
there are generally fats in compare to list 
use ()
we must add to mote then two elements it we want to create a tuple only one item in  () is not a list


'''

my_tuple=('mon','tues','wed' ,'thues','fri','sat','sunday')

print("my first Tuple",my_tuple)
print(type(my_tuple))

tup1=(1)
print(type(tup1))   # this is not tuple for our python but this is int

tup2=(1,)
print(type(tup2))

tup=()
print(type(tup))



# slicing

print("slicing",my_tuple[0:3])


# methods :

# index() return the index numbers of the mentioned items in parameter on first occurrence.
print("index",my_tuple.index('sunday'))


# methods :

# count() return the total occuerence of the items mentioned items in parameter 
print("count",my_tuple.count('sunday'))




# ============================  practice questions ================================


# empty_list=[]

# for i in range(0 ,3):
#     user_input=input("Enter Your MOvie Name :")
#     empty_list.append(user_input)

# print(empty_list)




# Task 2.

palindrom_list=['abc','efe','khushi','123','roshni']

for i in palindrom_list:
    if i==i[::-1] :
        print(i,"is palindrome")
    else :
        print(i,"is not palindrome")



# Task 3.

tuple=('a','c','a','b','b','v','p')
print("Count",tuple.count('b'))

list=['a','c','a','b','b','v','p']
list.sort(reverse=True)
print(list)


