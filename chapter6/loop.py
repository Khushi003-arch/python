'''
Loops in Python are used to repeat actions efficiently. 
The main types are For loops (counting through items) and While loops (based on conditions).

variables in loop are also called iterator and 
when loop complete its called iterations

syntax:

while condition :
    #some work 

for item in range :
    #some work


Break Keyword :used to terminate the loop means go outside the loop.
continue keyword :used to iterate the currrent item only


 1. break keyword

👉 Meaning: “Stop the loop completely”


2. continue keyword

👉 Meaning: “Skip this iteration and move to next”




For loop :

for loops are generaly used for sequential traversal .for traversing list string and tuples.
for with else 
but now questions is why we need this else so when we want that for
lopp completety execute tilll its completion in that case we use this else keywprd

but when we use break and continue kewword in that case else is mendatory to use 


===================== range ()
 
renge functuion return a sequence of numbers , staring from o and increment by 1 and stop before a specified numbers

range( start ,stop ,step )





Python में pass statement एक placeholder होता है जो कुछ नहीं करता, 
लेकिन code को syntactically valid बनाए रखता है। इसका इस्तेमाल तब होता है 
जब हमें block (जैसे function, loop, class, या if statement) लिखना है लेकिन 
अभी logic नहीं डालना चाहते।






'''

# count = 1
# while count <= 1115:
#     print("numbers are ",count)
#     count+=1





# practice questions :

# num=100

# while num >= 1:
#         print("num is",num)
#         num-=1





# practice 

# input=int(input("Enter Your Desire Number"))

# i=1
# while i<=10:
#     print(input*i)
#     i=i+1
 


# nums=[1,4,9,16,25,36,49,64,81,100]

# i=1


# while i <=10:
#     print(i*i)
#     i+=1
    



# we traverse on each element of list.

# names=['khushi','diya','roshni','priya','mina']

# index=0
# while index<len(names):
#     print(names[index])
#     index+=1







# task :


# nums=(1,4,9,2,4,5,7,8)
# x=7

# i=0
# while i <len(nums):
#     if nums[i]==x:

#         print("found at",i)
#     i=i+1







# task:

# nums=[1,4,9,16,25,36,49,64,81,100]
# i=0
# while i<len(nums):
    
#     print(nums[i])
#     if nums[i]==25:
        
#         break
#     i=i+1


# task


# i=0
# while i<len(nums):
#     if nums[i]==9 :
#         i=i+1
#         continue
#     print(nums[i])
#     i=i+1





# task
# i=1
# while i<=10:
#     if (i%2!=0) :
#         i+=1
#         continue
#     print(i)
#     i+=1





    
   
# ======================================== For loop ================================



# list =[1,2,3,4,5]

# for num in list :
#     print (num)
# else :
#     print("End the numbers ")






# for loop with else parts 

# name ='khushi'

# for i in name:
#     if (i=='u'):
#         break
#     print(i)
# else:
#     print("End the String")




# list=[1,2,3,4,5,6,7,8,9]
# for i in list:
#     print(i*i)



# x=7
# for i in list:
#     if(i==x):
#         print("found at",i)
#         print("found the values is ",list[i])
        
    
# ====================== range() ======================

# seq =range(0,5)
# for i in seq :
#     print(i)



# for i in range(10):
#     print(i)

# for i in range(5,10):
#     print(i)


# for i in range(5,10,2):
#     print(i)   





# n=int(input("Enter A number :"))

# for i in range(1,12):
#     print(n*i)





# =============================== pass statment =================================
'''

Python में pass statement एक placeholder होता है जो कुछ नहीं करता, 
लेकिन code को syntactically valid बनाए रखता है। इसका इस्तेमाल तब होता है 
जब हमें block (जैसे function, loop, class, या if statement) लिखना है लेकिन 
अभी logic नहीं डालना चाहते।

'''


for i in range(1,5):
    # print(i)
    pass
print("pass as placeholder")





# task :


# sum of n numbers :

