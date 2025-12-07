
# now variable means what a name that strore in memory location and also 
# known as one kind of box to store some value .
# vari means tha value that can be changed 


# syntax:
# variable name = variable vale 

name="khushi"       #string enclosed with "" or '' quotes.
age=21              #numeric
price=99.9          #float numeric

print("My name is : ",name)
print("My Age is  :",age)
print("Total Amount is",price)


age2=age    #here print 21 becuase of 21 is store At memory location of age and age is store in age2 memory location:
print(age)


# RULES FOR THE IDENTIFIERS(indentifiers means variable name :)

# variable name start with small and capital letters  ,and underscore.
# can not start with digit and we can not use special symbol in our indentifiers name :
# VARIABLE name should be simple , short and meaning full and simple to understand .
# variable names are case sensitive.
# keyword are never use as variable name.



# NOW I WANT TO KNOW THAT AT WHICH LOCATION THIS VARIABLE IS STRORED IT MEANS  I want to know thw
# memory location :

# FOR THAT USE id() function .

print(id(name))
print(id(age))      # here memory location is same 
print(id(price))
print(id(age2))    #with this location because both are present in one location :
