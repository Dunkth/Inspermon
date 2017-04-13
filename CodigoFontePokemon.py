import random
import json
import os
with open('DicionarioPokemons.json') as arquivo: 
	DicPKM=json.load(arquivo)
with open('ListaPokemonString.json') as arquivo1:
	PKMstr=json.load(arquivo1)
#___________________________________________________________________________________________________________________________________#

#                                                                 #VARIAVEIS#
PokeBelt=[]
Golpe=30
HPCheioPokeBelt=[]
#___________________________________________________________________________________________________________________________________#

#                                                           #DEFINIÇÃO DAS FUNÇÕES#
def FunçãoHPpokebelt():
	FHPPb=(((2*(DicPKM[PokeBelt[0]][0])+(random.randint(0,31)))*DicPKM[PokeBelt[0]][6])/100)+DicPKM[PokeBelt[0]][6]+10  #zero pq o pokebelt só tem 1 pokemon 50 pelo nivel
	#print (FHPPb)
	return FHPPb
def FunçãoOutrosStatsPokebelt(Stat):
	FSTPb=(((2*(DicPKM[PokeBelt[0]])[Stat]+(random.randint(0,31)))*DicPKM[PokeBelt[0]][6])/100)+5   #zero pq o pokebelt só tem 1 pokemon e 50 pelo nivel
	#print(FSTPb)
	return FSTPb
def FunçãoHPSelvagem(PKMS):
	FHPS=(((2*(DicPKM[PKMS])[0]+(random.randint(0,31)))*(DicPKM[PokeBelt[0]][6]-random.randint(0,3)))/100)+DicPKM[PokeBelt[0]][6]-random.randint(0,5)+10  #zero pq o pokebelt só tem 1 pokemon 50 pelo nivel
	if DicPKM[PokeBelt[0]][6]<=3:
		FHPS=(((2*(DicPKM[PKMS])[0]+(random.randint(0,31)))*(DicPKM[PokeBelt[0]][6]))/100)+DicPKM[PokeBelt[0]][6]+10
	#print (FHPS)
	return FHPS
def FunçãoOutrosStatsSelvagem(PKMS,Stat):
	FSTS=(((2*(DicPKM[PKMS])[Stat]+(random.randint(0,31)))*(DicPKM[PokeBelt[0]][6]-random.randint(0,3)))/100)+5   #zero pq o pokebelt só tem 1 pokemon e 50 pelo nivel
	if DicPKM[PokeBelt[0]][6]<=3:
		FSTS=(((2*(DicPKM[PKMS])[Stat]+(random.randint(0,31)))*(DicPKM[PokeBelt[0]][6]))/100)+5
	#print (FSTS)
	return FSTS
def FunçãoDanoCalculado(AtkAgro,DefVitima,Golpe):
	Damage = ((((2*50/5+2)*AtkAgro*Golpe/DefVitima)/50)+2)*random.randint(85,100)/(100)#*STAB*Weakness/Resistance
#                  ^^
#            Nível do pokemon que ataca
	return Damage
