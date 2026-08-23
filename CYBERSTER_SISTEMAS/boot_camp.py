from funcoes_jogo import *
import time
from inimigos import*
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
    time.sleep(2.5)
    print(f"Voce:{RESET} um alvo? ok se prepare!!! EU VOU SAIR DESSE PROJETO MALDITO")
    time.sleep(4)
    Jogador_bootcamp["Item Atual"] = Jogador_bootcamp['Itens'][1] #atribuindo Pistola como Item Atual
    alvo = alvo_bootcamp()
    while alvo["Vida"] > 0: #iniciando a introduçao ao combate
        limpar()
        print(f"{AZUL}Visor: [Objetivo]: Elimine o Alvo")
        print(f"Vida Atual: {alvo['Vida']}")
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
        menu_combate(dados_combate=Jogador_bootcamp,inimigo=alvo)

def boot_camp2():
        limpar()
        time.sleep(2)
        print("_"*30)
        print("ALVO DERROTADO".center(30))
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⡀⢀⠀⢠⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢠⢤⣀⠀⠀⠀⠈⣆⢧⠈⡆⢸⠀⠀⠀⢰⢡⠇⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⠀⠀⣯⢀⣨⠃⠀⠀⠀⠸⡜⣄⣣⢸⠀⠀⠀⡜⡌⠀⠀⠀⠀⢀⡜⡁⠀⠀⠀⠀⠀
    ⠀⠀⠙⢮⡳⢄⠈⠁⠀⢠⠴⠍⣛⣚⣣⢳⢽⡀⣏⣲⣀⢧⡥⠤⠶⢤⣠⢎⠜⠁⠀⠀⠀⠀⠀
    ⠀⠠⣀⠀⠙⢦⡑⢄⢀⣾⣧⡎⠁⠀⠙⡎⡇⡇⡇⠹⢪⣀⡓⣦⢀⣼⣵⠋⢀⠴⣊⠔⠁⠀⠀
    ⠀⠀⠈⠑⢦⣀⠙⣲⣝⢭⡚⠃⠀⠀⠀⠸⠸⣹⠁⠀⠀⠀⠉⣹⣪⣎⡸⢞⡵⠊⠁⣀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⣷⢯⣨⠷⣝⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠵⣪⢶⣙⡤⠖⢉⣀⠤⠖⠂
    ⠀⠀⠀⠀⠀⢀⡞⢠⠾⠓⢮⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢬⣺⡯⢕⢲⠉⣥⣀⡀⠀⠀
    ⠀⠀⢀⡤⣀⢈⡷⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠘⠀⢱⢾⠘⢇⢴⠁⠀⠀
    ⠀⠀⢻⣀⡼⢘⣧⢀⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢙⣞⠆⠀⠀⠀⠀⠀
    ⠀⠀⠀⠉⠀⢿⡀⠈⠧⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⣹⣦⠇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠸⢤⡴⢺⡧⣴⡶⢗⡣⠀⡀⠀⠀⠀⡄⠀⢀⣄⠢⣔⡞⣤⠦⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⣀⡤⣖⣯⡗⣪⢽⡻⣅⠀⣜⡜⠀⠀⠀⠸⡜⡌⣮⡣⡙⢗⢏⡽⠁⠰⡏⠙⡆⠀⠀
    ⠀⠀⣒⡭⠖⣋⡥⣞⣿⡚⠉⠉⢉⢟⣞⣀⣀⣀⠐⢦⢵⠹⡍⢳⡝⢮⡷⢝⢦⡀⠉⠙⠁⠀⠀
    ⠐⠊⢡⠴⠚⠕⠋⠹⣍⡉⠹⢧⢫⢯⣀⣄⣀⠈⣹⢯⣀⣧⢹⡉⠙⢦⠙⣄⠑⢌⠲⣄⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⠧⡴⣳⣃⣸⠦⠴⠖⢾⣥⠞⠛⠘⣆⢳⡀⠈⠳⡈⠳⡄⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⡱⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⢣⠀⠀⠉⠀⠈⠂⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⠞⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        print("_"*30)
        time.sleep(1.5)
        print(f"{AZUL} *Coronel chega ao campo de tiro*")
        time.sleep(1.5)
        print("Coronel: olha.. oque aconteceu com voce?? kkkk voce sempre foi horrivel soldado")
        time.sleep(0.5)
        print("Horrivel nao...HORROROSO PIOR QUE HORRIVEL KKK parece ate outra pessoa")
        time.sleep(2)
        print(f"Voce:{RESET} obrigado senhor!tem mais algo que eu possa fazer???")
        time.sleep(1)
        print(f"{AZUL}Coronel: bem agora que voce mencionou tem sim, eu preciso que...")
        time.sleep(2)
        print("*Um soldado entra gritando no campo de tiro*")
        time.sleep(1)
        print("Soldado: CORONEL CORONEL CORONEL!!!!!!")
        time.sleep(0.5)
        print("Coronel: Oque foi Soldado, que desespero é esse???")
        time.sleep(2)
        print("Soldado:Coronel.. É que o DENJ-3  foi infectado por um virus trojan remoto..")
        print("E ele está derrotando todos nossos soldados... alem de esta indo pro centro de pesquisa..")
        time.sleep(3)
        print("Coronel: O DENJ-3? QUER ME EXPLICAR COMO NOSSO MELHOR MECHA FOI INFECTADO???")
        print("E QUEM TA CONTROLANDO ELE??")
        time.sleep(3)
        print("Soldado:Eu nao sei quem ta controlando.. acho que foi infectado depois de receber uma atualizaçao")
        time.sleep(2)
        print("Coronel: oh meu Deus...bem talvez seja uma boa oportunidade..")
        time.sleep(2)
        print("Soldado: Oportunidade de que coronel??")
        time.sleep(2)
        print("Coronel: De testar Um brinquedinho novo..")
        print(f"Coronel: Ei {Jogador_bootcamp['Nome']} hoje é seu dia de sorte, pegue isso")
        print("*Coronel entrega uma katana De Pulsos eletromagneticos (Katana-EMP)*")
        time.sleep(5)
        if "K-EMP" not in nome_itens:
            Jogador_bootcamp["Itens"].append({
                "Nome":"Katana EMP",
                "Dano": 75,
                "MAG": 2,
                "CAP": 2,
                "Descrição": "Primeira Katana a usar pulsos Eletromagneticos feita pelo Exército ,\n     produzidas por: Laboratorio Militar"
            })
        with open("jogador.json","w",encoding="utf-8") as jogadorjson:
            json.dump(Jogador_bootcamp,jogadorjson,indent=4,ensure_ascii=False)
        print(f"Coronel:{Jogador_bootcamp['Nome']} preste atençao essa katana ta em fase beta entao tome cuidado ")
        print("Agora va e tire esse virus do mecha talvez seja necessario zerar a vida dele,depois continuamos a coversa..")
        time.sleep(3)
        input(f"*{Jogador_bootcamp['Nome']} corre pelo boot_camp ate encontrar o mecha infectado*")
