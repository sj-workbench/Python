# OUTPUT
name = 'SJ'
age = 69
print(f"Hi my name is {name} and my age is {age}")   # Formated string/ F-string
# or
print("Hi my name is",name, "and my age is" ,age)  # Multiple values

# INPUT
# Input always return string, if you want a number then convert manually using int() or float()
age = int(input("What is your age: "))
print(f"So your age is {age}")  # return int()

# ARITHMETIC OPERATORS (+,-,/,*,**,%,//)
a = 13
b = 14
print(a+1)
print(a-1)
print(b/1)
print(a*1)
print(a**2)  # provides answer as power
print(b%2)   # provides remainder as answer
print(b//2)  # provides float value into integer

# COMPARISON OPERATORS (>,<,>=,<=,==,!=) [Returns boolean]
print(14==12)
print(14>12)
print(14<12)
print(14>=12)
print(14<=12)
print(14!=12)

# LOGICAL OPERATOR (and, or, not)
# and = both the condition to be true [if yes then prints true or else false]
# or = either one of the condition needs to be true 
# not = reverse the boolen [if its true then returns false and vice versa]
print(12<23 and 45==45) # returns true
print(12<23 and 40==45) # returns false
print(12<23 or 40==45) # returns true as one of them is true, if none is true then returns false    
print(not 40==45) # returns true as (not) reverse the output

# ASSIGNMENT OPERATOR (+=,-=,*=,/=,//=,%=,**=)
a = 12

a+=2
print(a)

a-=2
print(a)

a*=2
print(a)

a/=2
print(a)

a//=2
print(a)

a%=2
print(a)

a**=2
print(a)
