f = open("server_list1.txt")
x = []
for m in f.readlines():
	x.append(m.rstrip())

g = open("server_list2.txt")
y = []
for n in g.readlines():
	y.append(n.rstrip())

print ('=====START=====')
result = set(y) - set(x) 
print(sorted(result))
