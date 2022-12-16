while True:
    try:
        vraag = input('?')
    except NameError:
        print(vraag)
        continue
    if vraag == 'quit':
        print('')
        