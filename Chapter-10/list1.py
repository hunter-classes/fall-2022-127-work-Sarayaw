#3

thelist= [76,92.3,'hello',True, 4,76]

thelist.append('apple')
thelist.append(76)
thelist.insert(3,'cat')
thelist.insert (0,99)

print(thelist.index('hello'))
print(thelist.count(76))
thelist.remove(76)
thelist.pop(thelist.index(True))

print (thelist)

