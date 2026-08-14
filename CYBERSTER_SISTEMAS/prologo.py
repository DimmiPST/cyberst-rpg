#prologo do cyberst
from funcoes_jogo import *
import time

#codigo das cores para auxiliar na criação do jogo
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
RESET = "\033[0m"
#para adicionar /033[codigo_cor + m

#INICIO CODIGO
def prologo1():
    print("-"*45)
    print(f"{AZUL} {"GERANDO JOGO...":^45}")
    time.sleep(2)
    input(f"Jogo Gerado Pressione ENTER para começar... {RESET}")
    print("-"*45)
    limpar()
    print(f"{AZUL}Em mais um dia de trabalho como estagiario em uma startup de cybersecurity... {RESET}")
    time.sleep(1.5)
    print("""
             _._._._._._._._._._._._._._._._._   
             | ___   ___    ___    ___   ___ |
         ^!^ ||_|_| |_|_|  |_|_|  |_|_| |_|_||
             |IIIII_IIIII__IIIII__IIIII_IIIII|      
             | ___   ___    ___    ___   ___ |
     )o(_    ||_|_| |_|_|  |_|_|  |_|_| |_|_||
    /(|)     |IIIII_IIIII__IIIII__IIIII_IIIII|
    H)o(_    | ___   ___    ___    ___   ___ |
    /(|)     ||_|_| |_|_|  |_|_|  |_|_| |_|_||
       H     |IIIII_IIIII__IIIII__IIIII_IIIII|    /)
       H     | ___   ___   _____   ___   ___ | __/ ),
       ~ ^~^ ||_|_| |_|_|  o~|~o  |_|_| |_|_||  ~^~^
      . ' .'.|IIIII_IIIII__|_|_|__IIIII_IIIII|'^~^'.',
     .,' , . |"""""""""""""/=====""""""""""""|.'.'.'.
       `~ ` "^^~ " ^^~'` "'     `",``~^^"" ~^^"   '~'
     .    "        "       ,   '           "    "
    Sher^  2-10-99
    ------------------------------------------------
    """)
    print(f"{AZUL}VOCÊ:{RESET}*Monitorando o Trafego de rede de um servidor*")
    time.sleep(1.5)
    print(f"{AZUL}PENSANDO:{RESET} Ah cara...acabou o café bem vou no deposito pegar mais")
    time.sleep(1.5)
    print(f"{AZUL}*Entra no Deposito*")
    time.sleep(1.5)
    print(f"*PENSANDO:{RESET} ahm cade o café???AH ACHEI , VEM AQUI")
    time.sleep(1.5)
    print(f"{AZUL}*Esbarra no café e o derruba atras da prateleira*")
    time.sleep(2)
    print("*Abaixa pra pegar o café e ve um pendrive*")
    time.sleep(2)
    print(f"*PENSANDO:*{RESET} Um pendrive?? bem.. vou pegar junto com o café e ve oque é")
    print(f"{AZUL}*Pega o pendrive e o café*")
    time.sleep(2)
    print(f"*PENSANDO:*{RESET}Ahm? projeto cyberst?SERA QUE É DE ALGUM EXECUTITO??? DEI A SORTE GRANDE")
    print(f"{AZUL}*De volta para o escritorio*")
    time.sleep(3)
    print(f"{AZUL}*PENSANDO:*{RESET}VOU COLOCAR O PENDRIVE NO COMPUTADOR E JA FAÇO O CAFÉ")
    time.sleep(3.5)
    print(f"{AZUL}*Coloca o café sobre a mesa*")
    time.sleep(3)
    print(f"{AZUL}*Coloca o Pendrive na Maquina e abre ele*")
    time.sleep(1.5)
    print(f"*PENSANDO*:{RESET} Só um arquivo?ah qual foi .. bem vou abrir né")
    time.sleep(2.5)
    print(f"{AZUL}*ABRE O ARQUIVO E ENTAO...*")
    time.sleep(2)
    print(f"{VERMELHO}Glitchs começam a aparecer na tela")
    time.sleep(2)
    print(f"{AZUL}*PENSANDO*:{RESET} Nao nao nao nao nao , Meu Deus oque eu fiz???")
    time.sleep(2.5)
    print(f"{AZUL}*TELA MONITOR:*")
    time.sleep(2)
    print(f"""{VERMELHO} B̶͔͍͚̼̟͕̣̍e̷̻͕̰͈͚̽͑m̴̡̧̙̥̞̼̙̬͉̼͔̩̋̀̏̋̉͘͠ ̵͕͋́͊͜v̸̨̤̺̜̺̜͍͈̹̙͇͍̝̤̓͊̽̅̃͐͋̇̈́̚͠į̷̢̛̬̱͕̦̰̜͇͆̄̈̐̑̃̑̉͗͘͜ń̵̢͍̘̗̳̗̦̟̥̞̞̲̦̩̹͌͒̾̕͝d̶̘̜̘͇̭͚̤̥̮̹͍̗̭͉̅̎̀̽̒̿ǫ̴̛͓̗̦͗̅́̿̀̅͌͐ ̵̛̝̩͇͎͔̯͕͆̓̒̅a̷͕̹͓̻̣͗̀͆́̚͘ö̷̜͚̳̹̠̤̙͕̖̭̯́̉̓͂̐͐́̌͆̆͘͜͝͝ͅ ̸̨̛̞̼̗̙̲͕̣̣̽̾͒̀̒̉̃̃͌͋̕
    ̶̨͎͈̻͕͉͓̟͓̥̒͆͛̈́̂͒̈̆͒̚͘̕͘͜͠͝P̷̤͙̲̐̾̑ͅR̵̨̢͈̫̻̙̳͇̰̼̯̤͕͛͑̎͆͆͑̄̚̕O̸̧̬̥͓̼͇͉͉̼̙͕͇̪͛͊́̔̿̏̕͝J̸̳̠̊͂̇̈́̑͐̃̐͒̓͐͝E̸̢̨̻̬͋̀͗͜T̵̡̡͍̩̺̗͍̜̜̽̇̉́̎̄́̈͋̄͝͝Ǫ̴̩͖̹̦̳̺̯̻̫̅̿͒̑́ ̵̧̛͖̺̭̼͕͎͖̯͕̘̪̊͛̉́̈́͛̈͑C̵̱̪̘͔̦͑͜ͅY̵̡̺̝̫̻̠̟̥̙͂̓̍̂̏͘B̴͉̬͉̫̘̗͆̂̓̈̽̑́́͝È̵̢͙̹͗̎͂͆̾͊̈͋͘͜R̶̢̯̺̪̖̣͚̪͊̀͊͆͂̉͆́̓̃͝Ş̴̺̤͇͇͚̦̪͎̪͔̖̪͕̍̅͗͐͑̒̇̎̑̍́̕̚T̸̢̧̧͚̹̹̘̦̥̫̹̩͐̐̀̋̑̓͝""")
    print(f"{AZUL}*LENDO:*{RESET} be-bem.. vindo ao Projet-o Cyb-")
    time.sleep(3)
    print(f"{VERMELHO}*Surge um Glitch Fora da tela Abstraindo Você e o café")
    input("""E̵̯͇͚̩̼̪͕̝̘͍͓̮̽͋̆͂̾̅́͗̓͑r̶̨̨̡̝̜͙͓̘̯͖͚̾͜r̵̡̛̹̹̼̝͚̄̃̏̌͂̄̓̋͛̉̉̕͘͝ǫ̵̢̙̜̤͍͙̮̲͙̯̠̤͔͒̈́̽̀̆̍̕4̷̙̞͕̰̦̲͂̓̔̈̍̋̔̿̀̇̐͘0̷̹̙̘͉̍͠4̷̘̄̀͑̌̈́̕ ̷̦̳̞̽͋̾̈́͛̀́̔͑̿͝E̴̬̳͇̦̪̺̫͕͙̠̳̳̪̭̅̑̃͋́͆̅̄͘͠R̸̢̡̧̫̭̳̼̮̰̭̠̯̣͇̈́̀̆̃͐̂̃͜R̵̨̖̗̖̝̠̞̱͉͊́̋̓̉̄̕̕͠ͅÖ̴̧̬͚̲̖̪͇̣̜͍̦́͌̑͜ͅ4̵͔̝͑̿͒͌͊̐̀̓̓̔͌̔͗̍͝0̷͚̘̳̫͈̻̤̈́͂̀̐̈́̃̄̈́̾̆́͋̑͝4̵̮̜̟͙͔̔͘͜ ̸̧̧̬͔̣͈͖̬̲̭͈̮̩͗͘Ę̷̮̩͉͚̝͉́Ŗ̷̱̭̜͓̜̠͕̤̺̲̖̝͕̎̽̆͠Ŗ̸̛̦̟͉̞̪̟͚̃̌̐͑͋͝Ȯ̴̢͕̘͎̝̰̳̮̣̘ͅͅ4̴̟͐͆̿͠0̵̨̪̩̹̜͚̳̺͆͐̀̕͝͠͝ͅ4̶̢̧͎̞͔̱̞̖̭̳̣̩̿͋̄̀Ȩ̸͉̬̝̦̥̲̝̝͕͓̒̒̈́͐̓͑̓͂̂͜͜͝͠R̴̥̗͈͖͇̳̝̪͆̏͛͊͊͌̎͑͝ͅȐ̴͚̽̋̓̎͗͛̄̈́́̕̕Ő̶̯͑̍̉͐̅̽̔̄̽̚͘4̷͇̰̤̟̇̈́̇͗̊̀̈́̆̌̓̊̒̕0̷̩̣̝͖͉̱͍͔̖͈̩̜̌͋̄̈́͗̏̐̆̀̍͜͝ͅ4̴̨̠̫̠͕͙̮͓̘̟̺́͘
    ̴̛̤̣͇͛̈́̈̀͜͠P̷͔̳͇̤̲̃̀̔̍ͅr̵̨̧͕̩͈̜͌̈́̇͛́͝ͅo̶̹͌̈͒̓̀̋̏̽̚͘͠͝c̴̛̜̈̓̌͛̀̋́͒̾̽͘͘͝ȩ̴̢̢̤̗̺̝͉̫̰̳̠̟̔͆̕͠s̷̷̡͙̜̜̞̹͔̦͔͓̑̓͆͜͜͜ͅͅo̸̡̨͔̯̘̜̯̣͕͗͜ ̸͉̏̋͂̐̑͠d̴̢̞͙̣̲̥̪̲̩͖̪̑͂̄̅͑͒̋̀͗̆̐̅͝ȩ̸̧̗̭̍̈͂ ̷͖̾̀̋́̊́͌̋̈́͛ͅ ̶̢̹̳̝͙̱͖̂̌̍͊̔͊̄̽̓͘͘͠A̶͕̠̣͔̠͗̎̋͂̇̂́̋̿̅͘͝b̷̖͍̲̝̄̉̅͌͆̓̎͋̀̃̊͠s̴͉̹͒̓͗̀̀̂̇̇̈́̐͋͗̀̕͝t̵̳̪̺̦̪̳̯͉̟͖͛̏̆̾r̷̻̗͕̯̙̈́̌̏̌͘͜å̶̛̘̠̜̜̲̬̉̋̓̓̀̌͠ͅç̴̡͓̘͈̫͚̠̠̝̘̝̼̲̝̌ã̶̙̥̦͙̩͕͈͕̺͈͈͚̣̇͘o̵͔̓̿
    PR3SS 3NT3R""")
    limpar()
