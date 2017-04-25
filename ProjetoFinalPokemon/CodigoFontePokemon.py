import random
import json
import os
with open('DicionarioPokemons.json') as arquivo: #NO DICIONARIO OS STATUS BASE DOS POKEMONS ESTAO ORGANIZADOS EM [HP,ATAQUE,DEFESA,ATAQUE ESPECIAL,DEFESA ESPECIAL,VELOCIDADE,LEVEL BASE, NIVEL DE EVOLUÇÃO(POKEMONS QUE NAO EVOLUEM TEM VALOR 200 QUE É MAIOR QUE O LEVEL MAXIMO),NIVEIS OBTIDOS POR MATAR ESSE POKEMON]
	DicPKM=json.load(arquivo)
with open('ListaPokemonString.json') as arquivo1:
	PKMstr=json.load(arquivo1)
#___________________________________________________________________________________________________________________________________#

#                                                                 #VARIAVEIS#
PokeBelt=[]
Golpe=random.randint(40,80)#A FORÇA DE CADA GOLPE VAI DE 40 A 80
IVsPokebelt=[]
StatusPKMBatalha=[]
ID=[]
#___________________________________________________________________________________________________________________________________#

#                                                           #DEFINIÇÃO DAS FUNÇÕES#
def GeraNovaListaDeStats(PosiçãoNoPokebelt):#Gera uma nova lista de status se necessário
	return ([int(FunçãoHPpokebelt(PosiçãoNoPokebelt,IVsPokebelt[PosiçãoNoPokebelt][0])),int(FunçãoOutrosStatsPokebelt(PosiçãoNoPokebelt,1,IVsPokebelt[PosiçãoNoPokebelt][1])),int(FunçãoOutrosStatsPokebelt(PosiçãoNoPokebelt,2,IVsPokebelt[0][2])),int(FunçãoOutrosStatsPokebelt(PosiçãoNoPokebelt,3,IVsPokebelt[0][3])),int(FunçãoOutrosStatsPokebelt(PosiçãoNoPokebelt,4,IVsPokebelt[0][4])),int(FunçãoOutrosStatsPokebelt(PosiçãoNoPokebelt,5,IVsPokebelt[0][5])),int(StatusTodosPKM[PosiçãoNoPokebelt][6])])
def captura(Max_HP,HP):#AS FORMULA UTILIZADAS ESTÃO DE ACORDO COM O ALGORITIMO DO JOGO ORIGINAL, POR ISSO SÃO UM POUCO COMPLEXAS
	#45 é o catch rate padrão padrão escolhido por mim
	treme=False
	CatchValue = (3*Max_HP-2*HP)*(45)/(3*Max_HP)
	if CatchValue>=255:
		Captura=True
	else:
		Catch=(1048560)/((16711680/CatchValue)**(1/2))**(1/2)
		ValorRandomico=random.randint(0,65535)
		if Catch>ValorRandomico:
			treme=True
			print ("Tremeu Uma Vez!")
		else:
			treme=False
		Catch=(1048560)/((16711680/CatchValue)**(1/2))**(1/2)
		ValorRandomico=random.randint(0,65535)
		if treme==True:
			if Catch>ValorRandomico:
				treme=True
				print ("Tremeu Duas Vezes!")
			else:
				treme=False
		Catch=(1048560)/((16711680/CatchValue)**(1/2))**(1/2)
		ValorRandomico=random.randint(0,65535)	
		if treme==True:
			if Catch>ValorRandomico:
				treme=True
				print ("Tremeu Três Vezes!")
			else:
				treme=False
		Catch=(1048560)/((16711680/CatchValue)**(1/2))**(1/2)
		ValorRandomico=random.randint(0,65535)
		if treme==True:
			if Catch>ValorRandomico:
				Captura=True
				print ("Capturou!!!")
			else:
				treme=False
		if treme==False:
			Captura=False
			print ("O Pokemon fugiu.....")
	return Captura
def levelpokemonselvagem(LevelSeusPokemons):
	Level=LevelSeusPokemons-(random.randint(-1,3))
	return Level#OS POKEMONS SELVAGENS PRECISAVAM DE UM LIMITADOR DE LEVEIS
