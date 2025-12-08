'''
to convert a one data type to another 
like int to string 
int to float
list to tuple
and all that.


-----------------------------> now in python there are two type of conversion
1.implicitly conversion.  (Automatically by python interpreter. )
2.explicilty conversion.  (manually by the coders using the buitl in function )

(Like :

1.int(val) ==== convert to int
2.str(val) ==== convert into string
3.float(val)  === convert into float value
4.list(val) ====convert into list
5.tuple(val) ===convert into tuple
6.dict(val) === convert into dictionary 
7.set(val) === create the set by removing the duplicates values.

)





'''

# ------------------------------ implicitly conversion ---------------------


a=10
b=10.20
c=a+b

print(c)
print(type(c))


# here what happens  i dont convert any data type explicitly yet 
# what the python interpreter do ..
# it conver int variable of a into float data type 
# and this is know as implicitly type conversion.





# ----------------------- explicitly conversion (Type Casting . by forse fully)

a=10
b="khushi"

print(str(a)+b)   #str function convert this a variable to string.


string="khushi"
print("convert  string into list:",list(string))
print("convert  string into tuple:",tuple(string))

list = [1, 2, 2, 3]
print(set(list))


str="10.5"

# here now question is what in str also numbers then why should not convert it into numbers.
# first we need to convert it into float

print("type casting first str to float then float to int.",int(float(str)))








# -----------------bool() return true and false

print(bool(False))
print(bool(0))
print(bool(None))
print(bool(True))
print(bool(""))
print(bool("khushi"))











# -------------------------------- truthy / falsy value in python. ---------------

'''

The following value is falsy value and apart from that all values are trated as Truthy value.

1.False
2.0 (no matter it is int ,float and ,complex)
3.None
4.Empty string " "
5.empty list []
6.empty tuple ()
7.empty dictionary {}
8.empty set set()



'''


a=""
print("check false/true:",bool(a))

b=None
print("check false/true:",bool(b))


c="khushi"
print("check false/true:",bool(c))


d=[]
print("check false/true:",bool(d))
