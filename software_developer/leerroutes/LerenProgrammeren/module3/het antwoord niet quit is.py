count = 0
x = 1
y = 100
while x != y:
    count +=1
    vraag = input('?')
    print(vraag)
    if vraag == 'quit':
        print(count)
        break