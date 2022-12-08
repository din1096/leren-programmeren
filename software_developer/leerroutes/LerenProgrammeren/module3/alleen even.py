begin = int(input('type een begin getal in'))
einde = int(input('type een eind getal in'))
 
for i in range(begin, einde + 1): 
    if i % 2 == 0:
        print(i, end=" ")