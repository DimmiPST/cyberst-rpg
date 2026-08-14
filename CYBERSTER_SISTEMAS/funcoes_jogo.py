import subprocess #importando funçoes
import json

#codigo das cores para auxiliar na criação do jogo
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"


def limpar(): #criando funçoes uteis para o jogo para evitar repetir codigo dentro das outras funçoes
    subprocess.run("clear",shell=True)
def dados_jogador():
    jogador = dict()
    try: #testando se existe um arquivo (so vai ir pro except na primeira vez)
        with open("jogador.json","r",encoding='utf-8') as carregar_json:
            jogador = json.load(carregar_json)
    except FileNotFoundError: #gerando informaçoes padrao
        jogador["Nome"] = input("Qual Seu Nome?: ")
        while True:
            jogador["Sexo"] = input(f"{AZUL}Qual Seu Genero?(M/F): ").upper().strip()
            if jogador["Sexo"] == "M" or jogador["Sexo"] == "F":
                break
            else:
                print(f"{VERMELHO}Digite um formato Valido {RESET}")
        jogador["Itens"] = [
            {"Nome":"Café",
             "Dano":0,
             "Descrição":"Talvez possa Ser Util em Algum Momento",
             }
        ]
        jogador["Local"] = "Bootcamp"
        jogador["Vida"] = 100
        return jogador # pra variavel que chamar se tornar um dicionario e poder mecher alterar dados