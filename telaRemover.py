import csv
linhas = []
def abrir():
    indice = int(input("Digite o número do Livro a ser excluído:"))

    with open('livros.csv', newline='', encoding='utf-8', errors='ignore') as csvLeitura:
        leitor = csv.reader(csvLeitura, delimiter=',')
        for linha in leitor:
            linhas.append(linha)
    linhas.pop(indice)
    with open('livros.csv', 'w', newline='', encoding='utf-8', errors='ignore') as csvEscrita:
        escrever = csv.writer(csvEscrita)
        escrever.writerows(linhas)
        print(f"Arquivo atualizado!  O Livro: {indice} foi excluído com sucesso!")