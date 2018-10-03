l = [100,200,300] # List is mutable
t = (100,200,300) # tuple is immutable

lsit = [1]
print(lsit)

tpule = (1)
print(tpule)


l.append(400)
# t.append(400) Tuples are immutable, hence append is not allowed

print(l)
print(t)
#print(t(4)) Not allowed