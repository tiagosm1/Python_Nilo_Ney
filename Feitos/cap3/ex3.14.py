kmrodado = float(input('Insira o KM rodado:'))
diaalugado = float(input('Insira os dias alugados:'))

totdia = diaalugado * 60
totkm = kmrodado * 0.15

totalaluguel = totkm + totdia

print(f'O aluguel do veículo por {diaalugado} dias, que rodou por {kmrodado}Km será de R$:{totalaluguel}')