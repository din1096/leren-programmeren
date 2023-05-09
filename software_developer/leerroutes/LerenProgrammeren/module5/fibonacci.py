def reeks(i):
    i -= 2
    getallenreeks = [0,1]
    for x in range(i):
        getallenreeks.append(getallenreeks[-1] + getallenreeks[-2])
        return reeks
reeks(int(input('voer een getal in')))