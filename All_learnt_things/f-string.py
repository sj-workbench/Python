# Formatting
letter = "hey i name is {} and i m from {}"
name = "me"
country = "india"
print(letter.format(name, country))

# better way
# f-string
print(f"hey i m {name} and i m from {country}")

price = 49.000272
txt = f"price is {price: .2f}"
print(txt)

print(f"{2*30}")

print(f"hey i m {{name}} and i m from {{country}}")
