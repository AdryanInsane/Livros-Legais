import telaCadastro
import telaLeitura
import telaRemover
import telaAtualizar

while(True):
    print("*** MENU PRINCIPAL ***")
    print("1 - Cadastrar Livros")
    print("2 - Estoque Livros")
    print("3 - Deletar Livros")
    print("4 - Alterar Livros")
    opcao = int(input("Digite a opção desejada:"))
    if opcao == 1:
        telaCadastro.abrir()
    elif opcao == 2:
        telaLeitura.abrir()
    elif opcao == 3:
        telaRemover.abrir()
    elif opcao == 4:
        telaAtualizar.abrir()
    else:
        print("Opção inválida")

# CRUD = Create, Read, Update, Delete.
# 1 - cadastrar
# 2 - ler
# 3 - atualizar
# 4 - deletar