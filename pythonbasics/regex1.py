import re

txt = "My name is Ajay"
x = re.search("^.*.$", txt)
print(type(x))
print(x)
y = re.findall("a", txt)
print(len(y))
print(y)
print(type(y))
z = re.search("\s", txt)

print("The first white-space character is located at index:", z.start())
t = re.split("\s", txt)
print(t)
p = re.search(r"\bn\w+", txt)
print(p.span())
email= "ajaychopra156@gmail.com"
txt2="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
a=re.search(txt2,email)
print(a)

