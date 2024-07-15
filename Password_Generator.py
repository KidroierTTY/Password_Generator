def generate(number_of_symbols=6):
    import random
    symbols = []
    for i in range(number_of_symbols):
        num = random.randint(1, 3)
        if num == 1:
            symbols.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        elif num == 2:
            symbols.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        elif num == 3:
            symbols.append(random.choice('0123456789'))
    password = ''.join(str(symb) for symb in symbols)
    text.delete('1.0', tkinter.END)
    text.insert('1.0', password)
