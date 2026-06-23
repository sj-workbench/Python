num = input("Enter a number: ")
print(f"The multiplication table of {num}: ")

for i in range(1,11):
    print(f"{int(num)} X {i} = {int(num)*i}")
print("END OF CODE")

# if in place of input we get something different than integer

n = input("Enter a number: ")
print(f"Multiplication taable of {n}: ")
try:
    for i in range (1,11):
        print(f"{int(n)}X{i} = {int(n)}*{i}")
except:
    print("sorry some error occured")

print("END OF CODE WITH ERROR")

try:
    num = int(input("Enter a nummber: "))
except ValueError:
    print("Entered number is not integer")