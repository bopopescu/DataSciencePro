def isPrime(n):
    for i in range(0, n + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j) == 0:
                    break
            else:
                print(i ,end=" ")



def my_function(*kids):
  print("The youngest child is " + kids[1])


def my_function2(child3, child2, child1):
  print("The youngest child is " + child3)


def my_function3(**kid):
      print("His last name is " + kid["lname"])




my_function("Emil", "Tobias", "linux ")
my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
my_function3(fname = "Tobias", lname = "Refsnes")
a = int(input("Enter baa range : "))

print(isPrime(a))





