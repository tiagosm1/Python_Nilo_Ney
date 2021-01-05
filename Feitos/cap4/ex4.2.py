velocidade = int(input('Insira a velocidade do carro:'))
multa = (velocidade - 80) * 5
if velocidade > 80:
    print(f'Você ultrapassou a velocidade permitida e foi multado em R$:{multa})')
else:
    print('Você está na velocidade permitida!!!')
