dic={
    "brand": "bmw",
    "Model": "First",
    "Number": "PB07"
}
print(dic)
print(type(dic))
x = dic["Model"]
print(x)
dic["Model"]= "Second"
print(dic)
for x in dic:
    print(dic[x])
for x in dic:
    print(x)
for z, y in dic.items():
  print(z,":", y)
dic["color"] = "red"
print(dic)
dic2=dic.copy()
dic2["Price"]="10cr"
print(dic2)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for z, y in myfamily.items():
  print(z,":", y)
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
j = car.setdefault("model", "")
x = car.keys()
p = car.values()
print(p)
print(j)
print(x)
p = ('Car1','Car2')
q = ("Audi","City","swift")

this = dict.fromkeys(p, q)

print(this)