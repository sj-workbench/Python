# Built-in function
def Num_Mean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
def isgreater(a,b):
    if a>b:
        print("first is bigger")
    else:
        print("second is greater")
def islesser(a,b):
    pass           # use later, no output
a = 3; b=4
isgreater(a,b)
Num_Mean(a,b)
c = 3; d=5
isgreater(c,d)
Num_Mean(c,d)

# Built-in function
# ex: min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print() etc

# Function arguments
def average(a=9, b=1):
    print("Average is: ", (a+b)/2)
average()

def average(a=9, b=1):
    print("Average is: ", (a+b)/2)
average(b=2)

def name(fname,mname = "Jena",lname = "Singh"):
    print("Hello, ", fname,mname, lname)
name("SJ")

# Key words arguements
def num(a=2,b=5):
    print((a+b)/2)
num(b=3, a=9)

def num(a,b=21):
    print((a+b)/2)
num(a=22)

def average(*number):
    print(type(number))
    sum =0
    for i in number:
        sum = sum + i 
    print("Average is: ", sum/len(number))
average(5,6,7,1)

def names(**name):
    print(type(name))
    print("hellow,", name["fname"], name["mname"], name["lname"])
names(fname = "Raghav", mname = "singh", lname = "chaddha")

def average(*number):
    print(type(number))
    sum =0
    for i in number:
        sum = sum + i 
    return sum/len(number)
c = average(5,6,7,1)
print(c)
