class Livro:
    # Método construtor
    def __init__(self, titulo, autor, genero, editora, paginas, preco):
        # ATRIBUTOS DA CLASSE CONTA
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__editora = editora
        self.__paginas = paginas
        self.__preco = preco

    @property
    def tamanho(self):
        return self.__titulo
    @tamanho.setter
    def titulo(self, valor):
        self.__titulo = valor

    @property
    def cor(self):
        return self.__autor
    @cor.setter
    def autor(self, valor):
        self.__autor = valor

    @property
    def genero(self):
        return self.__genero
    @genero.setter
    def genero(self, valor):
        self.__genero= valor

    @property
    def editora(self):
        return self.__editora
    @editora.setter
    def editora(self, valor):
        self.__editora = valor

    @property
    def paginas(self):
        return self.__paginas
    @paginas.setter
    def marca(self, valor):
        self.__paginas = valor

    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, valor):
        self.__preco = valor