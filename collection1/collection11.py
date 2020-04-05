import collections
pranshu = ('Pranshu', 24, 'M')
print(pranshu)
print(type(pranshu))
d1 = collections.OrderedDict()
d1['A'] = 10
d1['C'] = 12
d1['B'] = 11
d1['D'] = 13

for k, v in d1.items():
    print(k,":", v)


a=collections.Counter({1:5,2:4})
print(type(a))
list = [1,2,4,7,5,1,6,7,6,9,1]
c = collections.Counter(list)
print(c[6])
list = ["x","y","z"]
deq = collections.deque(list)
print(deq)
deq.append("e")
print(deq)
deq.insert(0,"q")
print(deq)