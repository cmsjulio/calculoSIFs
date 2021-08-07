#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys 						#para emitir mensagens de erro quando houver não conformidade
import numpy as np 				#para os cálculos
import matplotlib.pyplot as plt		#para os gráficos

plt.rcParams.update({'font.size' : 14}) 	#aumentando o tamanho da fonte dos gráficos

def plotH():
	nps=np.array(['10', '14', '18', '24'])
	T=np.array([9.27, 11.13, 14.27, 17.48])
	D_o=np.array([273, 355.6, 457, 610])
	t_p=T
	
	R=(D_o-T)/2
	
	#tê segundo ASME B16.9
	h21=3.1*(T/R)
	
	#boca de lobo com reforço
	h22=((T+t_p/2)**2.5)/(T**1.5*R)
	
	#boca de lobo sem reforço
	h23=T/R

		
	#CARACTERISTICA DE FLEXIBILIDADE
	fig = plt.figure (31, figsize=(6,6))
	plt.plot(nps, h21, marker='o', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$h -$ Tê conforme ASME B16.9')
	plt.xlabel('NPS')
	plt.ylabel('Característica. de flexibilidade $(h) -$ Tê conforme ASME B16.9')
	plt.tight_layout(pad=1)
	plt.legend()
	plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/plotFatores/caso2.1H', format='eps')
	#plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
	
	fig = plt.figure (32, figsize=(6,6))
	plt.plot(nps, h22, marker='o', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$h -$ Boca de lobo com reforço')
	plt.xlabel('NPS')
	plt.ylabel('Característica de flexibilidade $(h) -$ Boca de lobo com reforço')
	plt.tight_layout(pad=1)
	plt.legend()
	plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/plotFatores/caso2.2H', format='eps')
	#plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
	
	fig = plt.figure (33, figsize=(6,6))
	plt.plot(nps, h23, marker='o', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$h -$ Boca de lobo sem reforço')
	plt.xlabel('NPS')
	plt.ylabel('Característica de flexibilidade $(h) -$ Boca de lobo sem reforço')
	plt.tight_layout(pad=1)
	plt.legend()
	plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/plotFatores/caso2.3H', format='eps')
	#plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
	
	fig = plt.figure (34, figsize=(6,6))
	plt.plot(nps, h21, marker='o', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$h -$tê conforme ASME B16.9')
	plt.plot(nps, h22, marker='s', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$h -$boca de lobo com reforço')
	plt.plot(nps, h23, marker='x', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$h -$boca de lobo sem reforço')
	plt.xlabel('NPS')
	plt.ylabel('Característica de flexibilidade $(h)$')
	plt.tight_layout(pad=1)
	plt.legend(loc='center left')
	plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/plotFatores/caso2.4H', format='eps')
	#plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
	
def fatores2_1 (NPSin,Tin,D_oin,tin,d_oin, recursivo=True): #função que calcula fatores para tês curvados conforme ASME B16.9
		
	nps=NPSin

	T=Tin
	D_o=D_oin

	t=tin
	d_o=d_oin

	#obtendo parâmetros geométricos
	D=D_o-T
	d=d_o-t
	R=(D_o-T)/2
	r=(d_o-t)/2

	#check de conformidade com R/T<=50
	RsobreT=R/T
	for x in RsobreT:
		if x>50:
			sys.exit('Não conformidade com R/T<=50')

	#check de conformidade com d/D<=1
	dsobreD=d/D
	for x in dsobreD:
		if x>1:
			sys.exit('Não conformidade com d/D<=0')


	#check de conformidade com r/t<=50
	rsobret=r/t
	for x in rsobret:
		if x>50:
			sys.exit('Não conformidade com r/t<=50')
			

	#check de conformidade com t/T<=1.2
	tsobreT=t/T
	for x in tsobreT:
		if x>1.2:
			sys.exit('Não conformidade com t/T<=1.2')


	#--------------------- ITEM 2.1 --------------------#
	#---------------------- cálculo ----------------------#

	# fator de flexibilidade segundo ASME B31J (o Apêndice D não apresenta valores)
	
	#PRINCIPAL
	
	#no plano
	k_irJ=0.18*(R/T)**0.8*(d/D)**5
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_irJ):
		if k_irJ[count]<1:
			k_irJ[count]=1
		count=count+1


	#fora do plano=1, mas precisa criar lista da mesma dimensão com vários uns.
	k_orJ=(0*R)+1

	#torcional
	k_trJ=0.08*(R/T)**0.91*(d/D)**5.7
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_trJ):
		if k_trJ[count]<1:
			k_trJ[count]=1
		count=count+1

	#RAMAL

	#no plano
	k_ibJ=(1.91*(d/D)-4.32*(d/D)**2+2.7*(d/D)**3)*(R/T)**.77*(d/D)**.47*(t/T)
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_ibJ):
		if k_ibJ[count]<1:
			k_ibJ[count]=1
		count=count+1

	#fora do plano
	k_obJ=(0.34*(d/D)-0.49*(d/D)**2+0.18*(d/D)**3)*(R/T)**1.46*(t/T)
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_obJ):
		if k_obJ[count]<1:
			k_obJ[count]=1
		count=count+1

	#torcional
	k_tbJ=(1.08*(d/D)-2.44*(d/D)**2+1.52*(d/D)**3)*(R/T)**.77*(d/D)**1.61*(t/T)
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_tbJ):
		if k_tbJ[count]<1:
			k_tbJ[count]=1
		count=count+1

	#SIF conforme APÊNDICE D

	#carcaterística de flexibilidade
	h=3.1*(T/R)

	#SIF - principal e ramal são iguais
	#fora do plano
	i_orD=0.9/(h**(2/3))
	#nenhum SIF menor que 1
	count=0
	while count<len(i_orD):
		if i_orD[count]<1:
			i_orD[count]=1
		count=count+1
	i_obD=i_orD


	#no plano
	i_irD=(3/4)*(0.9/(h**(2/3)))+(1/4)
	#nenhum SIF menor que 1
	count=0
	while count<len(i_irD):
		if i_irD[count]<1:
			i_irD[count]=1
		count=count+1

	i_ibD=i_irD


	#torcional
	i_trD=np.array([1.0, 1, 1, 1])
	i_tbD=np.array([1.0, 1, 1, 1])

	#SIF conforme B31J
	#PRINCIPAL

	#no plano
	i_irJ=0.98*(R/T)**.35*(d/D)**.72*(t/T)**(-.52)
	#nenhum SIF menor que 1
	count=0
	while count<len(i_irJ):
		if i_irJ[count]<1:
			i_irJ[count]=1
		count=count+1

	#fora do plano
	i_orJ=0.61*(R/T)**(.29)*(d/D)**(1.95)*(t/T)**(-.53)
	#nenhum SIF menor que 1
	count=0
	while count<len(i_orJ):
		if i_orJ[count]<1:
			i_orJ[count]=1
		count=count+1

	#torcional
	i_trJ=0.34*(R/T)**(2/3)*(d/D)*(t/T)**(-.5)
	#nenhum SIF menor que 1
	count=0
	while count<len(i_trJ):
		if i_trJ[count]<1:
			i_trJ[count]=1
		count=count+1


	#RAMAL

	#no plano
	i_ibJ=0.33*(R/T)**(2/3)*(d/D)**.18*(t/T)**(0.7)
	#nenhum SIF menor que 1
	count=0
	while count<len(i_ibJ):
		if i_ibJ[count]<1:
			i_ibJ[count]=1
		count=count+1

	#fora do plano
	i_obJ=0.42*(R/T)**(2/3)*(d/D)**0.37*(t/T)**(0.37)
	#nenhum SIF menor que 1
	count=0
	while count<len(i_obJ):
		if i_obJ[count]<1:
			i_obJ[count]=1
		count=count+1

	#torcional
	i_tbJ=0.42*(R/T)**(2/3)*(d/D)**1.1*(t/T)**(1.1)
	#nenhum SIF menor que 1
	count=0
	while count<len(i_tbJ):
		if i_tbJ[count]<1:
			i_tbJ[count]=1
		count=count+1

	#----------------------CONDIÇÕES DO B31J para o caso 2.1 --------------#
	#SE i_ob<i_ib, fazer i_ob=i_ib
	count=0
	while count<len(i_obJ):
		if i_obJ[count]<i_ibJ[count]:
			i_obJ[count]=i_ibJ[count]
		count=count+1

	#SE i_ir<i_or, fazer i_ir=i_or
	count=0
	while count<len(i_irJ):
		if i_irJ[count]<i_orJ[count]:
			i_irJ[count]=i_orJ[count]
		count=count+1
		
	#organizando a forma como o output desta função será pra que a chamada do fator ocorra de modo: 
	#	var[flex ou SIF][in, out ou torç.][run ou branch][D ou B31J]
	# ex. var[0][0][0][1] = k_irJ
	# ex. var[1][2][1][0] = i_tbD
	
	kir=[1, k_irJ]
	kib=[1, k_ibJ]
	kor=[1, k_orJ]
	kob=[1, k_obJ]
	ktr=[1, k_trJ]
	ktb=[1, k_tbJ]
	
	iir=[i_irD, i_irJ]
	iib=[i_ibD, i_ibJ]
	ior=[i_orD, i_orJ]
	iob=[i_obD, i_obJ]
	itr=[i_trD, i_trJ]
	itb=[i_tbD, i_tbJ]
	
	ki=[kir, kib]
	ko=[kor, kob]
	kt=[ktr, ktb]
	
	ii=[iir, iib]
	io=[ior, iob]
	it=[itr, itb]
	
	k = [ki, ko, kt]
	i = [ii, io, it]
	
	#######################################
	
	fatores21= [k, i]
	
	#CHECK RECURSIVO -- fatores 2.1 pelo B31J não podem ser maiores do que os 2.3 também pelo B31J; 
	#qual seja: se fator2.1>fator2.3, fator2.1=fator2.3
	
	if recursivo==True:
		check23=fatores2_3(nps,T,D_o,t,d_o,False) #chamar com recursivo=False, pra não entrar em loop infinito
		#iterando em cada fator calculado pelo B31J:
		J=1
		for tipoFator in [0, 1]:
			for direcao in [0, 1, 2]:
				for tubulacao in [0, 1]:
					count=0
					while count<len(R):
						if fatores21[tipoFator][direcao][tubulacao][J][count]>check23[tipoFator][direcao][tubulacao][J][count]: #condição dada
							fatores21[tipoFator][direcao][tubulacao][J][count]=check23[tipoFator][direcao][tubulacao][J][count] #estabelecendo igualdade
							print ('troca fator 21>fator23 na pos ' + str(tipoFator) + str(direcao) + str(tubulacao)+str(J)+str(count))
							print (fatores21[tipoFator][direcao][tubulacao][J][count])
						count+=1
	
	return (fatores21)

def fatores2_2 (NPSin,Tin,D_oin,tin,d_oin, recursivo=True): #função que calcula fatores para bocas de lobo com reforço de espessura t_p=T
		
	nps=NPSin

	T=Tin
	D_o=D_oin

	t=tin
	d_o=d_oin

	#definindo espessura do reforço
	t_p=T

	#obtendo parâmetros geométricos
	D=D_o-T
	d=d_o-t
	R=(D_o-T)/2
	r=(d_o-t)/2

	#check de conformidade com R/T<=50
	RsobreT=R/T
	for x in RsobreT:
		if x>50:
			sys.exit('Não conformidade com R/T<=50')

	#check de conformidade com d/D<=1
	dsobreD=d/D
	for x in dsobreD:
		if x>1:
			sys.exit('Não conformidade com d/D<=0')


	#check de conformidade com r/t<=50
	rsobret=r/t
	for x in rsobret:
		if x>50:
			sys.exit('Não conformidade com r/t<=50')
			
	#--------------------- ITEM 2.2 --------------------#
	#---------------------- cálculo ----------------------#

	# fator de flexibilidade segundo ASME B31J (o Apêndice D não apresenta valores)

	#PRINCIPAL

	#no plano
	k_irJ=0.21*(R/(T+0.5*t_p))**0.97*(t/T)**(-0.65)*(d/D)**6.2
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_irJ):
		if k_irJ[count]<1:
			k_irJ[count]=1
		count=count+1


	#fora do plano=1, mas precisa criar lista da mesma dimensão com vários uns.
	k_orJ=(0*R)+1

	#torcional
	k_trJ=0.12*(R/(T+0.5*t_p))**1.39*(t/T)**(-0.74)*(d/D)**8.5
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_trJ):
		if k_trJ[count]<1:
			k_trJ[count]=1
		count=count+1

	#RAMAL

	#no plano
	k_ibJ=(1.29*(d/D)-2.73*(d/D)**2+1.62*(d/D)**3)*(R/(T+0.5*t_p))**1.2*(t/T)**0.56*(d/D)**0.33
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_ibJ):
		if k_ibJ[count]<1:
			k_ibJ[count]=1
		count=count+1

	#fora do plano
	k_obJ=(0.84*(d/D)-1.27*(d/D)**2+0.5*(d/D)**3)*(R/(T+0.5*t_p))**1.69*(t/T)**0.68*(d/D)**0.21
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_obJ):
		if k_obJ[count]<1:
			k_obJ[count]=1
		count=count+1

	#torcional
	k_tbJ=1.1*(R/(T+0.5*t_p))**0.5*(d/D)**5.42
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_tbJ):
		if k_tbJ[count]<1:
			k_tbJ[count]=1
		count=count+1

	#SIF conforme APÊNDICE D

	#carcaterística de flexibilidade
	h=((T+0.5*t_p)**2.5)/(T**1.5*R)

	#SIF - principal e ramal são iguais
	#fora do plano
	i_orD=0.9/(h**(2/3))
	#nenhum SIF menor que 1
	count=0
	while count<len(i_orD):
		if i_orD[count]<1:
			i_orD[count]=1
		count=count+1
	i_obD=i_orD


	#no plano
	i_irD=(3/4)*(0.9/(h**(2/3)))+(1/4)
	#nenhum SIF menor que 1
	count=0
	while count<len(i_irD):
		if i_irD[count]<1:
			i_irD[count]=1
		count=count+1

	i_ibD=i_irD


	#torcional
	i_trD=np.array([1.0, 1, 1, 1])
	i_tbD=np.array([1.0, 1, 1, 1])

	#SIF conforme B31J
	#PRINCIPAL

	#no plano
	i_irJ=(R/(T+0.5*t_p))**.45*(d/D)**.54*(t/T)**.34
	#este SIF não pode ser menor que 1.5
	count=0
	while count<len(i_irJ):
		if i_irJ[count]<1.5:
			i_irJ[count]=1.5
		count=count+1

	#fora do plano
	i_orJ=(1.29*(d/D)-2.87*(d/D)**2+2.39*(d/D)**3)*(t/T)**(-.25)*(R/(T+0.5*t_p))**.35
	#nenhum SIF menor que 1
	count=0
	while count<len(i_orJ):
		if i_orJ[count]<1:
			i_orJ[count]=1
		count=count+1

	#torcional
	i_trJ=0.36*(R/(T+0.5*t_p))**(2/3)*(t/T)**(-0.6)*(d/D)**1.4
	#nenhum SIF menor que 1
	count=0
	while count<len(i_trJ):
		if i_trJ[count]<1:
			i_trJ[count]=1
		count=count+1


	#RAMAL

	#no plano
	i_ibJ=(3.33*(d/D)-5.49*(d/D)**2+2.94*(d/D)**3)*(T*R**(2/3))*(T+0.5*t_p)**(-5/3)*(t/T)**0.3
	#nenhum SIF menor que 1
	count=0
	while count<len(i_ibJ):
		if i_ibJ[count]<1:
			i_ibJ[count]=1
		count=count+1

	#fora do plano
	#para este caso, será necessário uma iteração sobre t/T para que se possa respeitar a condição 'quando t/T<0.85, t/T=0.85'
	#cria-se uma nova variável, para que não se altere os valores originais de t e T
	tsobreT=t/T

	count=0
	while count<len(tsobreT):
		if tsobreT[count]<0.85:
			tsobreT[count]=0.85
		count=count+1

	i_obJ=(2.86*(d/D)+2.4*(d/D)**2-4.34*(d/D)**3)*(T*R**(2/3))*(T+0.5*t_p)**(-5/3)*tsobreT**0.3
	#nenhum SIF menor que 1
	count=0
	while count<len(i_obJ):
		if i_obJ[count]<1:
			i_obJ[count]=1
		count=count+1

	#torcional
	i_tbJ=0.642*(d/D)**2*(T*R**(2/3))*(T+0.5*t_p)**(-5/3)*(t/T)**.3
	#nenhum SIF menor que 1
	count=0
	while count<len(i_tbJ):
		if i_tbJ[count]<1:
			i_tbJ[count]=1
		count=count+1

	#----------------------CONDIÇÕES DO B31J para o caso 2.2 --------------#
	#SE i_ob<i_ib, fazer i_ob=i_ib
	count=0
	while count<len(i_obJ):
		if i_obJ[count]<i_ibJ[count]:
			i_obJ[count]=i_ibJ[count]
		count=count+1

	#SE i_ir<i_or, fazer i_ir=i_or
	count=0
	while count<len(i_irJ):
		if i_irJ[count]<i_orJ[count]:
			i_irJ[count]=i_orJ[count]
		count=count+1

	#SE t/T<=0.85, e d/D<1 e D/T>=25, deve-se multiplicar o i_ob10J pelo maior entre: 1 e (1.07*(t/T)-1.08*(t/T)**2+0.026)*(D/T)**0.34


	tsobreT=t/T
	dsobreD=d/D
	DsobreT=D/T
	count=0

	fator=i_obJ

	#o multiplicador definido no código
	multiplicador=(1.07*(t/T)-1.08*(t/T)**2+0.026)*(D/T)**0.34

	#o multiplicador nunca pode ser menor que 1
	count=0
	while count<len(multiplicador):
		if multiplicador[count]<1:
			multiplicador[count]=1
		count+=1


	count=0
	while count<len(tsobreT):
		if tsobreT[count]<=0.85: 			#primeira condição
			if dsobreD[count]<1: 			#segunda condição
				if DsobreT[count]>=25: 	#terceira condição
					fator[count]=fator[count]*multiplicador[count] #é preciso cuidar para multiplicar apenas o elemento da lista onde a condição foi atendida; qual seja: fator[count]
		count+=1

	i_obJ=fator ###########################


	#organizando a forma como o output desta função será pra que a chamada do fator ocorra de modo: 
	#	var[flex ou SIF][in, out ou torç.][run ou branch][D ou B31J]
	# ex. var[0][0][0][1] = k_irJ
	# ex. var[1][2][1][0] = i_tbD

	kir=[1, k_irJ]
	kib=[1, k_ibJ]
	kor=[1, k_orJ]
	kob=[1, k_obJ]
	ktr=[1, k_trJ]
	ktb=[1, k_tbJ]

	iir=[i_irD, i_irJ]
	iib=[i_ibD, i_ibJ]
	ior=[i_orD, i_orJ]
	iob=[i_obD, i_obJ]
	itr=[i_trD, i_trJ]
	itb=[i_tbD, i_tbJ]

	ki=[kir, kib]
	ko=[kor, kob]
	kt=[ktr, ktb]

	ii=[iir, iib]
	io=[ior, iob]
	it=[itr, itb]

	k = [ki, ko, kt]
	i = [ii, io, it]
	
	fatores22=[k, i]
	
	
	#CHECK RECURSIVO -- fatores 2.2 pelo B31J não podem ser maiores do que os 2.3 também pelo B31J; 
	#qual seja: se fator2.2>fator2.3, fator2.2=fator2.3
	
	if recursivo==True:
		check23=fatores2_3(nps,T,D_o,t,d_o,False) #chamar com recursivo=False, pra não entrar em loop infinito
		#iterando em cada fator calculado pelo B31J:
		J=1
		for tipoFator in [0, 1]:
			for direcao in [0, 1, 2]:
				for tubulacao in [0, 1]:
					count=0
					while count<len(R):
						if fatores22[tipoFator][direcao][tubulacao][J][count]>check23[tipoFator][direcao][tubulacao][J][count]: #condição dada
							fatores22[tipoFator][direcao][tubulacao][J][count]=check23[tipoFator][direcao][tubulacao][J][count] #estabelecendo igualdade
							print ('troca fator22>fator23 na pos ' + str(tipoFator) + str(direcao) + str(tubulacao)+str(J)+str(count))
							print (fatores22[tipoFator][direcao][tubulacao][J][count])
						count+=1

	#CHECK RECURSIVO -- fatores 2.2 pelo B31J não podem ser menores do que os 2.1; 
	#qual seja: se fator2.2<fator2.1, fator2.2=fator2.1
	
	if recursivo==True:
		check21=fatores2_1(nps,T,D_o,t,d_o,False) #chamar com recursivo=False, pra não entrar em loop infinito
		#iterando em cada fator calculado pelo B31J:
		J=1
		for tipoFator in [0, 1]:
			for direcao in [0, 1, 2]:
				for tubulacao in [0, 1]:
					count=0
					while count<len(R):
						if fatores22[tipoFator][direcao][tubulacao][J][count]<check21[tipoFator][direcao][tubulacao][J][count]: #condição dada
							fatores22[tipoFator][direcao][tubulacao][J][count]=check21[tipoFator][direcao][tubulacao][J][count] #estabelecendo igualdade
							print ('troca fator 22<fator21 na pos' + str(tipoFator) + str(direcao) + str(tubulacao)+str(J)+str(count))
							print (fatores22[tipoFator][direcao][tubulacao][J][count])
						count+=1
		
	
	return (fatores22)	

