class InnFuc:
  x=12
  def myfunc(self):
    global a
    a=200
    x = 300
    def myinnerfunc():
      print(x)
      print(InnFuc.x)
      print(a)
    myinnerfunc()


b=InnFuc()
b.myfunc()
print(a)