def evolução():#CHECA SE O POKEMON JA ESTA NO NIVEL QUE ELE DEVE EVOLUIR, SE SIM ELE EVOLUI
	LevelPKM=DicPKM[PokeBelt[PokemonUtilizado]][6]
	LevelEvolução=DicPKM[PokeBelt[PokemonUtilizado]][7]
	if LevelPKM>=LevelEvolução:
		for i in range(len(PKMstr)):
			if PKMstr[i]==PokeBelt[PokemonUtilizado]:
				if PokeBelt[PokemonUtilizado]=="Eevee":#O pokemon Eevee possui tres evoluções diferentes
					NovoPokemon=PKMstr[random.randint(1,3)+i]
				else:
					NovoPokemon=PKMstr[1+i]
				print ("Seu {0} evoluiu para um {1}!!!".format(PokeBelt[PokemonUtilizado],NovoPokemon))
				BulianoEvolução=True
	else:
		NovoPokemon=PokeBelt[PokemonUtilizado]
		BulianoEvolução=False
	return (NovoPokemon,BulianoEvolução)
def FunçãoHPpokebelt(PosiçãoNoPokebelt,IV):#GERA OHP DO POKEMON QUE VAI SER USADO NA BATALHA(DE ACORDO COM A FORMULA ORIGINAL DO JOGO)
	FHPPb=(((2*(DicPKM[PokeBelt[PosiçãoNoPokebelt]][0])+(IV))*DicPKM[PokeBelt[PosiçãoNoPokebelt]][6])/100)+DicPKM[PokeBelt[PosiçãoNoPokebelt]][6]+10  #zero pq o pokebelt só tem 1 pokemon 50 pelo nivel
	#print (FHPPb)
	return FHPPb
def FunçãoOutrosStatsPokebelt(PosiçãoNoPokebelt,Stat,IV):#GERA TODOS OS OUTROS STATUS DO POKEMON QUE VAI SER USADO NA BATALHA(DE ACORDO COM AS FORMULAS ORIGINAIS DO JOGO)
	FSTPb=(((2*(DicPKM[PokeBelt[PosiçãoNoPokebelt]])[Stat]+(IV))*DicPKM[PokeBelt[PosiçãoNoPokebelt]][6])/100)+5   #zero pq o pokebelt só tem 1 pokemon e 50 pelo nivel
	return FSTPb
def FunçãoHPSelvagem(PKMS):#GERA O HP DOS POKEMONS SELVAGENS(DE ACORDO COM AS FORMULAS ORIGINAIS DO JOGO)
	FHPS=(((2*(DicPKM[PKMS])[0]+(random.randint(0,31)))*(DicPKM[PKMS][6]-random.randint(0,3)))/100)+DicPKM[PKMS][6]-random.randint(0,5)+10  #zero pq o pokebelt só tem 1 pokemon 50 pelo nivel
	return FHPS
def FunçãoOutrosStatsSelvagem(PKMS,Stat):#GERA OS STATUS DOS POKEMONS SELVAGENS(DE ACORDO COM AS FORMULAS ORIGINAIS DO JOGO)
	FSTS=(((2*(DicPKM[PKMS])[Stat]+random.randint(0,31))*DicPKM[PKMS][6])/100)+5
	return FSTS
def FunçãoDanoCalculado(AtkAgro,DefVitima,Golpe,LevelAtacante):#CALCULA O DANO CAUSADO APÓS UM ATAQUE(COM AS FORMULAS ORIGINAIS)
	Damage = ((((2*LevelAtacante/5+2)*AtkAgro*Golpe/DefVitima)/50)+2)*random.randint(85,100)/(100)#*STAB*Weakness/Resistance
	return Damage
