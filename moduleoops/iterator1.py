class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
      if self.a <= 20:
          x = self.a
          self.a += 1
          return x
      else:
          raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

for x in myiter:
    print(x)

for i in mytuple:
    print(i)

