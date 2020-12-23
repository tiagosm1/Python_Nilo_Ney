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
# Arquivo: exercicios3\capitulo 11\exercicio-11-04.py
##############################################################################

import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        preço1 = input("Digite o menor preço a listar: ")
        preço2 = input("Digite o maior preço a listar: ")

        cursor.execute('''select * from preços
                          where preço >= ? and preço  <= ?''',
                       (preço1, preço2))
        achados = 0
        for resultado in cursor.fetchall():
            print("Nome: {0:30s} Preço: {1:6.2f}".format(*resultado))
            achados += 1
        if achados == 0:
            print("Não encontrado.")
        else:
            print("{} produto(s) encontrado(s).".format(achados))
