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
# Arquivo: exercicios3\capitulo 11\exercicio-11-01.py
##############################################################################

import sqlite3
from contextlib import closing

with sqlite3.connect("precos.db") as conexao:
    with closing(conexao.cursor()) as cursor:
        cursor.execute('''
                create table preços(
                    nome text,
                    preço numeric)
                ''')
        cursor.execute('''
                insert into preços (nome, preço)
                    values(?, ?)
                    ''', ("Batata", "3.20"))
        cursor.execute('''
                insert into preços (nome, preço)
                    values(?, ?)
                    ''', ("Pão", "1.20"))
        cursor.execute('''
                insert into preços (nome, preço)
                    values(?, ?)
                    ''', ("Mamão", "2.14"))
