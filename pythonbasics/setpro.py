set1={"Ajay","Kanish","Jatin","Sonu","Pooja"}
set2={"Ravi","Bharti","Arti","Sarju","Poonam"}
set3=set1.union(set2)
print(set3)
set3.pop()
print(set3)
set3.pop()
print(set3)
print(set3.update(set2))
print(set3)

for x in set3:
  print(x)
set3.add("Shami")
print(set3)
set4=set(("vinod","sunny","rajni","shusma"))
print(set4)
set5=set3.intersection(set1)
print(set5)
print(set5.isdisjoint(set1))
print(set3.symmetric_difference(set1))
print(set5.isdisjoint(set4))
print(set3.intersection_update(set5))