def prologo2():
    print(f"{AZUL}*Conectando lembranças..*")
    time.sleep(3)
    print("Conectando Itens Exportados[CAFÉ]...")
    time.sleep(3)
    print("Carregando Servidor...")
    time.sleep(3)
    input("Pressione ENTER para exibir Assistente  Ryoko")
    limpar()
    print(f"""
⣪⡑⣤⣶⣶⣶⣦⡔⣩⡒⠀   Olá Seja Bem-Vindo(a) Ao Projeto Cyberst
⢸⣯⣾⣿⢏⣿⣏⢿⣿⣮⣿⠀  Eu sou Ryoko e irei lhe apresentar ao Projeto
⢸⣿⢸⡗⣶⠙⢱⡖⣿⢸⣿⠀  Esse Projeto Foi Desenvolvido Pelo DEV Dimmi/J.B
⢸⡿⠀⠳⣄⣐⣂⡴⠃⠸⣿⠀  O objetivo era fazer um projeto pra encerrar com Maestria
⣾⠃⠀⡵⡔⠕⠕⡰⡅⠀⢻⡆  Python basico e aprender manipulaçao de arquivo
⢹⡆⠘⢴⠙⠑⠉⢳⡱⠀⣾⠁  {VERMELHO} M4$ %̷̻̳͚͚̱͍̭̳͈̥̩̠̓̐̓͌́͌̚̕#̸̛̗͊̃̀̀̔̋̀͛̏́͘͘̕͝  t4lv3z ALg0 t3nh& dado ERr4d0...{AZUL}
⠊⠀⠀⠈⡖⡖⡖⡎⠀⠀⠈⠂  {VERMELHO}Eu s0u ryok0...{AZUL}Eu deveria te apresentar ao Projeto  M4s..
⠀⠀⠀⠀⠉⠁⠉⠁⠀⠀⠀⠀  {VERMELHO}A tecnologia evoluiu muito sabe? principalmente a militar...Oque tornou
                 possivel salvar os dados do projeto automaticamente cada vez que você conseguir 
                 algo importante,Bem  Boa Sorte Antes...Vou fazer seu registro """.center(50))
    print("-"*50)
    time.sleep(2)
    print(f"{AZUL} POR FAVOR PREENCHA SEUS DADOS")
    jogador = dados_jogador()
    print("Aguarde um Momento..")
    time.sleep(2)
    print("Dados Cadastrados com sucesso , adicionei o item exportado CAFÉ no seu inventario")
    time.sleep(2)
    while True:
        exibirdadosPrologo = input(f"{AZUL}Deseja Exibir seu inventario Antes de começar? :(S/N) ")
        if exibirdadosPrologo.upper() == "S":
            mostrar_dados(jogador)
            break
        elif exibirdadosPrologo.upper() == "N":
            print("Ok ocultando Dados do inventario temporariamente...")
            break
        else:
            print(f"{VERMELHO}Opçao invalida por favor digite corretamente...")
    print("Certo.. tudo concluido iniciando CYBERST...")
    time.sleep(2)
    input(f"{VERMELHO}E̷̛̫̖̭̰͕͔͇͇͎͆͒͆̓̂̊̍̽͋ͅŘ̶̨͔̇́̽̿͛̑̉̈́̋̑́̈́R̴̢͔̙̀̌̑O̸̜͔͈̍͗͛̈͌̀̇ ̵̛͇̘͙͕̝̆̒́̉̋̇̍͛̊̐̎͒̋  \n             Pr3s@ @t3 C0mp3l&t4r Pr0j3to ... pr3ss 3nt&r")