def Batalha():#RODA AS AÇÕES DE BATALHAS COM O FATOR VELOCIDADE-POKEMON MAIS RÁPIDO SEMPRE ATACA PRIMEIRO-E COM POSSIBILIDADE DE GOLPES FISICOS OU A DISTANCIA
	AçãoNaBatalha=int(input("O que fazer?\nAtacar(1), Fugir(0), Tentar Capturar(2)"))
	os.system('cls')
	if AçãoNaBatalha==1:
		TipoDoGolpe=int(input("Usar um golpe Fisico(0) ou um Golpe Distância(1)?"))
		os.system('cls')
		if TipoDoGolpe==0:
			if StatusPKMBatalhaSelvagem[5] <= StatusPKMBatalha[5]:#Caso em que seu pokemon é mais rápido
				DeltaHPS=int(FunçãoDanoCalculado(StatusPKMBatalha[1],StatusPKMBatalhaSelvagem[2],Golpe,StatusPKMBatalha[6]))
				StatusPKMBatalhaSelvagem[0]=StatusPKMBatalhaSelvagem[0]-DeltaHPS
				print ( "Seu {0} causou {1} de dano!".format(PokeBelt[PokemonUtilizado],DeltaHPS))
				if StatusPKMBatalhaSelvagem[0] >0:#Se o pokemon que atacou primeiro matar o adverssário, este não ataca
								DeltaHPPb=int(FunçãoDanoCalculado(StatusPKMBatalhaSelvagem[1],StatusPKMBatalha[2],Golpe,StatusPKMBatalhaSelvagem[6]))
								StatusPKMBatalha[0]=StatusPKMBatalha[0]-DeltaHPPb
								print ( "O {0} selvagem causou {1} de dano!".format(Pokemon_Selvagem,DeltaHPPb))
			if StatusPKMBatalhaSelvagem[5] > StatusPKMBatalha[5]:#Caso em que seu pokemon é mais devagar
				DeltaHPPb=int(FunçãoDanoCalculado(StatusPKMBatalhaSelvagem[1],StatusPKMBatalha[2],Golpe,StatusPKMBatalhaSelvagem[6]))
				StatusPKMBatalha[0]=StatusPKMBatalha[0]-DeltaHPPb
				print ( "O {0} selvagem causou {1} de dano!".format(Pokemon_Selvagem,DeltaHPPb))
				if StatusPKMBatalha[0]>0:#Se o pokemon que atacou primeiro matar o adverssário, este não ataca
								   DeltaHPS=int(FunçãoDanoCalculado(StatusPKMBatalha[1],StatusPKMBatalhaSelvagem[2],Golpe,StatusPKMBatalha[6]))
								   StatusPKMBatalhaSelvagem[0]=StatusPKMBatalhaSelvagem[0]-DeltaHPS
								   print ( "Seu {0} causou {1} de dano!".format(PokeBelt[PokemonUtilizado],DeltaHPS))
			print ("Seu {0} ficou com {1} de vida!".format(PokeBelt[PokemonUtilizado],StatusPKMBatalha[0]))
			print ("O {0} selvagem ficou com {1} de vida!".format(Pokemon_Selvagem,StatusPKMBatalhaSelvagem[0])) 
			if StatusPKMBatalhaSelvagem[0]<0:
					StatusPKMBatalhaSelvagem[0]=0
			if StatusPKMBatalha[0]<0:
					StatusPKMBatalha[0]=0
					print (AçãoNaBatalha,StatusPKMBatalhaSelvagem[0],StatusPKMBatalha[0])                                                                                                
			return (AçãoNaBatalha,StatusPKMBatalhaSelvagem[0],StatusPKMBatalha[0])
		if TipoDoGolpe==1:
			if StatusPKMBatalhaSelvagem[5] <= StatusPKMBatalha[5]:#Caso em que seu pokemon é mais rápido
				DeltaHPS=int(FunçãoDanoCalculado(StatusPKMBatalha[3],StatusPKMBatalhaSelvagem[4],Golpe,StatusPKMBatalha[6]))
				StatusPKMBatalhaSelvagem[0]=StatusPKMBatalhaSelvagem[0]-DeltaHPS
				print ( "Seu {0} causou {1} de dano!".format(PokeBelt[0],DeltaHPS))
				if StatusPKMBatalhaSelvagem[0] >0:#Caso em que seu pokemon é mais devagar
								DeltaHPPb=int(FunçãoDanoCalculado(StatusPKMBatalhaSelvagem[3],StatusPKMBatalha[4],Golpe,StatusPKMBatalhaSelvagem[6]))
								StatusPKMBatalha[0]=StatusPKMBatalha[0]-DeltaHPPb
								print ( "O {0} selvagem causou {1} de dano!".format(Pokemon_Selvagem,DeltaHPPb))
			if StatusPKMBatalhaSelvagem[5] > StatusPKMBatalha[5]:
				DeltaHPPb=int(FunçãoDanoCalculado(StatusPKMBatalhaSelvagem[3],StatusPKMBatalha[4],Golpe,StatusPKMBatalhaSelvagem[6]))
				StatusPKMBatalha[0]=StatusPKMBatalha[0]-DeltaHPPb
				print ( "O {0} selvagem causou {1} de dano!".format(Pokemon_Selvagem,DeltaHPPb))
				if StatusPKMBatalha[0]>0:
								   DeltaHPS=int(FunçãoDanoCalculado(StatusPKMBatalha[3],StatusPKMBatalhaSelvagem[4],Golpe,StatusPKMBatalha[6]))
								   StatusPKMBatalhaSelvagem[0]=StatusPKMBatalhaSelvagem[0]-DeltaHPS
								   print ( "Seu {0} causou {1} de dano!".format(PokeBelt[PokemonUtilizado],DeltaHPS))
			print ("Seu {0} ficou com {1} de vida!".format(PokeBelt[PokemonUtilizado],StatusPKMBatalha[0]))
			print ("O {0} selvagem ficou com {1} de vida!".format(Pokemon_Selvagem,StatusPKMBatalhaSelvagem[0])) 
			if StatusPKMBatalhaSelvagem[0]<0:
					StatusPKMBatalhaSelvagem[0]=0
			if StatusPKMBatalha[0]<0:
					StatusPKMBatalha[0]=0
					print (AçãoNaBatalha,StatusPKMBatalhaSelvagem[0],StatusPKMBatalha[0])                                                                                                
			return (AçãoNaBatalha,StatusPKMBatalhaSelvagem[0],StatusPKMBatalha[0])
	if AçãoNaBatalha==2:
		if captura(HPMaxPKMSelvagem,StatusPKMBatalhaSelvagem[0])==True:
			return (0,StatusPKMBatalhaSelvagem[0],StatusPKMBatalha[0],Pokemon_Selvagem)
		else:#Quando escapa da pokemonbola o pokemon tem 50% de chances de fugir da batalha
			vaifugir=random.randint(0,1)
			if vaifugir==0:
				print ("O pokemon fugiu para longe....")
				return (0,StatusPKMBatalhaSelvagem[0],StatusPKMBatalha[0])
			else:
				return (100,StatusPKMBatalhaSelvagem[0],StatusPKMBatalha[0])
	if AçãoNaBatalha==0:
			return	(0,StatusPKMBatalhaSelvagem[0],StatusPKMBatalha[0])
