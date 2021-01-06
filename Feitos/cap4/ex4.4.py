salario = float(input('Insira o seu salário para calculo do aumento R$:'))
basesal = salario
if basesal > 1250:
    aumento = (salario * 10 / 100)
    totalaumento = aumento + basesal
    print(f'O salário de R$:{basesal:6.2f} teve um aumento de 10% (R$:{aumento:6.2f}) totalizando R${totalaumento:6.2f}')
if basesal <= 1250:
    aumento = (salario * 15 / 100)
    totalaumento = aumento + basesal
    print(f'O salário de R$:{basesal:6.2f} teve um aumento de 15% (R$:{aumento:6.2f}) totalizando em  R${totalaumento:6.2f}')


