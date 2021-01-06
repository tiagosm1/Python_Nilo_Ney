distancia = int(input('Digite a distancia que deseja percorrer em Km:'))
percorrido = distancia
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print(f'Para percorrer {distancia} Km você gastará R$: {valor:6.2f}')