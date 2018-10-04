# https://www.programiz.com/python-programming/methods/string

s = "abcdef"

print(s[0])
print(s[0:3]) # abc
print(s[0:4:2]) # ac

print(s.find('c')) # index of 'c'

print(s.replace('c','z')) # replaces all Cs with Zs = abzdef

print(s.count('e')) # counts occurances of 'e'