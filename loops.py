# FOR LOOPS
# For loops =  execute a block of code a fixed number of times. You can iterate over a range, string, sequence etc.

# range() function = range(start, stop, step)
for x in range(1,11,1):         # in place of x can be named anything.
    print(x)
print("Good boy")
for x in reversed(range(1,11,1)):         # in place of x can be named anything.
    print(x)

# String
credit_card = "1234-2627-4473"
for x in credit_card:
    print(x)


for x in range(1,21):
    if x==13:
        continue      # skip over an iteration
    else:
        print(x)
for x in range(1,21):
    if x==13:
        break         # end on that iteration
    else:
        print(x)


# WHILE LOOPS  = execute some code while some condition remaains true
name = input("Enter your name: ")
while name == "":
    print("No name entered")
    name = input("Enter your name: ")
print(f"hello {name}")

age = int(input("Enter your age: "))
while age < 0:
    print("age cant be zero")
    age = int(input("Enter your age: "))
print(f"so youre {age} years old.")

food = input("Enter your food (q to quit): ")
while not food =="q":
    print(f"You like {food}")
    food = input("Enter your food (q to quit): ")
print('Bye')

num = int(input("Enter a number between 1 and 10: "))
while num<1 or num>10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 and 10: "))
print(f"Your number is {num}")

# NESTED LOOPS (loop within the loop.)   ex: while loop inside of while loop, for loop inside of for loops, while loop inside of a for loop or for loop inside of a while loop.

            