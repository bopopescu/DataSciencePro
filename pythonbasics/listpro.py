fruit = ["apple","orange","banana","litchi","mango","guava","mausami","grapes","litchi"]
fruit2 = ["aaaa","bbbb","cccc","dddd","eeeee"]
"""fruit.append("kiwi")
fruit.insert(1,"chiku")
print(fruit)
t=fruit.count("litchi")
print(t)
print(len(fruit))

print(type(fruit))
print(fruit[-4: ])
print(fruit[ :4])
square=[0,1,4,9,16,25,36,49,64,81,100,121]
#n=int(input("Enter the number from 0-11: "))
#print("Square of ",n, " is :",square[n])"""
fruit.extend(fruit2)

print(fruit)
fruit.sort(reverse=True)
print(fruit)
fruit.reverse()
print(fruit)
letters = []
for letter in 'Python':
    letters.append(letter)
print(letters)
x = {'chrome': 'browser', 'Windows': 'OS', 'C': 'language'}
x['mouse'] = 'hardware'
print(x['Windows'])
print(x)