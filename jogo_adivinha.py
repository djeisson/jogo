import time
from random import randint

chances = " "
acertou = bool
name = " "
#opcao de salvar
def salvar():
    with open('dados.txt', 'a') as arquivo:
                for valor in name, chances, acertou:
                    arquivo.write(str(valor) + '         ')
                    print("feito")
                arquivo.write("\n")

#opcoes do jogador
def opcao():
    print("1 para jogar\n2 para verificar o placar dos lideres\n3 para creditos\n4 sair")
    botao1 = int(input(""))
    if botao1 == 1:
        carregar()
        jogar()
    elif botao1 == 2:
        carregar()
        historico()
    elif botao1 == 3:
        carregar()
        creditos()
    elif botao1 == 4:
        print("saindo")
        breakpoint
    else:
        carregar()
        print("voce digitou algo não esperado pelo sistema, tente novamente!")
        return opcao()

#funcao de tempo e carregamento    
def carregar():
    print("\n" * 50)
    print("carregando!!!")
    time.sleep(2)
    


    #cabeçalho

#cabecalho
def cabecalho():
    print("*" * 50)
    print("**             Jogo de Adivinhação              **")
    print("*" * 50)
    print("\n" * 3)
    

    opcao()

#historico de jogadas
def historico():
    with open('dados.txt', 'r') as arquivo:
        for valor in arquivo:
            print(valor)
    time.sleep(3)
    opcao()
    

def creditos():
    print("escrever bio do desenvolvedor")
    opcao2 = int(input("o que deseja fazer agora?\n1 para jogar\n2 para verificar o placar dos lideres\n3 para creditos"))
    if opcao2 == 1:
        print("\n" * 50)
        print("carregando!!!")
        time.sleep(2)
        jogar()    
    elif opcao2 == 2:
        print("\n" * 50)
        print("carregando!!!")
        time.sleep(2)
        historico()
    elif opcao2 == 3:
        print("\n" * 50)
        print("carregando!!!")
        time.sleep(2)
        creditos()
    else:
        print("")

#função de jogar
def jogar():
    chances = 0
    numero = randint(0, 10)

    name = input("Informe seu nome com duas letras, para iniciar o jogo: ")
    time.sleep(3)

    while chances != 3:
        chances = chances + 1
        print(f"vamos lá {name}! \nVocê deve acertar um numero entre 0  e 10")
        chute = int(input(""))
        if chute == numero:
            acertou = True
            print("\n" * 50)
            print("Parabéns você acertou!!")
            #funçao para salvar usuario e tentativas
            with open('dados.txt', 'a') as arquivo:
                for valor in name, chances, acertou:
                    arquivo.write(str(valor) + '         ')
                    print("feito")
                arquivo.write("\n")
                
            #chamaar sql para salvar dados no bd?
            
            opcao()
            
        elif chute != numero:
            acertou = False
            if chances != 3:
                print(f"voce errou, esta foi sua {chances}° chance!")
            elif chances == 3:
                print(f"voce errou, esta foi sua {chances}° chance!")
                print(f"o numero era {numero}")
                print("fim de jogo")
                with open('dados.txt', 'a') as arquivo:
                    for valor in name, chances, acertou:
                        arquivo.write(str(valor) + '         ')
                        print("feito")
                    arquivo.write("\n")
                opcao()


cabecalho()