n1 = int(input('Insira o primeiro número:'))
n2 = int(input('Insira o segundo número:'))
x = 1
r = 0
while x <= n2:
    r = r + n1
    x = x + 1
print(f'{n1} x {n2} = {r}')