def FunçãoIV():#GERA OS IV DE CADA POKEMON(VALORSS RANDOMICOS DE 0 A 31 QUE SÃO USADOS PARA CALCULAR OS ATRIBUTOS DE CADA POKEMON)
	return (random.randint(0,31))
def PokeCenter(PosiçãoNoPokebelt):#RECUPERA A VIDA DE TODOS OS POKEMONS DO JOGADDR
	print ("♪♫Tan Tan tananan♪♫")
	ListaIvPokecenter=(IVsPokebelt[PosiçãoNoPokebelt])
	StatusPKMBatalha[0]=int(FunçãoHPpokebelt(PosiçãoNoPokebelt,ListaIvPokecenter[0]))
def InsperDex():#PRINTA A INPERDEX COM TODOS OS POKEMONS JÁ ENCONTRADOS
	print ("InsperDex")
	Numero=1
	for NID in sorted(set(ID)):
		print ("{0}-{1}".format(Numero,NID))
		Numero=Numero+1
#____________________________________________________________________________________________________________________________________#
#                                                      #INTRODUÇÃO E ESCOLHA DO INICIAL#
os.system('cls')
StartMenu=int(input("Você deseja carregar algum jogo?\n Sim(0)\n Não(1)"))
if StartMenu==0:#Faz o Load do Jogo
	Nome_do_File=input("Qual o nome do load?")
	with open('{}ID'.format(Nome_do_File)) as IDload:
		ID=json.load(IDload)
	with open('{}IVsPokebelt'.format(Nome_do_File)) as IVsPokebeltLoad:
		IVsPokebelt=json.load(IVsPokebeltLoad)
	with open('{}IVsPokebelt'.format(Nome_do_File)) as StatusTodosPKMLoad:
		StatusTodosPKM=json.load(StatusTodosPKMLoad)
	with open('{}PokeBelt'.format(Nome_do_File)) as PokeBeltLoad:
		PokeBelt=json.load(PokeBeltLoad)
	with open('{}Player'.format(Nome_do_File)) as PlayerLoad:
		Nome_jogador=json.load(PlayerLoad)
	DesculpaLuciano=False
