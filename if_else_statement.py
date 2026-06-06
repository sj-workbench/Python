money = int(input("Enter you salary in lpa: "))
if money>=5 and money<10:  # conditon 
    print("Ok ok")

elif money >= 10 and money <=100:  # another condition and can be used as many times someone wants
    print("Ultra Rich")

else: 
    print("Poor")    


# Without else
cash = int(input("Money recieved: "))
if cash==10:
    print("I will have Chocolate")
elif cash ==50:
    print("I will have Chips")
elif cash == 100:
    print("I will have chicken roll")

# Comparison
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
if num1>num2:
    print("Num1 is bigger")
elif num1==num2:
    print("Both are equal")
else:
    print("Num2 is bigger")

# even odd
num = int(input("Enter a number: "))
if (num%2)==0:
    print("number is even")
else:
    print("number is odd")

# Voting
name = input("Tell me your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"Hello {name} youre eligible to vote")
else:
    print(f"Hello {name} youre not eligible to vote")

# Leap year
year = int(input("Enter a year: "))
if year%100==0 and year%400==0:
    print("Its a leap year")
elif year%100 !=0 and year%4==0:
    print("Its a leap year")
else:
    print("Its not a leap year")