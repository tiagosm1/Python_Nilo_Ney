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
# Arquivo: exercicios3\capitulo 03\exercicio-03-10.py
##############################################################################

salário = float(input("Digite o salário atual:"))
p_aumento = float(input("Digite a porcentagem de aumento:"))
aumento = salário * p_aumento / 100
novo_salário = salário + aumento
print("Um aumento de %5.2f %% em um salário de R$ %7.2f" % (p_aumento, salário))
print("é igual a um aumento de R$ %7.2f" % aumento)
print("Resultando em um novo salário de R$ %7.2f" % novo_salário)
