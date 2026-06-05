# Every character in a string has a unicode even spaces too
a = " "
b = " % "
c = "hellow"
d = " hellow i m sj"
print(ord(a))

# String indexing
a = "hello"
# hello = h = 0, e = 1, l = 2, l = 3, o = 4
# hello = h = -5, e = -4, l = -3, l = -2, o = -1
print(a[0])
print(a[-5])

# String Slicing   a[start:stop:step]
a = "hello"
print(a[0:4:2])

# Type conversion
a = 12.4
b = int(a)
print(type(a))
print(type(b))
b = str()
c = float()

a = "hello"
b = ""
c = {}
d = []
e = ()
f = False
g = 12
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print(bool(g))

 