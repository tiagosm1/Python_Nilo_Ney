with open('multiplos4.txt', 'r') as multiplos4:
    with open('pares.txt') as pares:
        for l in pares.readlines():
            if int(l) % 4 == 0:
                multiplos4.write(l)