else:
	print ("Bem vindo ao incrível mundo de inspermon! Eu sou o Professor Sequoia!")
	Nome_jogador=input("Qual seu nome? \n")
	os.system('cls')
	print ("Muito bem, {0}! Agora escolha um pokemon!" .format(Nome_jogador))
	PokemonInicial= int(input(" 0-Bulbasaur\n 1-Charmander\n 2-Squirtle\n"))
	os.system('cls')
	while PokemonInicial >= 3:
		PokemonInicial= int(input(" 0-Bulbasaur\n 1-Charmander\n 2-Squirtle\n "))
	if PokemonInicial==1:
		print ("Por quê eu ainda pergunto....")
		PokemonInicial=132
	if PokemonInicial==0 or PokemonInicial==2:
		print("Então você escolhe o charm...")
		print("Bom a escolha é sua. Boa sorte no mundo sem um charizard.")
		if PokemonInicial==2:
			PokemonInicial=6
	PokeBelt.append(PKMstr[PokemonInicial])
	IVsPokebelt.append([FunçãoIV(),FunçãoIV(),FunçãoIV(),FunçãoIV(),FunçãoIV(),FunçãoIV()])
	ID.append(PokeBelt[0])
	DesculpaLuciano=True 

#__________________________________________________________________________________________________________________________________#
#     
O_que_fazer=100
#                                              #COMEÇO DOS LOOPINGS#
os.system('cls')
while O_que_fazer !=int(4):
	O_que_fazer=int(input("O que você que fazer agora,{0}?\n Ir batalhar(0)\n Visitar o centro pokemon(1)\n Abrir a InsperDex(2)\n Salvar(3)\n Sair(4)\n " .format(Nome_jogador)))
	os.system('cls')
	if O_que_fazer==1:
		for i in range (len(PokeBelt)):
			PokeCenter(i)
	if O_que_fazer==0:
		for i in range(len(PokeBelt)):
			print (i+1)
			print (PokeBelt[i])
		PokemonUtilizado=int(input("Qual a posição do pokemon você quer utilizar?"))-1
		if DesculpaLuciano==True:#Faz os status do primeiro pokemon(só pode acontecer uma vez por "save")
			StatusTodosPKM=[[int(FunçãoHPpokebelt(PokemonUtilizado,IVsPokebelt[PokemonUtilizado][0])),int(FunçãoOutrosStatsPokebelt(PokemonUtilizado,1,IVsPokebelt[PokemonUtilizado][1])),int(FunçãoOutrosStatsPokebelt(PokemonUtilizado,2,IVsPokebelt[PokemonUtilizado][2])),int(FunçãoOutrosStatsPokebelt(PokemonUtilizado,3,IVsPokebelt[PokemonUtilizado][3])),int(FunçãoOutrosStatsPokebelt(PokemonUtilizado,4,IVsPokebelt[PokemonUtilizado][4])),int(FunçãoOutrosStatsPokebelt(PokemonUtilizado,5,IVsPokebelt[PokemonUtilizado][5])),int(DicPKM[PokeBelt[PokemonUtilizado]][6])]]
			DesculpaLuciano==False
		StatusPKMBatalha=GeraNovaListaDeStats(PokemonUtilizado)
		print ("♫Tan tan tan tan tan tan tanana nanan nan tanana nana nan turu....♫")
		Gerador_PKM_Selvagem= random.randint(0,148)#Gera o pokemon selvagem de acordo com a lista dos pokemons em string
		Pokemon_Selvagem=PKMstr[Gerador_PKM_Selvagem]
		ID.append(Pokemon_Selvagem)
