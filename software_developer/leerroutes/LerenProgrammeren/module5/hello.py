cijfer = int(input('type een cijfer in'))
def hello(cijfer):
    i = 1
    while(i < cijfer):
        print(f"hello from funtion town{i}!")
        i +=1
        if i > cijfer:
            break
            




hello(cijfer)