import random
import time
import androidhelper
d = androidhelper.Android()
vida = 100
life = 50

mon =3
heal =3

def menu():
    opcao =''
    opcoes=['1','2','x']
    while opcao not in opcoes:
        for i in range(20):
            print("")
        print("")
        print("")    
        print(" >>>> Monster Slayer <<<<")
        print("[1] Jogar")
        print("[2] Instruções")
        print("[x] Sair")
        print("")
        print("")
        opcao= input("opcao: ")
        if opcao not in opcoes:
            print("opção inválida!", opcao)
            continue
        return(opcao)
    
        
def atack(i):
    mag = 20
    swd= 30
    flc = 15
    magprob = [0,0,0,1,1,1]
    swdprob = [1,1,0,1,1]
    flcprob = [1,0,1,0,0,1,1,2]
    
    
    #for x in range(20):
    #print("")
    if i == "1":
        m = random.choice(magprob)
        if m == 1:
            return (mag)
        else:
            print("errou o golpe!")
            return (0)
    if i == "2":
        s = random.choice(swdprob)
        if s == 1:
            return (swd)
        if s == 2:
            print("Crítico!!!")
            return (swd*2)
        else:
            print("errou o golpe!")
            return (0)
    if i == "3":
        f = random.choice(flcprob)
        if f == 1:
            return (flc)
        if f == 2:
            print("Crítico!!!")
            return (flc*4)
        else:
            print("errou o golpe!")
            return (0)
    if i == "4":
        if heal <=0:
            print("Curas insuficientes!")
            return (0)
        else: 
            print("50 de vida curados")
            
            return(50)
    else:
        print("Comando inválido!")
        
        
        
def playSound():
    if mon == 1:
        d.mediaPlay('/storage/emulated/0/python/monster/audio/beast.m4a',)
    if mon == 3:
        d.mediaPlay('/storage/emulated/0/python/monster/audio/b2.mp3')
        
def stopSound():
    d.mediaPlayClose()
    
    
def ler_dados(id):
    if id == 1:
        arq = open('/storage/emulated/0/python/monster/res/demon.txt','r',)
        res =arq.read().splitlines()
        for linha in res : print (linha)
        arq.close() 
    if id == 2:
        arq = open('/storage/emulated/0/python/monster/res/instructions.txt','r',)
        res =arq.read().splitlines()
        for linha in res : print (linha)
        arq.close()     
    if id == 3:       
        arq = open('/storage/emulated/0/python/monster/res/rabbit.txt','r',)
        res =arq.read().splitlines()
        for linha in res : print (linha)
        arq.close()
    
    
        
def mon_atk():
    if mon ==1:
        
        monster = 40
        lista =[1,1,0,1,2,2]
        result = random.choice(lista)
        if result == 1:
            d.vibrate()
            return(monster)
        if result == 2:
            d.vibrate()
            print("você recebeu um golpe crítico")
            return (monster*2)
        else:
            return(0)
    if mon ==3:
        
        monster = 5
        lista =[1,0,0,0,0,0,0,1,2]
        result = random.choice(lista)
        if result == 1:
            d.vibrate()
            return(monster)
        if result == 2:
            d.vibrate()
            print("você recebeu um golpe crítico")
            return (monster*2)
        else:
            return(0)
def state():
    if vida <= 0:
        print("Você morreu!")
        stopSound()
        return(False)
    if life <= 0:
        print("Você venceu! Yayyyy")
        stopSound()
        return(False)

    
stopSound()
while True:
    menuOpcao =menu()
    if menuOpcao == "2":
        ler_dados(2)
        continue
    #playSound()
    while True:
        ler_dados(mon)
        print("Monster: ", life,"     HP: ",vida, " Curas: ",heal)
        print("\n")
        print("Magia [1]  Espada [2]  Arco [3]  Cura [4]")
        i= input("Opcao: ") 
        op= atack(i)
        if op ==50:
            vida+=50
            heal-=1
        else:
            life -=op
        atk= mon_atk()
        vida -=atk
       
        if state() == False:
            if vida<=0:
                break
            print("")
            time.sleep(1)
            print("Agora um desafio melhor :)")
            mon=1
            life =2000
            print("Preparado?")
            time.sleep(3)
            time.sleep(1)
            d.vibrate()
            print("3!")
            time.sleep(1)
            d.vibrate()
            print("2!")
            d.vibrate()
            time.sleep(1)
            print ("1!")
            time.sleep(1)
            playSound()
            
        
       