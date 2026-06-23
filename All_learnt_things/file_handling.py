# read, append, write, create, text, binary

f = open("myfile.txt","r")
text = f.read()
print(text)
f.close()

f = open("myfile2.txt","w")
f.write("yo")