def Batalha():
	AçãoNaBatalha=int(input("O que fazer?\nAtacar(1), Fugir(0)"))
	os.system('cls')
	if AçãoNaBatalha==1:
		TipoDoGolpe=int(input("Usar um golpe Fisico(0) ou um Golpe Distância(1)?"))
		if TipoDoGolpe==0:
			if StatusPKMBatalhaSelvagem[5] <= StatusPKMBatalha[5]:
				DeltaHPS=int(FunçãoDanoCalculado(StatusPKMBatalha[1],StatusPKMBatalhaSelvagem[2],Golpe))
				StatusPKMBatalhaSelvagem[0]=StatusPKMBatalhaSelvagem[0]-DeltaHPS
				print ( "Seu {0} causou {1} de dano!".format(PokeBelt[0],DeltaHPS))
				if StatusPKMBatalhaSelvagem[0] >0:
								DeltaHPPb=int(FunçãoDanoCalculado(StatusPKMBatalhaSelvagem[1],StatusPKMBatalha[2],Golpe))
								StatusPKMBatalha[0]=StatusPKMBatalha[0]-DeltaHPPb
								print ( "O {0} selvagem causou {1} de dano!".format(Pokemon_Selvagem,DeltaHPPb))
			if StatusPKMBatalhaSelvagem[5] > StatusPKMBatalha[5]:
				DeltaHPPb=int(FunçãoDanoCalculado(StatusPKMBatalhaSelvagem[1],StatusPKMBatalha[2],Golpe))
				StatusPKMBatalha[0]=StatusPKMBatalha[0]-DeltaHPPb
				print ( "O {0} selvagem causou {1} de dano!".format(Pokemon_Selvagem,DeltaHPPb))
				if StatusPKMBatalha[0]>0:
								   DeltaHPS=int(FunçãoDanoCalculado(StatusPKMBatalha[1],StatusPKMBatalhaSelvagem[2],Golpe))
								   StatusPKMBatalhaSelvagem[0]=StatusPKMBatalhaSelvagem[0]-DeltaHPS
								   print ( "Seu {0} causou {1} de dano!".format(PokeBelt[0],DeltaHPS))
			print ("Seu {0} ficou com {1} de vida!".format(PokeBelt[0],StatusPKMBatalha[0]))
			print ("O {0} selvagem ficou com {1} de vida!".format(Pokemon_Selvagem,StatusPKMBatalhaSelvagem[0])) 
			if StatusPKMBatalhaSelvagem[0]<0:
					StatusPKMBatalhaSelvagem[0]=0
			if StatusPKMBatalha[0]<0:
					StatusPKMBatalha[0]=0
		if TipoDoGolpe==1:
			if StatusPKMBatalhaSelvagem[5] <= StatusPKMBatalha[5]:
				DeltaHPS=int(FunçãoDanoCalculado(StatusPKMBatalha[3],StatusPKMBatalhaSelvagem[4],Golpe))
				StatusPKMBatalhaSelvagem[0]=StatusPKMBatalhaSelvagem[0]-DeltaHPS
				print ( "Seu {0} causou {1} de dano!".format(PokeBelt[0],DeltaHPS))
				if StatusPKMBatalhaSelvagem[0] >0:
								DeltaHPPb=int(FunçãoDanoCalculado(StatusPKMBatalhaSelvagem[3],StatusPKMBatalha[4],Golpe))
								StatusPKMBatalha[0]=StatusPKMBatalha[0]-DeltaHPPb
								print ( "O {0} selvagem causou {1} de dano!".format(Pokemon_Selvagem,DeltaHPPb))
			if StatusPKMBatalhaSelvagem[5] > StatusPKMBatalha[5]:
				DeltaHPPb=int(FunçãoDanoCalculado(StatusPKMBatalhaSelvagem[3],StatusPKMBatalha[4],Golpe))
				StatusPKMBatalha[0]=StatusPKMBatalha[0]-DeltaHPPb
				print ( "O {0} selvagem causou {1} de dano!".format(Pokemon_Selvagem,DeltaHPPb))
				if StatusPKMBatalha[0]>0:
								   DeltaHPS=int(FunçãoDanoCalculado(StatusPKMBatalha[3],StatusPKMBatalhaSelvagem[4],Golpe))
								   StatusPKMBatalhaSelvagem[0]=StatusPKMBatalhaSelvagem[0]-DeltaHPS
								   print ( "Seu {0} causou {1} de dano!".format(PokeBelt[0],DeltaHPS))
			print ("Seu {0} ficou com {1} de vida!".format(PokeBelt[0],StatusPKMBatalha[0]))
			print ("O {0} selvagem ficou com {1} de vida!".format(Pokemon_Selvagem,StatusPKMBatalhaSelvagem[0])) 
			if StatusPKMBatalhaSelvagem[0]<0:
					StatusPKMBatalhaSelvagem[0]=0
			if StatusPKMBatalha[0]<0:
					StatusPKMBatalha[0]=0
	#print (AçãoNaBatalha,StatusPKMBatalhaSelvagem[0],StatusPKMBatalha[0])                                                                                                
	return (AçãoNaBatalha,StatusPKMBatalhaSelvagem[0],StatusPKMBatalha[0])
