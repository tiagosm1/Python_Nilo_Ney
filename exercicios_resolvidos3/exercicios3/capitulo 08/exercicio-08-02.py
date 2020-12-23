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
# Arquivo: exercicios3\capitulo 08\exercicio-08-02.py
##############################################################################

def múltiplo(a, b):
    return a % b == 0


print(f"múltiplo(8,4) == True  -> obtido: {múltiplo(8,4)}")
print(f"múltiplo(7,3) == False -> obtido: {múltiplo(7,3)}")
print(f"múltiplo(5,5) == True  -> obtido: {múltiplo(5,5)}")