#		Faz os status do pokemon selvagem resgatando valores no dicionário
		StatusPKMBatalhaSelvagem=[int(FunçãoHPSelvagem(Pokemon_Selvagem)),int(FunçãoOutrosStatsSelvagem(Pokemon_Selvagem,1)),int(FunçãoOutrosStatsSelvagem(Pokemon_Selvagem,2)),int(FunçãoOutrosStatsSelvagem(Pokemon_Selvagem,3)),int(FunçãoOutrosStatsSelvagem(Pokemon_Selvagem,4)),int(FunçãoOutrosStatsSelvagem(Pokemon_Selvagem,5)),int(levelpokemonselvagem(StatusPKMBatalha[6]))]
		HPMaxPKMSelvagem=StatusPKMBatalhaSelvagem[0]
		print ("Um {0} selvagem level {1} apareceu!!!!".format(Pokemon_Selvagem,StatusPKMBatalhaSelvagem[6]))
		AçãoNaBatalha=100
		while StatusPKMBatalhaSelvagem[0] != 0 and StatusPKMBatalha[0]!=0 and AçãoNaBatalha!=0:
					HPPosBatalha=Batalha()
					#print (HPPosBatalha)
					AçãoNaBatalha=int(HPPosBatalha[0])
					StatusPKMBatalhaSelvagem[0]=int(HPPosBatalha[1])
					StatusPKMBatalha[0]=int(HPPosBatalha[2])
					if StatusPKMBatalha[0]==0:
										print ("Você perdeu....")
					if StatusPKMBatalhaSelvagem[0]==0:
										print ("Você Ganhou!!!")
										if DicPKM[PokeBelt[PokemonUtilizado]][6]<100:
											DicPKM[PokeBelt[PokemonUtilizado]][6]=DicPKM[PokeBelt[PokemonUtilizado]][6]+DicPKM[Pokemon_Selvagem][8]					
											print ("Seu {0} subiu para o level {1}".format(PokeBelt[PokemonUtilizado],DicPKM[PokeBelt[PokemonUtilizado]][6]))
					if len(HPPosBatalha)==4:
						PokeBelt.append(HPPosBatalha[3])
						IVsPokebelt.append([FunçãoIV(),FunçãoIV(),FunçãoIV(),FunçãoIV(),FunçãoIV(),FunçãoIV()])
						StatusTodosPKM.append(StatusPKMBatalhaSelvagem)
	if O_que_fazer==3:#Carrega o jogo previamente salvo de acordo com o nome usado na hora que se salvou.
		Nome_do_Save=input("Qual o nome do sabe?")
		with open('{}ID'.format(Nome_do_Save), 'w') as outfile:
			json.dump(ID,outfile)
		with open('{}IVsPokebelt'.format(Nome_do_Save), 'w') as outfile:
			json.dump(IVsPokebelt, outfile)  		
		with open('{}StatusTodosPKM'.format(Nome_do_Save), 'w') as outfile:
			json.dump(StatusTodosPKM,outfile)  		
		with open('{}PokeBelt'.format(Nome_do_Save), 'w') as outfile:
			json.dump(PokeBelt,outfile)
		with open('{}Player'.format(Nome_do_Save), 'w') as outfile:
			json.dump(Nome_jogador,outfile)
	if O_que_fazer !=2: #PARTE DO CÓDIGO EM QUE É IMPLEMENTADA A FUNÇÃO DA EVOLUÇÃO
		PokeBelt[PokemonUtilizado]=evolução()[0]
		if evolução()[1]==True:
			StatusTodosPKM[PokemonUtilizado]=GeraNovaListaDeStats[PokemonUtilizado]
			StatusTodosPKM[PokemonUtilizado][7]=DicPKM[Pokemon_Selvagem][8]
	if O_que_fazer == 2:
		InsperDex()
		SairInsperDex=input()
