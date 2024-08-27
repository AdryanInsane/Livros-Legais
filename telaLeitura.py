import csv
def abrir():
    i = 0
    with open('livros.csv', newline='', encoding='utf-8', errors='ignore') as csvfile:
        leitor = csv.reader(csvfile, delimiter=',')
        for linha in leitor:
            print(f"* Livro {i}: {linha[0]}, {linha[1]}, {linha[2]}, {linha[3]}, {linha[4]}, R$ {linha[5]}")
            i = i+1