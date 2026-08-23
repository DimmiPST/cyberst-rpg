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
        jogador["Item Atual"] = "Nenhum" #fazer push nisso
        jogador["Local"] = "Bootcamp"
        jogador["Vida"] = 100
        with open("jogador.json","w",encoding="utf-8") as dados_json: #salvando informaçoes padrao em um
            json.dump(jogador,dados_json,indent=4,ensure_ascii=False) #arquivo .JSON
        return jogador
def mostrar_dados(inventario_jogador): #Funcao pra mostrar os dados do usuario inclusive
    for chave, valor in inventario_jogador.items(): # os itens juntos ,Para deixar a saída mais limpa
        if chave != "Itens" and chave != "Item Atual":
            print(f"{chave}: {valor}")
        elif chave == "Itens":
            for indice, conteudo in enumerate(valor,start=1):
                print(f"item N•{indice}")
                print(f"    Nome: {conteudo['Nome']}")
                print(f"    Dano: {conteudo['Dano']}")
                print(f"    MAG: {conteudo['MAG']}")
                print(f"    CAP: {conteudo['CAP']}")
                print(f"    Descriçao: {conteudo['Descrição']}")
        else: #verificar se  item atual é lista ou string("nenhum item selecionado")
            if isinstance(inventario_jogador["Item Atual"], dict):
                print(f"{chave}: {valor['Nome']}")
            else:
                print(f"{chave}: {valor}")
def menu_combate(dados_combate,inimigo):
    if not isinstance(dados_combate["Item Atual"], dict):
        while True:
            limpar()
            print(f"{AZUL}")
            print("-"*40)
            print("Turno:0")
            print("SELECIONE UM ITEM PARA ENFRENTAR O INIMIGO".center(40))
            print("-"*40)
            print(f"Vida {dados_combate['Nome']}:{dados_combate['Vida']}")
            print(f"Item Atual: {dados_combate['Item Atual']}")
            escolha_alvo = input(
                "Oque voce deseja fazer?1-Selecionar item")
            if escolha_alvo == "1":
                mostrar_dados(dados_combate)
                while True:
                    try:  # mudando o item
                        indice_item = int(input(f"{AZUL}Informe o Indice do Item que deseja Selecionar"))
                        dados_combate["Item Atual"] = dados_combate['Itens'][indice_item - 1]
                        break
                    except (ValueError, IndexError):  # tratando opçoes invalidas
                        input(f"{VERMELHO}[ERRO] selecione um indice valido")
                break
            else:
                input(f"{VERMELHO}[ERRO] selecione uma opçao valida")
    else:
        print(f"Vida {dados_combate['Nome']}:{dados_combate['Vida']}")
        print(f"Item Atual: {dados_combate['Item Atual']['Nome']}")  # exibindo o item atual
        print(f"MAG: {dados_combate['Item Atual']['MAG']} / CAP {dados_combate['Item Atual']['CAP']}")
        escolha_alvo = input(
            "Oque voce deseja fazer?1-Atirar 2-Trocar item")#armazenando escolha do usuario

        if escolha_alvo == "1" and dados_combate["Item Atual"]["MAG"] > 0:#tratando caso a escolha seja 1 e tenha muniçao
            inimigo["Vida"] -= dados_combate['Item Atual']['Dano']
            dados_combate['Item Atual']['MAG'] -= 1

        elif escolha_alvo == "1" and dados_combate["Item Atual"]["MAG"] == 0:  # tratando caso nao tenha muniçao
            input(f"{VERMELHO} [ERRO] MAG insuficiente selecione outro item (press enter)")

        elif escolha_alvo == "2":  # tratando caso a escolha seja 2
            mostrar_dados(dados_combate)
            while True:
                try:  # mudando o item
                    indice_item = int(input(f"{AZUL}Informe o Indice do Item que deseja Selecionar"))
                    dados_combate["Item Atual"] = dados_combate['Itens'][indice_item - 1]
                    break
                except (ValueError , IndexError):  # tratando opçoes invalidas
                    input(f"{VERMELHO} [ERRO] selecione um indice valido")
        else:
            input(f"{VERMELHO} [ERRO] selecione uma opçao valida(press enter)")