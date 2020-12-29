dias = int(input('Insira o número de dias:'))
horas = int(input('Insira o número de horas:'))
minutos = int(input('Insita o número de minutos:'))
segundos = int(input('Insira o número de segundos:'))

total_em_segundos = dias * 86400 + horas * 3600 + minutos * 60 + segundos

print(f'Os valores inseridos totalizam em {total_em_segundos} segundos!')