import sys

# Verifica se os parâmetros foram passados
if len(sys.argv) != 4:  # Lembre-se que o nome do programa é o primeiro da lista
    print("\nUso: e09-02.py nome_do_arquivo inicio fim\n\n")
else:
    nome = sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arquivo = open(nome, "r")
    for linha in arquivo.readlines()[inicio-1:fim]:
        # Como a linha termina com ENTER,
        # retiramos o último caractere antes de imprimir
        print(linha[:-1])
    arquivo.close()