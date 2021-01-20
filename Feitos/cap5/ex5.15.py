
apagar = 0
while True:
    codigo = int(input('Insira o código do produto (0 para sair):'))
    preço = 0
    if codigo == 0:
        break
    elif codigo == 1:
        preço = 0.50
    elif codigo == 2:
        preço = 1.00
    elif codigo == 3:
        preço = 4.00
    elif codigo == 5:
        preço = 7.00
    elif codigo == 9:
        preço = 8.00
    else:
        print('Código Inválido!!')
    if preço != 0:
        quantidade = int(input('Insira a quantidade do produto:'))
        apagar = apagar + (preço*quantidade)
print(f'O preço a pagar pelo produto de código: {codigo} é de R$:{apagar:8:2f}.')
