'''with open('numeros.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha)'''

import sys
print(f'Número de parametros: {len(sys.argv)}')
for n, p in enumerate(sys.argv):
    print(f'Parametro {n} = {p}')