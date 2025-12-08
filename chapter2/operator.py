'''

so operators are the basic symbol that is used to perform some basic operations between the operands

1.Arithmetic operators.  #used to perform mathematical performns.
(LIKE: + ,- ,* ,/ , %, ,etc.)



2.relations operators/Comparison operators
Always return boolean values from the variable TRUE / FALSE.:
(LIKE : ==,!=,<=,>=,>,<)



3.Assignments operator:   (value assign karna and value ko update karne .)
(LIKE: = , += ,-+ ,*= ,/= ,%= ,**=)



4.Logical operator: used with conditional Statement .
(LIKE : And Or Not)
and:both true 
or:any one true
not:reverse (if true return false)


5.identify operators :  (object ki identity check karta hai )
(is , is not) : in simple terms memory location check karta hai 
----------------> if location same  , is operator return true.
----------------> if location dose not same , is not operator return  true.
----------------> to check memory location we use id() function.


6.membership Operators.
(check that is the element is member of list/tuple/string/)
in ------------> return true if value is present in sequence.
not in --------> return true if value is not present in sequence.







'''


# ------------------------------> Arithmetic Operators.

a=2
b=10

print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(a%b)    #used to find reminder
print(a**b)   #for find the power of a of b






# ------------------------------> Relational  Operators. (that return boolean value always.)

a=15
b=10
c=10

print(a==b)     #false
print(a>c)      #true
print(b<c)      #false
print(a!=b)     #true
print(a<=b)     #false
print(a>=b)     #true





# -------------------------> assignment operators :
# (assign value from right side to left side into the variable and also update the vale)




no1=10
print(no1)

# no1=no1+10
no1+=10                        #here we are using the assignment operators and it is +=
print(no1)

# no1=no1-10
no1-=10                        #here we are using the assignment operators and it is +=
print(no1)


print("Number is :",no1)   # here you can notice that Numbers value is updated.



no1%=2
print("Modul is :" ,no1)




# -------------------------------> logical operators:

# Not operators is works on single operand
# And operators is works on two operand
# Or operators is wokrs on two operand

a=10
b=15

print(not False)
print(not (b>a))



value1=False
value2=True

print("And operators",(value1 and value2))
print("Or operators",(a==b) or (value2))



print("And operators is :",(a<b)and (value1))
print("Or operators is :",(a<b)and (value2))



'''
And operators return true when both operands are true.
Or operators return true if any one oprand is true. 

'''



#--------------------------------> identify operators :    

x=10
y=20
z=x


memoryLocation=x is y
memoryLocation2=x is z

# ---------------------------- here i want to print moemory location of all of them.

print("Memory of X variable:",id(x))
print("Memory of y variable:",id(y))
print("Memory of z variable:",id(z))

print("check Memory location :",memoryLocation)
print("Now check Memory location2 :",memoryLocation2)


print("Example of Is not operators :",x is not z)
print("Example of Is not operators :",x is not y)



# -----------------------> membership operator 

list=[10,20,30]
tuple=('mango','banana')
string="python is fun"

print("in operators",10 in list)  #true
print("in operators",10 in tuple)  #false
print("in operators","p" in string) #true


print("not in operatprs" ,"khushi" not in string)   #true
print("not in operators","python" not in string)  # false


dictionary={
    "name":"rahul",
    "age":21,
    "course":"BCA"
}

print("name" in dictionary)
print("rahul" in dictionary)
print("rahul" not in dictionary)    #------------------ in operators only check the key not value
