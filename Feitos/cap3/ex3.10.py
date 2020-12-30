salario = int(input('Digite seu salário: '))
porc = int(input('Insira a % de aumento: '))

totsal = salario * porc/100
total = salario + totsal

print(f'O salário teve {porc}% de aumento totalizando em R$:{totsal}')
print(f'Agora o salário ficou em R$:{total}')