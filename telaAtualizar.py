def abrir():
    import csv
    from livro import Livro
    livros = []

    def ler_arquivo(): 
        with open('livros.csv', newline='', encoding='utf-8', errors='ignore') as csvLeitura:
            linha = csv.reader(csvLeitura, delimiter=',')
            for coluna in linha:
                novoLivro = Livro(coluna[0], coluna[1],coluna[2],coluna[3],coluna[4],coluna[5])
                livros.append(novoLivro)



    def altera_dados():
        indice = int(input("Digite o índice do produto:"))
        print("Digite o atributo desejado. Se deseja manter, aperte ENTER")
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Gênero: ")
        editora = input("Editora: ")
        paginas = input("Páginas: ")
        preco = input("Preço: ")
        if titulo != "":
            livros[indice].titulo = titulo
        if autor != "":
            livros[indice].autor = autor
        if genero != "":
            livros[indice].genero = genero
        if editora != "":
            livros[indice].editora = editora
        if paginas != "":
            livros[indice].paginas = paginas
        if preco != "":
            livros[indice].preco = preco
    

    def escreve_arquivo():
        with open('livros.csv', 'w', newline='', encoding='utf-8', errors='ignore') as csvEscrita:
            escrever = csv.writer(csvEscrita)
            for c in livros:
                escrever.writerow([c.titulo, c.autor, c.genero, c.editora, c.paginas, c.preco])
            print(f"Livro Atualizado!")


    ler_arquivo()
    altera_dados()
    escreve_arquivo()