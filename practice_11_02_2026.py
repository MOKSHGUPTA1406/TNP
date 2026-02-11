# Date: 11-02-2026

# 1. WAP to store your age and print it.

age=int(input("Enter your age: "))
print("Your age is:", age)

# 2. Create two variables a=10 abd b=20. swap the values of a and b without using a third variable.

a=10
b=20
print("Before swapping: a =", a, "b =", b)
a=a+b
b=a-b
a=a-b
# or a,b=b,a
print("After swapping: a =", a, "b =", b)

# 3. Take two numbers as input from the user and print their sum, difference, product and division.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Sum:", num1+num2)
print("Difference:", num1-num2)
print("Product:", num1*num2)
print("Division:", num1/num2)

# 4. Take a number as input from the user and check if it is even or odd.
num=int(input("Enter a number: "))
if num%2==0:
    print(num, "is even.") 
else:
    print(num, "is odd.")
    
# 5. Take three numbers as input from the user and find the largest among them.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1>num2 and num1>num3:
    print(num1, "is the largest.")
elif num2>num1 and num2>num3:
    print(num2, "is the largest.")
else:
    print(num3, "is the largest.")

# 6. calculate a user's age by taking their birth year as input and then use current operator to subtract the birth year from the current year.
birth_year=int(input("Enter your birth year: "))
current_year=2026
age=current_year-birth_year
print("Your age is:", age)