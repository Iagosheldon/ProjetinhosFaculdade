opcao = ""
livros = ""
livros2 = ""
pilha = []
fila = []
tam = []
qnt = 10
opcao2 = ""

while opcao != '7':

    if opcao == "":
        livros = input("Qual livro você deseja adicionar à fila de leitura?\n")
        fila.append(livros)
        print(f"Você adicionou {livros} à fila de leitura!\n")
        print("Escolha outra opção: \n")

    else:
        while opcao2 != "7":

            if len(tam) <= qnt:
                opcao2 = input("\n[1] Adicionar outro livro\n"
                               "[7] Retornar para o menu\n\n")

                if opcao2 == "1":
                    livros = input("Digite o nome do outro livro: ")
                    fila.append(livros)
                    print(f"Você adicionou {livros} à fila de leitura!\n")

    opcao = input("[1] Adicionar\n"
                  "[2] Remover da fila de leitura\n"
                  "[3] Verificar fila de leitura\n"
                  "[4] Adicionar à fila de prioridade\n" #Prioridade de leitura é da maior para menor#
                  "[5] Remover da fila de prioridade\n"
                  "[6] Verificar lista de prioridade\n"
                  "[7] Encerrar\n\n")

    if opcao == "1":
        livros = input("Digite o nome do outro livro: ")
        fila.append(livros)
        print(f"Você adicionou {livros} à fila de leitura!\n")

    elif opcao == "2":
        if len(fila) != 0:
            fila.pop(0)
            print("Você acabou de remover o primeiro livro da fila!\n")
        else:
            print ("Não há livros para serem removidos\n")

    elif opcao == "3":
        if len(fila) != 0:
            print("Livros a serem lidos: ",fila)
            print("")
        else:
            print ("Não há livros para serem lidos\n")

    elif opcao == "4":
        livros2 = input("Qual livro você deseja adicionar à fila de prioridade?\n")
        pilha.append(livros2)
        print(f"Você adicionou {livros2} à fila de prioridade!\n")
        print("Escolha outra opção: \n")

    elif opcao == "5":
        if len(pilha) != 0:
            pilha.pop()
            print("Livro com maior prioridade removido!\n")
        else:
            print("Não há livros na prioridade para serem removidos\n")

    elif opcao == "6":
        if len(pilha) != 0:
            print("Livros na prioridade a serem lidos: ", pilha)
        else:
            print("Não há livros para serem lidos\n")

    elif opcao == "7":
        print("Finalizado!")

    else:
        print("Opção inválida. Digite uma opção correta.\n")
        continue