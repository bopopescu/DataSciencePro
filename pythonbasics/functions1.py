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


def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)

  else:
    result = 0
  return result


def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)


my_function("Emil", "Tobias", "linux ")
my_function2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
my_function3(fname = "Tobias", lname = "Refsnes")
a = int(input("Enter baa range : "))

print(isPrime(a))
print(tri_recursion(6))
print(recur_factorial(7))




