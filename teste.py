import random      #bibliotecas
import time
import emoji


def iguais():
    print('<>' * 10)
                          #funções
def texto(txt):
    iguais()
    print(txt.center(20))
    iguais()


animais = ['camelo', 'coruja', 'gato', "cachorro",]          #lista
frutas = ["uva", "laranja", "banana", "jaca"]

topicos = {                                   #dicionario
    "animal": animais,
    "fruta": frutas
}

texto('JOGO DA FORCA')

while True:                   #estrutura de repetição
    print('Vamos jogar? ')
    querJogar = str(input('Sim / Não: ')).strip().upper() == "SIM"

    if not querJogar:
        break

    print("Escolha um tópico:")
    topico_selecionado = input(f"""Lista {", ".join([f'"{key}"' for key in topicos.keys()])}:\n""").lower()

    palavras_topico_selecionado = topicos[topico_selecionado]

    palavra_secreta = random.choice(palavras_topico_selecionado).lower()
    letras_pessoa = []
    tentativas = 6

    print("Você tem 6 tentativas. ")
    print("\033[35mPensando na palavra... \033[m ")
    time.sleep(3)
    print("Palavra escolhida, vamos jogar!")

    palpites = ["_"] * len(palavra_secreta) # Gera a lista underline, com o tamanho da palavra escolhida
    print(f"A palavra tem {len(palavra_secreta)} letras ")
    print(' '.join(palpites))  # Mostra underlines separadas por espaços

    while True:
        print("Qual letra você acha que a palavra tem? ")
        while True:

            letra = input("letra: ")
            if len(letra) != 1:
                print('Digite apenas uma letra! ')
            else:
                if letra in letras_pessoa:
                    print(f'A letra {letra} já foi escolhida.')
                else:
                    break

        letras_pessoa.append(letra)           #adicionar a letra que a pessoa escolheu
        print(f'Letras tentadas: {(" ").join(letras_pessoa)}')

        if letra in palavra_secreta:   #Se a letra estiver na palavra secreta ele vai criar uma lista chamada posicoes
            posicoes = []
            # verifica todas as posições que tem a letra
            for indice, letra_palavra_secreta in enumerate(palavra_secreta):
                if letra == letra_palavra_secreta:     #se letra for igual a uma letra da palavra secreta
                    palpites[indice] = letra_palavra_secreta  #palpites na posição indice recebe a letra
                    posicoes.append(indice)        #adicionar a letra acertada na posição indice
            print(f'\033[1;32mVocê acertou uma letra na(s) posição(s) {" , ".join(map(str, posicoes ))} \033[m')

            print(' '.join(palpites))

            if palavra_secreta == ''.join(palpites):
                print(emoji.emojize("parabéns você ganhou :clap: :heart_eyes: !", use_aliases=True))
                break

        else:
            print('\033[1;91mVocê errou uma letra !\033[m')
            tentativas -= 1
            if tentativas <= 0:
                print(emoji.emojize('Você perdeu :sob: :sob: ', use_aliases=True))
                print(f'A palavra era "{palavra_secreta}" . ')
                break
            print(f'Tente novamente \nAgora você tem {tentativas} chances.')

    print(emoji.emojize('Obrigado por jogar :blush:', use_aliases=True))

print("Até a proxima! ")

