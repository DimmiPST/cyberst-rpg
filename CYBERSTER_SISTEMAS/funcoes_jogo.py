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
            return jogador
    except FileNotFoundError: #gerando informaçoes padrao
        jogador["Nome"] = input("Qual Seu Nome?: ")
        while True:
            jogador["Sexo"] = input(f"{AZUL}Qual Seu Genero?(M/F): ").upper().strip()
            if jogador["Sexo"] == "M" or jogador["Sexo"] == "F":
                break
            else:
                print(f"{VERMELHO}Digite um formato Valido {RESET}")
        jogador["Itens"] = [ #MAG = magazine/capacidade/muniçao atual CAP = capacidade/muniçao Maxima
            {"Nome":"Café",
             "Dano":0,
             "MAG":0,
             "CAP":0,
             "Descrição":"Talvez possa Ser Util em Algum Momento",
             }
        ]
        jogador["Local"] = "Bootcamp"
        jogador["Vida"] = 100
        with open("jogador.json","w",encoding="utf-8") as dados_json: #salvando informaçoes padrao em um
            json.dump(jogador,dados_json,indent=4,ensure_ascii=False) #arquivo .JSON
        return jogador
def mostrar_dados(inventario_jogador): #Funcao pra mostrar os dados do usuario inclusive
    for chave, valor in inventario_jogador.items(): # os itens juntos ,Para deixar a saída mais limpa
        if chave != "Itens":
            print(f"{chave}: {valor}")
        else:
            for indice, conteudo in enumerate(valor,start=1):
                print(f"item N•{indice}")
                print(f"    Nome: {conteudo['Nome']}")
                print(f"    Dano: {conteudo['Dano']}")
                print(f"    MAG: {conteudo['MAG']}")
                print(f"    CAP: {conteudo['CAP']}")
                print(f"    Descriçao: {conteudo['Descrição']}")