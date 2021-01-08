valorimovel = float(input('Insira o valor do imóvel R$:'))
salario = float(input('Insira o seu salário mensal R$:'))
anos = int(input('Insira em quantos anos quer pagar:'))
prestacao = valorimovel / (anos * 12)
if prestacao >= salario * 0.30:
    print('Crédito não aprovado')
else:
    print(f'Crédito aprovado! O valor da prestação será de R$:{prestacao:6.2f}')