def fatores2_3 (NPSin,Tin,D_oin,tin,d_oin, recursivo=True): #função que calcula fatores para bocas de lobo sem reforço
	
	nps=NPSin

	T=Tin
	D_o=D_oin

	t=tin
	d_o=d_oin


	#obtendo parâmetros geométricos
	D=D_o-T
	d=d_o-t
	R=(D_o-T)/2
	r=(d_o-t)/2

	#check de conformidade com R/T<=50
	RsobreT=R/T
	for x in RsobreT:
		if x>50:
			sys.exit('Não conformidade com R/T<=50')

	#check de conformidade com d/D<=1
	dsobreD=d/D
	for x in dsobreD:
		if x>1:
			sys.exit('Não conformidade com d/D<=0')


	#check de conformidade com r/t<=50
	rsobret=r/t
	for x in rsobret:
		if x>50:
			sys.exit('Não conformidade com r/t<=50')
			
	#--------------------- ITEM 2.3 --------------------#
	#---------------------- cálculo ----------------------#

	# fator de flexibilidade segundo ASME B31J (o Apêndice D não apresenta valores)

	#PRINCIPAL

	#no plano
	k_irJ=1.23*(R/T)**0.47*(t/T)**(-0.47)*(d/D)**5.3
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_irJ):
		if k_irJ[count]<1:
			k_irJ[count]=1
		count=count+1


	#fora do plano=1, mas precisa criar lista da mesma dimensão com vários uns.
	k_orJ=(0*R)+1

	#torcional
	k_trJ=(R/T)**0.78*(t/T)**(-0.8)*(d/D)**7.8
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_trJ):
		if k_trJ[count]<1:
			k_trJ[count]=1
		count=count+1

	#RAMAL

	#no plano
	k_ibJ=(3.15*(d/D)-6.4*(d/D)**2+4*(d/D)**3)*(R/T)**.83*(t/T)**.49*(d/D)**(-0.2)
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_ibJ):
		if k_ibJ[count]<1:
			k_ibJ[count]=1
		count=count+1

	#fora do plano
	k_obJ=(2.05*(d/D)-2.94*(d/D)**2+1.1*(d/D)**3)*(R/T)**1.4*(t/T)**.6*(d/D)**.12
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_obJ):
		if k_obJ[count]<1:
			k_obJ[count]=1
		count=count+1

	#torcional
	k_tbJ=.95*(R/T)**.83*(d/D)**5.42
	#nenhum fator de flexibilidade menor que 1
	count=0
	while count<len(k_tbJ):
		if k_tbJ[count]<1:
			k_tbJ[count]=1
		count=count+1

	#SIF conforme APÊNDICE D

	#carcaterística de flexibilidade
	h=T/R

	#SIF - principal e ramal são iguais
	#fora do plano
	i_orD=0.9/(h**(2/3))
	#nenhum SIF menor que 1
	count=0
	while count<len(i_orD):
		if i_orD[count]<1:
			i_orD[count]=1
		count=count+1
	i_obD=i_orD


	#no plano
	i_irD=(3/4)*(0.9/(h**(2/3)))+(1/4)
	#nenhum SIF menor que 1
	count=0
	while count<len(i_irD):
		if i_irD[count]<1:
			i_irD[count]=1
		count=count+1

	i_ibD=i_irD


	#torcional
	i_trD=np.array([1.0, 1, 1, 1])
	i_tbD=np.array([1.0, 1, 1, 1])

	#SIF conforme B31J
	#PRINCIPAL

	#no plano
	i_irJ=1.2*(d/D)**0.5*(R/T)**0.4*(t/T)**(-0.35)
	#este SIF não pode ser menor que 1.5
	count=0
	while count<len(i_irJ):
		if i_irJ[count]<1.5:
			i_irJ[count]=1.5
		count=count+1

	#fora do plano
	#para este caso, será necessário uma iteração sobre t/T para que se possa respeitar a condição 'quando t/T<0.5, t/T=0.5'
	#bem como d/D, para respeitar 'quando d/D<0.5, usar d/D=0.5'
	#cria-se duas novas variáeis, para que não se altere os valores originais de t, T, d e D.
	tsobreT=t/T
	dsobreD=d/D
	
	count=0
	while count<len(tsobreT):
		if tsobreT[count]<0.5:
			tsobreT[count]=0.5
		count=count+1
		
	count=0
	while count<len(dsobreD):
		if dsobreD[count]<0.5:
			dsobreD[count]=0.5
		count=count+1
	
	i_orJ=(dsobreD-2.7*dsobreD**2+2.62*dsobreD**3)*(R/T)**.43*tsobreT**(-0.7)
	#nenhum SIF menor que 1
	count=0
	while count<len(i_orJ):
		if i_orJ[count]<1:
			i_orJ[count]=1
		count=count+1

	#torcional
	#para este caso, será necessário uma iteração sobre t/T para que se possa respeitar a condição 'quando t/T<0.15, t/T=0.15'
	tsobreT=t/T
	
	count=0
	while count<len(tsobreT):
		if tsobreT[count]<0.15:
			tsobreT[count]=0.15
		count=count+1
	
	i_trJ=1.2*(R/T)**.46*(tsobreT)**(-0.45)*(d/D)**1.37
	#nenhum SIF menor que 1
	count=0
	while count<len(i_trJ):
		if i_trJ[count]<1:
			i_trJ[count]=1
		count=count+1


	#RAMAL

	#no plano
	#para este caso, será necessário uma iteração sobre t/T para que se possa respeitar a condição 'quando t/T<1, t/T=1'
	tsobreT=t/T
	
	count=0
	while count<len(tsobreT):
		if tsobreT[count]<1:
			tsobreT[count]=1
		count=count+1
	
	i_ibJ=(0.038+1.45*(d/D)-2.39*(d/D)**2+1.34*(d/D)**3)*(R/T)**.76*(tsobreT)**.74
	#nenhum SIF menor que 1
	count=0
	while count<len(i_ibJ):
		if i_ibJ[count]<1:
			i_ibJ[count]=1
		count=count+1

	#fora do plano
	#para este caso, será necessário uma iteração sobre t/T para que se possa respeitar a condição 'quando t/T<0.85, t/T=0.85'
	#cria-se uma nova variável, para que não se altere os valores originais de t e T
	tsobreT=t/T

	count=0
	while count<len(tsobreT):
		if tsobreT[count]<0.85:
			tsobreT[count]=0.85
		count=count+1

	i_obJ=(0.038+2*(d/D)+2*(d/D)**2-3.1*(d/D)**3)*(R/T)**(2/3)*tsobreT
	#nenhum SIF menor que 1
	count=0
	while count<len(i_obJ):
		if i_obJ[count]<1:
			i_obJ[count]=1
		count=count+1

	#torcional
	i_tbJ=0.45*(R/T)**.8*(t/T)**.29*(d/D)**2
	#nenhum SIF menor que 1
	count=0
	while count<len(i_tbJ):
		if i_tbJ[count]<1:
			i_tbJ[count]=1
		count=count+1

	#----------------------CONDIÇÕES DO B31J para o caso 2.2 --------------#
	#SE i_ob<i_ib, fazer i_ob=i_ib
	count=0
	while count<len(i_obJ):
		if i_obJ[count]<i_ibJ[count]:
			i_obJ[count]=i_ibJ[count]
		count=count+1

	#SE i_ir<i_or, fazer i_ir=i_or
	count=0
	while count<len(i_irJ):
		if i_irJ[count]<i_orJ[count]:
			i_irJ[count]=i_orJ[count]
		count=count+1

	#SE t/T<=0.85, e d/D<1 e D/T>=25, deve-se multiplicar o i_ob10J pelo maior entre: 1 e (0.75*(t/T)-0.89*(t/T)**2+0.18)*(D/T)**0.34
	

	tsobreT=t/T
	dsobreD=d/D
	DsobreT=D/T
	count=0

	fator=i_obJ


	#o multiplicador definido no código
	multiplicador=(0.75*(t/T)-0.89*(t/T)**2+0.18)*(D/T)**0.34
	

	#o multiplicador nunca pode ser menor que 1
	count=0
	while count<len(multiplicador):
		if multiplicador[count]<1:
			multiplicador[count]=1
		count+=1


	count=0
	while count<len(tsobreT):
		if tsobreT[count]<=0.85: 			#primeira condição
			if dsobreD[count]<1: 			#segunda condição
				if DsobreT[count]>=25: 	#terceira condição
					fator[count]=fator[count]*multiplicador[count] #é preciso cuidar para multiplicar apenas o elemento da lista onde a condição foi atendida; qual seja: fator[count]
		count+=1

	i_obJ=fator ###########################


	#organizando a forma como o output desta função será pra que a chamada do fator ocorra de modo: 
	#	var[flex ou SIF][in, out ou torç.][run ou branch][D ou B31J]
	# ex. var[0][0][0][1] = k_irJ
	# ex. var[1][2][1][0] = i_tbD

	kir=[1, k_irJ]
	kib=[1, k_ibJ]
	kor=[1, k_orJ]
	kob=[1, k_obJ]
	ktr=[1, k_trJ]
	ktb=[1, k_tbJ]

	iir=[i_irD, i_irJ]
	iib=[i_ibD, i_ibJ]
	ior=[i_orD, i_orJ]
	iob=[i_obD, i_obJ]
	itr=[i_trD, i_trJ]
	itb=[i_tbD, i_tbJ]

	ki=[kir, kib]
	ko=[kor, kob]
	kt=[ktr, ktb]

	ii=[iir, iib]
	io=[ior, iob]
	it=[itr, itb]

	k = [ki, ko, kt]
	i = [ii, io, it]
	
	fatores23=[k, i]
	
	#CHECK RECURSIVO -- fatores 2.3 pelo B31J não podem ser menores do que os do 2.1; 
	#qual seja: se fator2.3<fator2.1, fator2.3=fator2.1
	
	if recursivo==True:
		check21=fatores2_1(nps,T,D_o,t,d_o,False) #chamar com recursivo=False, pra não entrar em loop infinito
		#iterando em cada fator calculado pelo B31J:
		J=1
		for tipoFator in [0, 1]:
			for direcao in [0, 1, 2]:
				for tubulacao in [0, 1]:
					count=0
					while count<len(R):
						if fatores23[tipoFator][direcao][tubulacao][J][count]<check21[tipoFator][direcao][tubulacao][J][count]: #condição dada
							fatores23[tipoFator][direcao][tubulacao][J][count]=check21[tipoFator][direcao][tubulacao][J][count] #estabelecendo igualdade
							print ('troca, fator23<fator21 na pos ' + str(tipoFator) + str(direcao) + str(tubulacao)+str(J)+str(count))
							print (fatores23[tipoFator][direcao][tubulacao][J][count])
						count+=1
	
	
	return (fatores23)	

