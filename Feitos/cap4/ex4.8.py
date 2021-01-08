n1 = int(input('Insira o primeiro número:'))
n2 = int(input('Insira o segundo número:'))
op = str(input('Selecione a operação para fazer com os números (+ ou - ou * ou /):'))
if op == '+':
    res = (n1 + n1)
elif op == '-':
    res = (n1 - n2)
elif op == '*':
    res = (n1 * n2)
elif op == '/':
    res = (n1 / n2)
else:
    print('Operação não selecionada, escolha entre: + - * / ')
    op = 0
print(f'O resultado de {n1} {op} {n2} = {res}')