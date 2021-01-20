deposito = float(input('Insira o valor do depósito inicial:'))
taxa = float(input('Isira a taxa de juros em %:'))
mes = 1
saldo = deposito
while mes <= 24:
    saldo = saldo + (saldo * taxa/100)
    print(f'O saldo do mês {mes} é de R$:{saldo:5.2f}')
    mes = mes + 1
print(f'O ganho obtido nos meses é de R$:{saldo-deposito:8.2f}')
