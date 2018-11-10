newlist=[]
for i in range(11):
    newlist.append(i*2)
print(newlist)


print([i*2 for i in range(11)])

list=['Jack','Maro','Peter','Luke']
for name in list:
    if name.startswith('P'):
        print('\n',name)

print([name for name in list if name.startswith('L')])
print([name for name in list_1 if name.startswith('J')])