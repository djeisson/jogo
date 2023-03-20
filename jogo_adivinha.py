import time
from random import randint

name = " "

    #cabeçalho
def cabecalho():
    print("*" * 50)
    print("**             Jogo de Adivinhação              **")
    print("*" * 50)
    print("\n" * 3)
    print("-" * 50)
    print("1 para jogar\n2 para verificar o placar dos lideres\n3 para creditos\n4 sair")
    print("-" * 50)

    botao1 = int(input(""))
    if botao1 == 1:
        print("\n" * 50)
        print("carregando!!!")
        time.sleep(2)
        jogar()
    elif botao1 == 2:
        print("\n" * 50)
        print("carregando!!!")
        time.sleep(2)
        historico()
    elif botao1 == 3:
        print("\n" * 50)
        print("carregando!!!")
        time.sleep(2)
        creditos()
    elif botao1 == 4:
        print("saindo")
        breakpoint
    else:
        print("voce digitou algo não esperado pelo sistema, tente novamente!")
        return


#placar dos lideres
def historico():
    with open('dados.txt', 'r') as arquivo:
        for valor in arquivo:
            print(valor)
    time.sleep(3)
    print("-" * 30)
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
        print()

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
        print("\n" * 20)
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
            time.sleep(5)
            print("\n" * 50)
            opcao2 = int(input("O que deseja fazer agora?\n1 para jogar\n2 para verificar o placar dos lideres\n3 para creditos\n4 sair"))
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
            elif opcao2 == 4:
                print("saindo")
                break
            else:
                print("")
            
        elif chute != numero:
            acertou = False
            if chances != 3:
                print(f"voce errou, esta foi sua {chances}° chance!")
                time.sleep(3)
                print("\n" *30)
            elif chances == 3:
                print(f"voce errou, esta foi sua {chances}° chance!")
                print(f"o numero era {numero}")
                print("fim de jogo")
                with open('dados.txt', 'a') as arquivo:
                    for valor in name, chances, acertou:
                        arquivo.write(str(valor) + '         ')
                        print("feito")
                    arquivo.write("\n")
                time.sleep(5)
                print("\n" *30)
                opcao2 = int(input("o que deseja fazer agora?\n1 para jogar\n2 para verificar o placar dos lideres\n3 para creditos\n4 sair"))
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
                elif opcao2 == 4:
                    print("saindo")
                    break
                else:
                    print()


cabecalho()