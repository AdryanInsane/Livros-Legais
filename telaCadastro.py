import csv
from livro import Livro

def escreveArquivo(titulo, autor, genero, editora, paginas, preco):
    with open('livros.csv', 'a', newline='', encoding='utf-8', errors='ignore') as csvfile:
        escreve = csv.writer(csvfile, delimiter=',')
        escreve.writerow([titulo, autor, genero, editora, paginas, preco])
        print("### LIVRO: -", titulo, "- Adicionado com sucesso! ###")

livros = []
def abrir():
    print("### BEM VINDO AO CADASTRO DE LIVROS ###")
    print("\nNOVO LIVRO:")
    titulo = input("Título: \n")
    autor = input("Autor: \n")
    genero = input("Gênero: \n")
    editora = input("Editora: \n")
    paginas = input("Páginas: \n")
    preco = input("Preco: \n")
    novoLivro = Livro(titulo, autor, genero, editora, paginas, preco)
    
    escreveArquivo(titulo, autor, genero, editora, paginas, preco)
    livros.append(novoLivro)