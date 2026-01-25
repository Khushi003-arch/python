'''

1.List is sequence data type :
2.List is dyanamic Array means on go you can add anything .
3.List is hectrogeneous  not homogeneous .
4.hectrogenius means you can add any type of data in list .
5.slow process then array because it has  slow execution in 
compare to array this is Drawback of list.




'''



L=[1,2,3]
print(id(L))
print(id(L[0]))
print(id(L[1]))
print(id(L[2]))

# Now check the memory address again.

print(":",id(1))
print(":",id(2))
print(":",id(3))

'''

-------------------------- characteristics -----------------

1. ordred 
2.mutable
3.hectrogeneous
4.can have duplicates.
5.can be nested.
6.item can be accessed.
7.can contain any type of object in python.

'''


# create an empty list
print([])

# create an 1D  list and also it is homogeneous.
print("1D list and homogeneous.",[1,2,3])

# create an 2D or you can say nested list 
print("nested list and hectrogeneous",[1,2,3,[1,2]])

# create an 3D list .
print([[[1,2],[1,2],[1,2]]])  
# now it is homogeneous. because of this list is contain same type of data and that is list.


# create an hectrogeneous list .
print(['number','string','boolean',1,{}])


# using type conversion
print(list('khushi'))


#----------------------------- accessing items from a list ----------------------
# 1.indexing
# 2.slicing

# positive indexing.
# negative indexing.

l=[1,2,'khushi',[-1,2],]   # hectrogeneous.

print("positive indexing start from 0 in left to right order :",l[0])
print("negative indexing start from -1 in right to left order :",l[-1])
print("in 2D",l[-1][-2])


Three_D_list=[[[1,2],[3,4],[5,6]]]
print("Accessing 3D elements.",Three_D_list[0][1])
print("Accessing 3D elements.",Three_D_list[0][2][0])
print("Accessing 3D elements.",Three_D_list[-1][-1][-2])


# slicing in list
# syntax:[start:end:step]
# to pick or get some part of list by mentioning the startIndex:lastIndex 


list=[1,2,3,4,5,6,7,8,9,10]
print(list[0:1])
print(list[0::3])
print(list[-1:-4:-1])
print(list[-1:-10:-3])
print(list[0:5:2])
print(list[-6:-1:2])
print(list[::-1])





# -------------------------------- adding items in the list --------------------



# 1.insert(index,item)  ----insert elemnets at specific position. it take two arguments.
# 2.append()  ----add elements at last index.
# 3.expand()  ----add multiple items at once.





fruits=['apple','mango','guava']
fruits.insert(2,'banana')
print(fruits)

fruits.append('banana')
print(fruits)

fruits.extend(['fruits1,fruits2'])
print(fruits)





# ------------------------------- editing items in list -----------------------

# 1.indexing
# 2.slicing

list=[1,2,3,4,5]

# indexing:
list[4]=500
print(list)


# slicing:
list[2:4]=[300,400,500]
print(list)




# ---------------------------- deletion in list ----------------------------

'''
del keyword  ----- delete the whole list and also by index
pop()        ----- delete items by indexing
remove()     ----- delete by value at first occurrence
clear()      ----- create an empty list.

'''


L=[1,2,3,4,5,1,2,3,4,5]

L.remove(5)
print(L)

L.pop()
print(L)


# del L    # this will delete whole list  but not at memory level
del L[0]  #this will delete by indexing.
print(L)


L.clear()
print(L)


L=[1,2,3]
L.pop(1)
print(L)







# ---------------------------- operations on list ---------------------------

'''
1. Arithmetic  .
2. membership  .
3. Loop .


'''


# Arithmetic.

l1=[1,2,3,4]
l2=[5,6,7,8]

print(l1 + l2)   #concat the list.
print(l1*3)      #repeat the whole list three times.


# Membership operator.


l1=[1,2,3,4,[5,6]]
print(5 not in l1)
print(5 in l1)
print([5,6] in l1)




# Loop

l1=[[[1,2,3],[1,2,3],[1,2,3,4]]]
for i in l1:
    print(i)


l2=[5,6,7,8]
for i in l2:
    print(i)




# ---------------------------------- function in list ---------------------------

# len/min/max/sorted (this are universal function:)

num=[1,5,8,7,100,512,0]

print("length",len(num))
print("minimum",min(num))
print("Maximum",max(num))

# sorted function return in ascending order descending order.

print("Ascending order:",sorted(num))

# if you want to print it in descending order. then give second hidden arguments 
# reverse = True
print("Descending order",sorted(num,reverse="True"))




# count


num=[1,5,8,7,100,512,0,100]
print("Count",num.count(100))



# copy
# reverse
# index