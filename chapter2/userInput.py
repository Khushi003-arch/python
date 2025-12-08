'''
input() function is used to take value using the keyboard from the user .
input() function always return string 


'''


# -------------------- here you can see that input() function used to take input from the user side.



user=input("Please Enter Your Name:")
print("welcome to Dear",user)


# as we know that our python input() function return always string.
# here we are convert input string into int and float also.


age=int(input("Enter Your Age :"))
print("You Entered in" ,age)


price=float(input("Price of Product :"))
print("product Price",price)



'''
practice Question:

1.write a program to input 2 numbers and print their sum:

'''

number1=int(input("Enter a Number1: "))
number2=int(input("Enter a Number2: "))
sum=number1+number2
print("Total of Two Numbers :",sum)





'''
practice Question:

1.write a program to print area of square.:
2.Area of Sequare : side * side

'''


side=float(input("Enter side of sequare"))
area=side*side
print("Area of Sequare is : ",area)



'''
practice Question:

1.write a program to print average.:
2.Average = sum of value / 2  like (a+b)/2


'''
first = float(input("Enter first value: "))
second = float(input("Enter second value: "))

print("Average of two values ",(first+second)/2)


# print true if first is grater then second


print(first > second)


