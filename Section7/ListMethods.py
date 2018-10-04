# https://www.programiz.com/python-programming/methods/list
a = [1,2,3]
b = [4,5,6]

c = a + b
print(c) # [1, 2, 3, 4, 5, 6]

s = 'a b c d e f'
z = s.split() # splits onn basis of space
print(z)

if 'a' in z:
    print("'a' is in list z")
else:
    print("'a' is not in list z")

if 'g' not in z:
    print("'g' is not in list z")
else:
    print("'g' is in list z")

for i in z:
    print(i)

q = [2,1,5,4,8,7]
q.sort()
print(q)

q.reverse()
print(q)

print(q.count(2))
print(q.index(8))
print(len(q))
print(min(q))
print(max(q))