def boot_camp3():
    limpar()
    print("-"*30)
    print("PROXIMO AO CENTRO DE PESQUISA".center(30))
    print("-"*30)
    print(f"Você:{RESET}Achei.. vem aqui seu pedaço de lata")
    denj3_boot = denj3()
    turno_atual = 0
    while denj3_boot["Vida"] > 0:
        limpar()
        print(f"{AZUL}Visor: [Objetivo]: Elimine o mecha infectado")
        print(f"Turno: {turno_atual}")
        print(f"Vida Denj-3: {denj3_boot['Vida']}")
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢾⡿⠛⠋⠛⢿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡧⣄⣄⢀⣀⡤⣎⣷⢿⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⣤⡄⠀⠀⠀⠀⠀⣿⢷⡯⢽⣻⣷⣿⢛⣑⣾⣸⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣞⡄⠀⠀⠀⠀⣻⣟⣿⣯⡵⣻⢿⣶⣯⣽⣿⣿⣶⣻⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣽⡄⠀⠀⠀⣿⣟⣟⣷⠖⠛⠒⢛⡻⣿⣿⣟⣻⣿⣟⣷⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣹⣿⣿⣹⣀⣀⣀⣿⡿⡙⡬⢟⣶⡞⣥⢟⣽⣻⣻⣿⣯⣅⡀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣥⣽⣵⣚⡿⣿⣿⣿⣷⣿⣿⣏⢿⢿⡻⢹⣿⣿⣿⡇⠀⣩⢿⣿⣷⣄⠀⠀⠀⢀⣷⡃⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣰⣿⣽⣻⣿⣿⣿⣿⣿⢴⣿⡧⣿⣿⣿⣿⣴⣿⡡⡄⠒⣻⣿⣷⡄⠀⢸⢻⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣄⡀⠀⠀⣹⣿⣿⣟⣿⣮⣻⣿⣿⣦⣿⣥⢿⣿⣿⣿⣿⣿⣪⣴⣿⣿⣿⣿⣧⣄⡏⡌⡼⡺⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡿⠤⣼⣿⣏⣹⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠺⢽⡿⣟⠫⣝⡳⢟⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡘⣿⣿⢽⣨⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢱⣿⠛⠁⠀⠀⠈⠳⢽⣪⢍⣶⣟⣳⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⣿⣷⣃⣿⡟⢨⢛⣿⣿⣿⣿⣿⣿⣿⢻⣽⣦⣼⣧⠀⠀⠀⠀⠀⠀⠀⣽⣿⠿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣾⣻⠁⡿⢸⡟⡇⠙⢿⣿⠟⣡⡌⢻⣿⣿⣿⣦⣄⣠⣔⣆⣀⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        menu_combate(dados_combate=Jogador_bootcamp,inimigo=denj3_boot)
        print(f"{AZUL}")
        if turno_atual > 0 and turno_atual % 3 == 0:
            print("-"*30)
            print("*O mecha Denj-3 atacou*")
            print("-"*30)
            input("(press enter)")
            Jogador_bootcamp["Vida"] -= denj3_boot["Dano"]
            turno_atual += 1
        elif turno_atual != 0:
            print("-" *50)
            print("*O mecha Infectado esta preparando um ataque...*")
            print("-" *50)
            input("(press enter)")
            turno_atual += 1
        else:
            input("(press enter)")
            turno_atual += 1
    limpar()
    print("Denj-3: he's coming ....")
    print("-"*30)
    print("DENJ-3 FOI DERROTADO")
    print("-"*30)
    print("*Coronel chega correndo no corredor*")
    time.sleep(2)
    print("Coronel: Olha.. voce conseguiu usar essa katana no final das contas")
    time.sleep(2)
    print("bem acho que podemos continuar o assunto de mais cedo")
    time.sleep(2)
    print("recentemente nosso laboratorio detectou um aumento no numero de Malware ,e eu preciso que voce investigue isso")
    time.sleep(3)
    print("Quero que vá ate cyber_district e de uma olhada no que esta havendo,leve a katana com voce, ira precisar")
    time.sleep(3)
    print("boa viagem soldado... ate logo ")
    time.sleep(2)
    Jogador_bootcamp["Local"] ="cyber_district"
    with open("jogador.json", "w", encoding="utf-8") as jogadorboot:
        json.dump(Jogador_bootcamp, jogadorboot, indent=4,ensure_ascii=False)