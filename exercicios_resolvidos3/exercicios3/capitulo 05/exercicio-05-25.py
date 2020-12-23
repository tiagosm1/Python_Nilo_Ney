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
# Arquivo: exercicios3\capitulo 05\exercicio-05-25.py
##############################################################################

# Atenção: na primeira edição do livro, a fórmula foi publicada errada.
# A fórmula correta é p = ( b + ( n / b ) ) / 2
# A função abs foi utilizada para calcular o valor absoluto de um número,
# ou seja, seu valor sem sinal.
# Exemplos: abs(1) retorna 1 e abs(-1) retorna 1

n = float(input("Digite um número para encontrar a sua raiz quadrada: "))
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f"A raiz quadrada de {n} é aproximadamente {p:8.4f}")
