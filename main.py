#Local onde o codigo principal vai rodar
import subprocess  #importando funçoes
import time
from CYBERSTER_SISTEMAS import prologo
#criando funçoes/def
def limpar():
    subprocess.run("clear",shell=True)
def menu():
    print(f"{AZUL}-" * 30)
    print(f"{AMARELO} {"CYBERST - MENU PRINCIPAL":^30}")
    print(F"{AZUL}-" * 30)
    print("ESCOLHA UMA OPÇAO".center(30))
    print("1-Load Game \n2-New Game \n3-Quit")
#definindo cores
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"
#inicio do codigo
while True:
    try:
        menu()
        escolha_opcaomenu = int(input("Escolha: "))
        while escolha_opcaomenu not in [1,2,3]:
            print(f"{VERMELHO}O numero {escolha_opcaomenu} não é uma opçao valida")
            input("Pressione ENTER para tentar novamente")
            limpar()
            menu()
            escolha_opcaomenu = int(input("Escolha: "))
        break
    except ValueError:
        print(f"{VERMELHO }Opção Invalida Por Favor digite uma opção valida")
        input(f"Pressione ENTER  para tentar novamente {RESET}")
        limpar()
print("-"*30,f"{RESET}")
if escolha_opcaomenu == 1: #sistema de load
    pass
elif escolha_opcaomenu == 2: #game normal
    limpar()
    prologo.prologo1()
    #implementar prologo2 e cadastro player
else:
    limpar()
    print("-"*30)
    print("CYBERST - SYSTEM".center(30))
    print("SAINDO....")
    time.sleep(2)
    print("OK,VOLTE SEMPRE")
    print("-"*30)
