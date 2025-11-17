s = {"let's", "learn"}
s.add("!")
print(s)


fs = frozenset(["hello", "world"])
#print(fs)
#fs.add("!")

s.add(fs)
print(fs)
