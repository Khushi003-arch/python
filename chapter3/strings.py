'''

what is strings :
strings are the sequence of the character :
and also a primitive data type :
strings are inmutable.
strings are enclosed with single and double and tripple quotes also .''," ",''' '''

'''


# why we use this three enclosed method : for example :

# "this is khushi's chapter3"  

str1="khushi"
str2='khushi'
str='''khushi'''




demoStr='this is string .\n i am creating the string in python language.'
print(demoStr)
# here i want move this above string in second line start with . i 


# so for that we are use the escape 
'''
1.\n :------------> for new line 
2.\t :------------> for tab space
3.\" :------------> for double quotes
4. \\ :-----------> for backclash 


'''



# =================================== Basic Operations of string ================================



# 1. concatenation

char1="welcome"
char2="new user"
finalchar=char1 + char2
print(finalchar)



# ===============================================================================



# 2. length of string

# syntax:
# len(string_name)
# it also count white space :

print("length of char1",len(char1))
print("length of char2",len(char2))



# =================================================================================






# 3. indexing

# indexing : indexing means to assign a position to each element 
# indexing start with 0 numbers 
# negative indexing start with -1 numbers (always start in reverse order:)
# positive indexing also increase:
# negative indexing always descrese


name="khushi vishwakarma"
    # 012345678901234567

char=name[0]
print("character position :", char)    

print("last position :",name[-2])

fruit='apple'
print("Negative indexing:",fruit[-5:-2])




# ==================================================================================




# 4. slicing():
# accessing parts of strings :
# if we forget to define last index number then python automatically understand that 
# user want to go at last position

# synatx:
# variable_Name(start_index:last_index)        last index does not include in output.

print("slicing example :",name[0:7])
print("slicing example :",name[7:])
print("slicing example :",name[7:len(name)])






# ==================================================================================




# 5.startWith() / endsWith()
# syntax:
# variable_name.function()



# file=input("Enter a fileName:")
# if file.endswith(".py"):
#     print("These is Python file. ")
# else:
#     print("Not Python File.")



newUser='surat user'
print("Start with :",newUser.startswith('surat'))




# ===================================================================================



# str.capitalize() 
# this function capitalize only 1 (first) character
# str.title()
# this function capitalize all first character of each words.
# it return new string and does not change the original string .

print("Capitalize Example:", fruit.capitalize())
fruit2='apple banana mango'
print("capitalize Example:",fruit2.title())



# ===================================================================================

# 5.replace()
# replace only first occurence .

string="i am old "
print(string.replace('old','new'))

str="i am learning javascript from apna college and javascritp is also most populatr"
print(str.replace('javascript','python'))


# ===============================================================================



# 6.find()
# return index of first occurence or -1
# 

print("find() Example",string.find('old')) 






# ==================================================================================

# 7.count()
# count() return  total number of matching words in whole string.

str='if you want to happy then think like you are happy and you always happy and all things are happy.'
print("Count() Example", str.count('happy'))





#----------------------------- PRACTICE QUESTIONS:--------------------------------



# WAP to input user first name and print its length.


userName=input("Enter User Name :")
print(len(userName))


# WAP to count occurrence of $ symbol.


str="hii $ i am $ symbol $99.99 "
print(str.count('$'))




# Try ye programs:

# 1️⃣ Check string empty hai ya nahi
# 2️⃣ Count vowels in a string
# 3️⃣ Check palindrome string
# 4️⃣ Password validation program
# 5️⃣ Check email contains @ and .


# Check string empty hai ya nahi

s1=input("Enter A string:")
if s1=="":
    print("String is empty:")
else:
    print("String is not Empty:")

        
#  Check email contains @ and .



email=input("Enter A Email:")
if '@' in email and '.' in email:
    print("This Email is Valid:")
else:
    print("This Email is not valid:")



# Password validation program

password=input("Enter A Password:")

if len(password)<8:
    print("Password too Short:")
elif not any(ch.isdigit() for ch in password):
    print("Password must be contain At least one digit:")
else:
    print("password is Valid:")