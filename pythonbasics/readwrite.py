ftr=open("mytxt.txt", 'r')
print(ftr)
print(ftr.tell())
s=ftr.readline()
print(s)
print(ftr.tell())
content=ftr.read(9)
print(content)
print(type(content))
ftr2=open("mytxt.txt", 'a')
print(ftr2.tell())
ftr2.write("jfieehghj")

print(ftr2.tell())


