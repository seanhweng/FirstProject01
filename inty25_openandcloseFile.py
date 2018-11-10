#
# file=open('introduction.txt')
# text=file.read()
# print(text)
# file.close()
#
with open('introduction.txt') as f:
    print(f.read())

with open('./introduction.txt') as file:
    print(file.read())

with open('introduction.txt','a') as file:
    file.write('\nThis line is just attached.')