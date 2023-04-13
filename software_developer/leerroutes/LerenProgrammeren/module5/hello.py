cijfer = int(input('type een cijfer in'))
def hello(cijfer):
    x = 1
    while(x < cijfer):
        print(f"hello from funtion town{x}!")
        x += 1
        if x > cijfer:
            break
            
hello(cijfer)