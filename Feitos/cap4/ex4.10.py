kwh = int(input('Insira a quantidade de KWH consumida:'))
tipoinst = str(input('Insira o tipo de instalação: R (residencial) / C (comercial) / I (industrial)'))
if tipoinst == 'R' or 'r':
    if kwh <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif tipoinst == 'C' or 'c':
    if kwh <= 1000:
        preço = 0.55
    else:
        preço = 0.60
elif tipoinst == 'I' or 'i':
    if kwh <= 5000:
        preço = 0.55
    else:
        preço = 0.60
else:
    preco = 0
    print('Erro, instalação desconhecida!')
consumo = kwh * preço

print(f'O total da conta para o tipo de instalação {tipoinst} é R${consumo}')