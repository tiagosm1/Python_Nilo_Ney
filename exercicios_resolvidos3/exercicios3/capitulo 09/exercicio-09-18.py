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
# Arquivo: exercicios3\capitulo 09\exercicio-09-18.py
##############################################################################

# Se o # aparecer no nome ou telefone de uma entrada na agenda,
# ocorrerá um erro ao ler o arquivo.
# Este erro ocorre pois o número de campos esperados na linha será diferente
# de 2 (nome e telefone).
# O programa não tem como saber que o caracter faz parte de um campo ou de outro.
# Uma solução para este problema é substituir o # dentro de um campo antes de salvá-lo.
# Desta forma, o separador de campos no arquivo não seria confundido com o conteúdo.
# Durante a leitura a substituição tem que ser revertida, de forma a obter o mesmo conteúdo.
