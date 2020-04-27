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



print(tri_recursion(6))
print(recur_factorial(7))