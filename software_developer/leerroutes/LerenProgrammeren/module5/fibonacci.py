def fibonacci(x):
    a = 0
    b = 1
    reeks = [a,b]
    for x in range(x-2):
        a,b = b, a+b
        reeks.append(b)
    guldensnee = b/a
    return reeks,guldensnee
aantal = int(input("voer een getal in:"))
print(fibonacci(aantal))