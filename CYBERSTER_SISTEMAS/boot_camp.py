from funcoes_jogo import *
import time
Jogador_bootcamp = dados_jogador() #Variavel recebedora Do dicionario que guarda as informaçoes do jogador
#Usada para alterar e modificar dados
nome_itens = [itens_jogador["Nome"] for itens_jogador in Jogador_bootcamp["Itens"]]
'''Descriçao da atribuiçao em cima: Criando uma lista (nomeitens) que atraves de list compherension (comprimir listas)
esta recebendo o resultado de uma variavel chamada itens_jogador que a cada rodada do ( for in) guarda o dicionario que ta em
Jogador_bootcamp [itens] ja que cada item é um dic, o itns_jogador[nome] serve pra guardar apenas oque ta na posiçao nome desse dic de itens
E entao garda o resultado em nome_itens, que guarda os nomes dos itens no dicionario, essa lista vai ser usada para
verificar se um item ja existe no .json antes de adicionar (usada principalmente guando carregar o jogo)'''
def boot_camp():
    print(f"{AZUL} Ryoko : Teletransportando consciencia para boot camp...")
    time.sleep(2)
    input(f"Iniciando...")
    limpar()
    time.sleep(2)
    print("_"*30)
    print("BOOT CAMP".center(30)) #iniciando a parte 1 do jogo
    print("_" * 30)
    print()
    print(f"{AZUL}Coronel:")
    time.sleep(1)
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⠐⠒⠒⠠⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⠀⠀⣎⡂⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀Acorda Soldado!! Ta pensando no pós-vida?kkk
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀Hora do treinamento! va ate o campo de tiro e descarregue o pente 
⠀⠀⠀⠀⠀⠀⠀⠀⠸⢶⡾⢅⣉⡖⣆⣉⠬⣶⠾⠀⠀⠀⠀⠀⠀⠀⠀ah oque? Cade sua arma e o seu visor de status??! OQUE VOCE PERDEU?!
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡁⠘⢻⠀⠘⡛⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀Oh meu Deus tome essa pistola de laser XR1 e esse visor de status H1 e  TOME CUIDADO DESSA VEZ!!
⠀⠀⠀⢀⡠⢰⡆⣮⣯⢾⠩⡈⠉⡲⡂⠉⢈⢻⢦⡯⡧⠲⡤⣀⡀⠀⠀
⠀⠀⢞⠣⠝⠂⠉⠁⠀⠈⠠⢀⣁⡀⢀⣉⡀⠜⠸⠀⠈⠁⠚⠧⢚⢆⠀
⠀⢸⠀⠑⢄⠀⣀⣀⣀⣓⢲⠀⠡⠕⢢⠃⠐⣰⣦⣤⣤⡄⠀⠖⠁⠸⠀
⠀⠀⠀⠀⠈⣆⠣⠄⣀⠠⠋⠁⠂⢧⠆⠂⠉⠁⠄⣀⠠⢃⡜⠀⠀⠀⡇
⠀⢀⠀⠀⠀⡎⠑⡀⠀⠀⠀⠀⠐⢺⠁⠀⠀⠀⠀⠀⡰⠉⡆⠀⠀⢀⡇
⢠⠃⠀⠀⠀⠨⢢⠘⠤⣄⣀⣀⣘⣻⣀⣀⣀⣀⣤⠔⢁⢊⠀⠀⠀⠀⢡
⠸⠀⠀⠀⠀⠀⢫⠀⠘⡄⠀⠈⢉⠙⠋⠉⠁⠀⡼⠀⠀⡧⠀⠀⠀⠀⢸
⠀⠑⠢⠤⠧⠐⠃⠀⠀⠣⣀⠀⣀⠏⠃⡀⢀⡠⠃⠀⠀⠑⠀⠦⠤⠒⠃
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣸⣿⡇⠀⠀⣿⣿⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠚⠛⠛⠛⠛⠛⠃⠀⠀⠛⠛⠛⠛⠛⠛⠒⠀⠀⠀⠀⠀⠀""")
    time.sleep(4.5)
    if "Pistola XR1" not in nome_itens and "Visor H1" not in nome_itens:
        Jogador_bootcamp["Itens"].append({ #adicionando 2 itens no inventario do jogador: Pistola e visor
            "Nome":"Pistola XR1",
            "Dano":15,
            "MAG":12,
            "CAP":12,
            "Descrição":"Primeira geração de pistolas a laser,\n     produzidas por: JN-ARMS"
        })
        Jogador_bootcamp["Itens"].append({
            "Nome": "Visor H1",
            "Dano": 0,
            "MAG": 0,
            "CAP": 0,
            "Descrição": "Visor com sistema Python integrado para ver os status dos demais,\n    produzidas por: JN-ARMS"
        })
    with open("jogador.json","w",encoding="utf-8") as moficar_jogador: #Salvando as alteraçoes no .json
        json.dump(Jogador_bootcamp,moficar_jogador,indent=4,ensure_ascii=False)
    while True:
        exibir_itens = input(f"{AZUL}*Pistola XR1 e Visor H1 adicionados a seu inventario deseja conferir? (S/N)*")
        if exibir_itens.upper() == "S": #Perguntando ao usuario se ele deseja abrir o inventario e tratando essa escolha com if/else
            mostrar_dados(Jogador_bootcamp)
            break
        elif exibir_itens.upper() == "N":
            print("Ok ocultando inventario..")
            break
        else: # impedindo o usuario de digitar uma opçao invalida como "Cachorro"
            print(f"{VERMELHO}[ERRO] Digite uma opçao valida com a formatação correta")
    print("-"*30)
    input("Coronel:Pronto agora va treinar  No campo de tiro e descarregue o pente! ANDA LOGO SOLDADO!")
    limpar()
    print("_"*30)
    print("CAMPO DE TIRO".center(30)) #sub local da parte 1 onde introduz o sistema de combate
    print("_"*30)
    time.sleep(2)
    print(f"Voce:{RESET}  Nao entendi direito por que eu vim parar num centro militar?bem que aquela ryoko avisou ...")
    print("mas se eu quero sair preciso avançar ")
    time.sleep(5)
    print(f"{AZUL}Voce:{RESET} bem... vou fazer oque esse tal de coronel disse ..nunca usei uma arma ,será que consigo? ")
    time.sleep(3)
    print(f"{AZUL}*Surge um Alvo na sua frente*")
    time.sleep(2)
    print(f"Voce:{RESET} um alvo? ok se prepare!!! EU VOU SAIR DESSE PROJETO MALDITO")
    time.sleep(4)
    Jogador_bootcamp["Item Atual"] = Jogador_bootcamp['Itens'][1] #atribuindo Pistola como Item Atual
    vidaalvo = 180
    while vidaalvo > 0: #iniciando a introduçao ao combate
        limpar()
        print(f"{AZUL}Visor: [Objetivo]: Elimine o Alvo")
        print(f"Vida Atual: {vidaalvo}")
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢒⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡴⠋⣁⢹⣈⠑⢦⡀⠀⠀⠀
⠀⠀⠀⣀⡸⣁⣆⡀⠘⠀⠑⠀⣳⣀⣀⡀
⠁⠉⠉⠉⠩⡀⢆⠀⡠⠀⡹⠉⠙⠉⠀⠀
⠀⠀⠀⠀⠀⠰⢄⣉⣧⣉⡠⠎⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀""")
        print(f"Item Atual: {Jogador_bootcamp['Item Atual']['Nome']}")#exibindo o item atual
        print(f"MAG: {Jogador_bootcamp['Item Atual']['MAG']} / CAP {Jogador_bootcamp['Item Atual']['CAP']}")
        escolha_alvo = input("Oque voce deseja fazer?1-Atirar 2-Trocar item") #perguntando a escolha do usuario e armazenando ela
        if escolha_alvo == "1" and Jogador_bootcamp["Item Atual"]["MAG"] > 0: #tratando caso a escolha seja 1 e tenha muniçao
            vidaalvo -= Jogador_bootcamp['Item Atual']['Dano']
            Jogador_bootcamp['Item Atual']['MAG'] -= 1

        elif escolha_alvo == "1" and Jogador_bootcamp["Item Atual"]["MAG"] == 0: #tratando caso nao tenha muniçao
            input(f"{VERMELHO} [ERRO] MAG insuficiente selecione outro item (press enter)")

        elif escolha_alvo == "2": #tratando caso a escolha seja 2
            mostrar_dados(Jogador_bootcamp)
            while True:
                try: #mudando o item
                    indice_item = int(input(f"{AZUL}Informe o Indice do Item que deseja Selecionar"))
                    Jogador_bootcamp["Item Atual"] = Jogador_bootcamp['Itens'][indice_item-1]
                    break
                except ValueError or IndexError: #tratando opçoes invalidas
                    input(f"{VERMELHO} [ERRO] selecione um indice valido")
        else:
            input(f"{VERMELHO} [ERRO] selecione uma opçao valida(press enter)")
    limpar()
    print("_"*30)
    print("ALVO DERROTADO".center(30))
    print("_"*30)
boot_camp()