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
# Arquivo: exercicios3\capitulo 08\exercicio-08-01.py
##############################################################################

def máximo(a, b):
    if a > b:
        return a
    else:
        return b


print(f"máximo(5,6) == 6 -> obtido: {máximo(5,6)}")
print(f"máximo(2,1) == 2 -> obtido: {máximo(2,1)}")
print(f"máximo(7,7) == 7 -> obtido: {máximo(7,7)}")