def plotFatores(nps, fat, nomeFigura=0):
#x=fatores2_n(nps, T, D_o, t, d_o)
	
	#alocando as variáveis da entrada em novas variáveis
	
	k_irD=fat[0][0][0][0]
	k_irJ=fat[0][0][0][1]

	k_ibD=fat[0][0][1][0]
	k_ibJ=fat[0][0][1][1]

	k_orD=fat[0][1][0][0]
	k_orJ=fat[0][1][0][1]

	k_obD=fat[0][1][1][0]
	k_obJ=fat[0][1][1][1]

	k_trD=fat[0][2][0][0]
	k_trJ=fat[0][2][0][1]

	k_tbD=fat[0][2][1][0]
	k_tbJ=fat[0][2][1][1]


	#SIF
	i_irD=fat[1][0][0][0]
	i_irJ=fat[1][0][0][1]

	i_ibD=fat[1][0][1][0]
	i_ibJ=fat[1][0][1][1]

	i_orD=fat[1][1][0][0]
	i_orJ=fat[1][1][0][1]

	i_obD=fat[1][1][1][0]
	i_obJ=fat[1][1][1][1]

	i_trD=fat[1][2][0][0]
	i_trJ=fat[1][2][0][1]

	i_tbD=fat[1][2][1][0]
	i_tbJ=fat[1][2][1][1]


	##plotando
	#FLEXIBILIDADE
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6), sharey=False)
	for ax in fig.get_axes():
		ax.label_outer()


	ax1.plot(nps, k_irJ, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ir}$, B31J')
	ax1.plot(nps, k_orJ, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{or}$, B31J')
	ax1.plot(nps, k_trJ, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tr}$, B31J')

	ax2.plot(nps, k_ibJ, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ib}$, B31J')
	ax2.plot(nps, k_obJ, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{ob}$, B31J')
	ax2.plot(nps, k_tbJ, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tb}$, B31J')

	#ax2.set_ylabel('Fator de flexibilidade no ramal $(i_{ib}, i_{ob}, i_{tb})$')
	ax1.set_ylabel('Fator de flexibilidade na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')

	secax= ax.secondary_yaxis('right')
	secax.set_ylabel('Fator de flexibilidade no ramal $(i_{ib}, i_{ob}, i_{tb})$')


	ax2.set_xlabel('NPS')
	ax1.set_xlabel('NPS')
	ax.yaxis.set_label_position("right")
	ax.yaxis.tick_right()

	ax1.legend(bbox_to_anchor=(.99, 0, 1, 1), loc='upper left')
	ax2.legend(bbox_to_anchor=(-.99, 0, 1, 1), loc='lower right')
			   
	plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
	plt.subplots_adjust(wspace=.37)

	if nomeFigura!=0:
		plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/plotFatores/' + str(nomeFigura) + 'k.eps', format='eps')
		
	#SIFS
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6), sharey=True)
	for ax in fig.get_axes():
		ax.label_outer()


	ax1.plot(nps, i_irD, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, Ap.D')
	ax1.plot(nps, i_irJ, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, B31J')
	ax1.plot(nps, i_orD, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, Ap.D')
	ax1.plot(nps, i_orJ, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, B31J')
	ax1.plot(nps, i_trD, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, Ap.D')
	ax1.plot(nps, i_trJ, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, B31J')

	ax2.plot(nps, i_ibD, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, Ap.D')
	ax2.plot(nps, i_ibJ, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, B31J')
	ax2.plot(nps, i_obD, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, Ap.D')
	ax2.plot(nps, i_obJ, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, B31J')
	ax2.plot(nps, i_tbD, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, Ap.D')
	ax2.plot(nps, i_tbJ, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, B31J')

	#ax2.set_ylabel('SIFs no ramal $(i_{ib}, i_{ob}, i_{tb})$')
	
	secax= ax.secondary_yaxis('right')
	secax.set_ylabel('SIFs no ramal $(i_{ib}, i_{ob}, i_{tb})$')
	ax1.set_ylabel('SIFs na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')
	ax2.set_xlabel('NPS')
	ax1.set_xlabel('NPS')
	ax.yaxis.set_label_position("right")
	ax.yaxis.tick_right()

	ax1.legend(bbox_to_anchor=(.99, 0, 1, 1), loc='upper left')
	ax2.legend(bbox_to_anchor=(-.99, 0, 1, 1), loc='lower right')
			   
	plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
	plt.subplots_adjust(wspace=.37)
	
	if nomeFigura!=0:
		plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/plotFatores/' + str(nomeFigura) + '.eps', format='eps')

def plotMedia(fat10, fat14, fat18, fat24, nomeFigura=0):
	
	##obtendo medias para os sifs
	#principal
	i_irMD=np.array([np.average(fat10[1][0][0][0]), np.average(fat14[1][0][0][0]), np.average(fat18[1][0][0][0]), np.average(fat24[1][0][0][0])])
	i_irMJ=np.array([np.average(fat10[1][0][0][1]), np.average(fat14[1][0][0][1]), np.average(fat18[1][0][0][1]), np.average(fat24[1][0][0][1])])
	i_orMD=np.array([np.average(fat10[1][1][0][0]), np.average(fat14[1][1][0][0]), np.average(fat18[1][1][0][0]), np.average(fat24[1][1][0][0])])
	i_orMJ=np.array([np.average(fat10[1][1][0][1]), np.average(fat14[1][1][0][1]), np.average(fat18[1][1][0][1]), np.average(fat24[1][1][0][1])])
	i_trMD=np.array([np.average(fat10[1][2][0][0]), np.average(fat14[1][2][0][0]), np.average(fat18[1][2][0][0]), np.average(fat24[1][2][0][0])])
	i_trMJ=np.array([np.average(fat10[1][2][0][1]), np.average(fat14[1][2][0][1]), np.average(fat18[1][2][0][1]), np.average(fat24[1][2][0][1])])

	#ramal
	i_ibMD=np.array([np.average(fat10[1][0][1][0]), np.average(fat14[1][0][1][0]), np.average(fat18[1][0][1][0]), np.average(fat24[1][0][1][0])])
	i_ibMJ=np.array([np.average(fat10[1][0][1][1]), np.average(fat14[1][0][1][1]), np.average(fat18[1][0][1][1]), np.average(fat24[1][0][1][1])])
	i_obMD=np.array([np.average(fat10[1][1][1][0]), np.average(fat14[1][1][1][0]), np.average(fat18[1][1][1][0]), np.average(fat24[1][1][1][0])])
	i_obMJ=np.array([np.average(fat10[1][1][1][1]), np.average(fat14[1][1][1][1]), np.average(fat18[1][1][1][1]), np.average(fat24[1][1][1][1])])
	i_tbMD=np.array([np.average(fat10[1][2][1][0]), np.average(fat14[1][2][1][0]), np.average(fat18[1][2][1][0]), np.average(fat24[1][2][1][0])])
	i_tbMJ=np.array([np.average(fat10[1][2][1][1]), np.average(fat14[1][2][1][1]), np.average(fat18[1][2][1][1]), np.average(fat24[1][2][1][1])])


	##obtendo medias para flexibilidade

	#principal
	k_irMJ=np.array([np.average(fat10[0][0][0][1]), np.average(fat14[0][0][0][1]), np.average(fat18[0][0][0][1]), np.average(fat24[0][0][0][1])])
	k_orMJ=np.array([np.average(fat10[0][1][0][1]), np.average(fat14[0][1][0][1]), np.average(fat18[0][1][0][1]), np.average(fat24[0][1][0][1])])
	k_trMJ=np.array([np.average(fat10[0][2][0][1]), np.average(fat10[0][2][0][1]), np.average(fat10[0][2][0][1]), np.average(fat10[0][2][0][1])])

	#ramal
	k_ibMJ=np.array([np.average(fat10[0][0][1][1]), np.average(fat14[0][0][1][1]), np.average(fat18[0][0][1][1]), np.average(fat24[0][0][1][1])])
	k_obMJ=np.array([np.average(fat10[0][1][1][1]), np.average(fat14[0][1][1][1]), np.average(fat18[0][1][1][1]), np.average(fat24[0][1][1][1])])
	k_tbMJ=np.array([np.average(fat10[0][2][1][1]), np.average(fat10[0][2][1][1]), np.average(fat10[0][2][1][1]), np.average(fat10[0][2][1][1])])
	

	
	#PLOTANDO VARIAÇÃO DAS MÉDIAS POR NPS DA TUBULAÇÃO PRINCIPAL
	#SIFs
	npsP=np.array(['10', '14', '18', '24'])

	##plotando
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
	for ax in fig.get_axes():
		ax.label_outer()


	ax1.plot(npsP, i_irMD, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, Ap.D')
	ax1.plot(npsP, i_irMJ, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, B31J')
	ax1.plot(npsP, i_orMD, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, Ap.D')
	ax1.plot(npsP, i_orMJ, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, B31J')
	ax1.plot(npsP, i_trMD, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, Ap.D')
	ax1.plot(npsP, i_trMJ, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, B31J')


	ax2.plot(npsP, i_ibMD, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, Ap.D')
	ax2.plot(npsP, i_ibMJ, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, B31J')
	ax2.plot(npsP, i_obMD, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, Ap.D')
	ax2.plot(npsP, i_obMJ, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, B31J')
	ax2.plot(npsP, i_tbMD, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, Ap.D')
	ax2.plot(npsP, i_tbMJ, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, B31J')


	ax2.set_ylabel('SIF médio no ramal $(i_{ib}, i_{ob}, i_{tb})$')
	ax1.set_ylabel('SIF médio na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')
	ax2.set_xlabel('NPS da tubulação principal')
	ax1.set_xlabel('NPS da tubulação principal')

	ax.yaxis.set_label_position("right")
	ax.yaxis.tick_right()

	ax1.legend(bbox_to_anchor=(.985, 0, 1, 1), loc='upper left')
	ax2.legend(bbox_to_anchor=(-.985, 0, 1, 1), loc='lower right')
			   
	plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
	plt.subplots_adjust(wspace=.37)
	
	
	if nomeFigura!=0:
		plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/plotFatores/' + str(nomeFigura) + '.eps', format='eps')
		
	############
	
	#FATOR DE FLEXIBILIDADE
	npsP=np.array(['10', '14', '18', '24'])

	##plotando
	fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6), sharey=False)
	for ax in fig.get_axes():
		ax.label_outer()


	ax1.plot(npsP, k_irMJ, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ir}$, B31J')
	ax1.plot(npsP, k_orMJ, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{or}$, B31J')
	ax1.plot(npsP, k_trMJ, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tr}$, B31J')


	ax2.plot(npsP, k_ibMJ, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ib}$, B31J')
	ax2.plot(npsP, k_obMJ, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{ob}$, B31J')
	ax2.plot(npsP, k_tbMJ, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tb}$, B31J')


	#ax2.set_ylabel('F. de flex. médios por NPS da tub. principal $(k_{ib}, k_{ob}, k_{tb})$')
	secax= ax.secondary_yaxis('right')
	secax.set_ylabel('Fator de flex. médio no ramal $(k_{ib}, k_{ob}, k_{tb})$')

	ax1.set_ylabel('Fator de flex. médio na tub. principal $(k_{ir}, k_{or}, k_{tr})$')
	ax2.set_xlabel('NPS da tubulação principal')
	ax1.set_xlabel('NPS da tubulação principal')


	ax.yaxis.set_label_position("right")
	ax.yaxis.tick_right()

	ax1.legend(bbox_to_anchor=(.985, 0, 1, 1), loc='upper left')
	ax2.legend(bbox_to_anchor=(-.985, 0, 1, 1), loc='lower right')
			   
	plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
	plt.subplots_adjust(wspace=.38)
	
	
	if nomeFigura!=0:
		plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/plotFatores/' + str(nomeFigura) + 'k.eps', format='eps')
		
if True: # INSERINDO PARÂMETROS GEOMÉTRICOS
	
	#nps, diâmetro externo e espessura para conforme diâmetro principal -- obtidos do ASME B31.10M

	# -------------------------------------- NPS PRINCIPAL DE 10 ---------------------------------
	nps10=np.array(['10x10x8', '10x10x6', '10x10x5', '10x10x4'])
	T10=np.array([9.27, 9.27, 9.27, 9.27])
	D_o10=np.array([273, 273, 273, 273])
	t10=np.array([8.74, 7.11, 6.55, 6.02])
	d_o10=np.array([219.1, 168.3, 141.3, 114.3])


	# -------------------------------------- NPS PRINCIPAL DE 14 ---------------------------------
	nps14=np.array(['14x14x12', '14x14x10', '14x14x8', '14x14x6'])
	T14=np.array([11.13, 11.13, 11.13, 11.13])
	D_o14=np.array([355.6, 355.6, 355.6, 355.6])
	t14=np.array([10.31, 9.27, 8.74, 7.11])
	d_o14=np.array([323.8, 273.0, 219.1, 168.3])


	# -------------------------------------- NPS PRINCIPAL DE 18 ---------------------------------
	nps18=np.array(['18x18x16', '18x18x14', '18x18x12', '18x18x10'])
	T18=np.array([14.27, 14.27, 14.27, 14.27])
	D_o18=np.array([457, 457, 457, 457])
	t18=np.array([12.70, 11.13, 10.31, 9.27])
	d_o18=np.array([406.4, 355.6, 323.8, 273.0])


	# -------------------------------------- NPS PRINCIPAL DE 24 ---------------------------------
	nps24=np.array(['24x24x20', '24x24x18', '24x24x16', '24x24x14'])
	T24=np.array([17.48, 17.48, 17.48, 17.48])
	D_o24=np.array([610, 610, 610, 610])
	t24=np.array([15.09, 14.27, 12.70, 11.13])
	d_o24=np.array([508.0, 457.0, 406.4, 355.6])

plotH()

if 0: # PRINT CASO 2.1
	## calculando os fatores para o caso 2.1 e plotando resultados.
	fat21nps10=fatores2_1(nps10, T10, D_o10, t10, d_o10)
	plotFatores(nps10, fat21nps10, 'Caso2.1 - NPS 10')

	fat21nps14=fatores2_1(nps14, T14, D_o14, t14, d_o14)
	plotFatores(nps14, fat21nps14, 'Caso2.1 - NPS 14')

	fat21nps18=fatores2_1(nps18, T18, D_o18, t18, d_o18)
	plotFatores(nps18, fat21nps18, 'Caso2.1 - NPS 18')

	fat21nps24=fatores2_1(nps24, T24, D_o24, t24, d_o24)
	plotFatores(nps24, fat21nps24, 'Caso2.1 - NPS 24')
	
	plotMedia(fat21nps10, fat21nps14, fat21nps18, fat21nps24, nomeFigura='Caso2.1 - Médias')

if 0: # PRINT CASO 2.2
	## calculando os fatores para o caso 2.2 e plotando resultados.

	fat22nps10=fatores2_2(nps10, T10, D_o10, t10, d_o10)
	plotFatores(nps10, fat22nps10, 'Caso2.2 - NPS 10')

	fat22nps14=fatores2_2(nps14, T14, D_o14, t14, d_o14)
	#plotFatores(nps14, fat22nps14, 'Caso2.2 - NPS 14')

	fat22nps18=fatores2_2(nps18, T18, D_o18, t18, d_o18)
	#plotFatores(nps18, fat22nps18, 'Caso2.2 - NPS 18')

	fat22nps24=fatores2_2(nps24, T24, D_o24, t24, d_o24)
	#plotFatores(nps24, fat22nps24, 'Caso2.2 - NPS 24')
	
	#plotMedia(fat22nps10, fat22nps14, fat22nps18, fat22nps24, nomeFigura='Caso2.2 - Médias')

if 0: # PRINT CASO 2.3
	## calculando os fatores para o caso 2.3 e plotando resultados.

	fat23nps10=fatores2_3(nps10, T10, D_o10, t10, d_o10,)
	plotFatores(nps10, fat23nps10, 'Caso2.3 - NPS 10')

	fat23nps14=fatores2_3(nps14, T14, D_o14, t14, d_o14)
	plotFatores(nps14, fat23nps14, 'Caso2.3 - NPS 14')

	fat23nps18=fatores2_3(nps18, T18, D_o18, t18, d_o18)
	plotFatores(nps18, fat23nps18, 'Caso2.3 - NPS 18')

	fat23nps24=fatores2_3(nps24, T24, D_o24, t24, d_o24)
	plotFatores(nps24, fat23nps24, 'Caso2.3 - NPS 24')
	
	plotMedia(fat23nps10, fat23nps14, fat23nps18, fat23nps24, nomeFigura='Caso2.3 - Médias')



plt.show()




