##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2020
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: exercicios3\capitulo 08\exercicio-08-09.py
##############################################################################

# Comparando o programa da listagem 8.12 com o resultado
# da listagem 8.13.
#
# O programa calcula o fatorial de 4
# Pelas mensagens impressas na listagem 8.13 e pelo rastreamento do programa,
# podemos concluir que o fatorial de 4 é calculado com chamadas recursivas
# na linha: fat = n * fatorial(n-1)
#
# Como a chamada do fatorial precede a impressão da linha Fatorial de,
# podemos visualisar a sequencia em forma de pilha, onde o cálculo é feito de fora
# para dentro: Calculo do fatorial de 4, 3 , 2 e 1
# para então processiguir na linha seguinte, que faz a impressão dos resultados:
# fatorial de 1,2,3,4
