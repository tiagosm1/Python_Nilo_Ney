mercadoria = int(input('Insira o valor da mercadoria:'))
percdesc = int(input('Insira a % de desconto:'))

desconto = mercadoria * percdesc/100
totalcomdesc = mercadoria-desconto

print(f'O valor original do produto era R$:{mercadoria}')
print(f'Com o desconto de {percdesc}% totalizou em uma economia de R$:{desconto}')
print(f'O produto com desconto ficou R$:{totalcomdesc}')
