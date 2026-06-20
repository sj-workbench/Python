# 1
fruits = ["orange","apple","grapes"]  # List = ordered and changeable, Duplicate ok
print(fruits[0:3:2]) # [start:end:step]
print(len(fruits))
print(dir(fruits))
fruits[0] = "pineapple"
print(fruits)
fruits.append("pineapple")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.insert(1,"car")
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
print(fruits.index("grapes"))

# 2
fruits = {"apple","grapes", "mango"}  # Set = unordered and immutable, add/remove ok, no duplicates
print(fruits)
print(dir(fruits))
fruits.add("pineapple")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)

# 3 
fruits = ("apple","mango","tomato") # Tuple = ordered and unchangeable, duplicates ok, faster than lists
print(type(fruits))
print(len(fruits))
print(fruits.index("mango"))
print(fruits.count("mango"))

# 4
# Dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates
capitals = {"usa":"washington_dc",
            "india":"new delhi",
            "china":"beijing",
            "russia":"moscow"}
print(dir(capitals))
print(capitals.get("china"))
print(capitals.update({"japan":"tokyo"}))
print(capitals)
capitals.pop("china")
print(capitals)
capitals.popitem()
print(capitals)
keys = capitals.keys()
print(keys)
values = capitals.values()
print(values)
items = capitals.items()
print(items)
for key,values in capitals.items():
    print(f"{key}:{values}")