def PokeCenter():
	print ("♪♫Tan Tan tananan♪♫") 
	StatusPKMBatalha[0]=DicPKM[PokeBelt[0]][0]
#____________________________________________________________________________________________________________________________________#
#                                                      #INTRODUÇÃO E ESCOLHA DO INICIAL#

print ("Bem vindo ao incrível mundo de inspermon! Eu sou o Professor Sequoia!")
Nome_jogador=input("Qual seu nome?")
os.system('cls')
print ("Muito bem, {0}! Agora escolha um pokemon!" .format(Nome_jogador))
PokemonInicial= int(input("0-Bulbasaur\n1-Charmander\n2-Squirtle"))
os.system('cls')
while PokemonInicial >= 3:
	PokemonInicial= int(input("0-Bulbasaur\n1-Charmander\n2-Squirtle"))
if PokemonInicial==1:
	print ("Por quê eu ainda pergunto....")
if PokemonInicial==0 or PokemonInicial==2:
	print("Então você escolhe o charm...")
	print("Bom a escolha é sua. Boa sorte no mundo sem um charizard.")
PokeBelt.append(PKMstr[PokemonInicial])
HPCheioPokeBelt.append((PokeBelt[0])[0])
#__________________________________________________________________________________________________________________________________#
#     
O_que_fazer=100
x=0                                                   #COMEÇO DOS LOOPINGS#
while O_que_fazer !=int(2):
	O_que_fazer=int(input("O que você que fazer agora,{0}? Ir batalhar(0) , visitar o centro pokemon(1) , sair(2)" .format(Nome_jogador)))
	os.system('cls')
	if O_que_fazer==1:
		PokeCenter()
	if O_que_fazer==0:
		if x==0:
			StatusPKMBatalha=[int(FunçãoHPpokebelt()),int(FunçãoOutrosStatsPokebelt(1)),int(FunçãoOutrosStatsPokebelt(2)),int(FunçãoOutrosStatsPokebelt(3)),int(FunçãoOutrosStatsPokebelt(4)),int(FunçãoOutrosStatsPokebelt(5)),int(FunçãoOutrosStatsPokebelt(6))]
			x=x+1
		print ("♫Tan tan tan tan tan tan tanana nanan nan tanana nana nan turu....♫")
		Gerador_PKM_Selvagem= random.randint(0,4)
		Pokemon_Selvagem=PKMstr[Gerador_PKM_Selvagem]
		StatusPKMBatalhaSelvagem=[int(FunçãoHPSelvagem(Pokemon_Selvagem)),int(FunçãoOutrosStatsSelvagem(Pokemon_Selvagem,1)),int(FunçãoOutrosStatsSelvagem(Pokemon_Selvagem,2)),int(FunçãoOutrosStatsSelvagem(Pokemon_Selvagem,3)),int(FunçãoOutrosStatsSelvagem(Pokemon_Selvagem,4)),int(FunçãoOutrosStatsSelvagem(Pokemon_Selvagem,5)),int(FunçãoOutrosStatsSelvagem(Pokemon_Selvagem,6))]
		print ("Um {0} selvagem level {1} apareceu!!!!".format(Pokemon_Selvagem,StatusPKMBatalhaSelvagem[6]))
		AçãoNaBatalha=100
		while StatusPKMBatalhaSelvagem[0] != 0 and StatusPKMBatalha[0]!=0 and AçãoNaBatalha!=0:
					HPPosBatalha=Batalha()
					print (HPPosBatalha)
					AçãoNaBatalha=int(HPPosBatalha[0])
					StatusPKMBatalhaSelvagem[0]=int(HPPosBatalha[1])
					StatusPKMBatalha[0]=int(HPPosBatalha[2])
					if StatusPKMBatalha[0]==0:
										print ("Você perdeu....")
					if StatusPKMBatalhaSelvagem[0]==0:
										print ("Você Ganhou!!!")
										if DicPKM[PokeBelt[0]][6]<100:
                                                                                        DicPKM[PokeBelt[0]][6]=DicPKM[PokeBelt[0]][6]+1
                                                                                        print ("Seu {0} subiu para o level {1}".format(PokeBelt[0],DicPKM[PokeBelt[0]][6]))


