#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys 						#para emitir mensagens de erro quando houver não conformidade
import numpy as np 				#para os cálculos
import matplotlib.pyplot as plt		#para os gráficos

plt.rcParams.update({'font.size' : 14}) 	#aumentando o tamanho da fonte dos gráficos

def fatores3_1 (nps,T1,T2,D1,D2):
	print ('NPS de: ' + str(nps))
	
	#obtendo valores geométricos
	r2=0.1*D1
	L2=0.1*D2
	#na ausência de alpha, nosso caso, usar o menor entre 60*((D1/D2)-1) e 60
	alpha=60*((D1/D2)-1) 
	print ('antigo alpha')
	print (alpha)
	
	#nenhum alpha maior que 60
	count=0
	while count<len(alpha):
		if alpha[count]>60:
			alpha[count]=60
		count=count+1
	
	print ('novo alpha:')
	print (alpha)
	
	###############
	#check de conformidade com 5<alpha<=60
	for a in alpha:
		if not (5<a and a<=60):
			print ('erro em:')
			print (a)
			sys.exit('Não conformidade com 5<alpha<=60')
			
    #check de conformidade com 5<D2/T2<80
	D2sobreT2=D2/T2
	print('D2 sobre T2= ')
	print (D2sobreT2)
	for a in D2sobreT2:
		if not (5<a and a<80):
			print ('erro em:')
			print (a)
			sys.exit('Não conformidade com 5<D2/T2<80')
	
	#check de conformidade com 0.08<r2/D2<0.7
	r2sobreD2=r2/D2
	for a in r2sobreD2:
		if not (0.08<a and a<0.7):
			sys.exit('Não conformidade com 0.08<r2/D2<0.7')

	#check de conformidade com 1<T1/T2<2.12
	T1sobreT2=T1/T2
	for a in T1sobreT2:
		if not (1<a and a<2.12):
			sys.exit('Não conformidade com 1<T1/T2<2.12')
	
	#para utilizar no plot
	alphaT2sobreT1=alpha*T2/T1
	
	i_i=0.6+0.003*(alpha*T2/T1)**0.8*(D2/T2)**0.25*(D2/r2)
	i_o=0.6+0.003*(alpha*T2/T1)**0.8*(D2/T2)**0.25*(D2/r2)
	i_t=0.3+0.0015*(alpha*T2/T1)**0.8*(D2/T2)**0.25*(D2/r2)
	
	#nenhum SIF menor que 1
	count=0
	while count<len(i_i):
		if i_i[count]<1:
			i_i[count]=1
		count=count+1
	#nenhum SIF menor que 1
	count=0
	while count<len(i_o):
		if i_o[count]<1:
			i_o[count]=1
		count=count+1
	#nenhum SIF menor que 1
	count=0
	while count<len(i_t):
		if i_t[count]<1:
			i_t[count]=1
		count=count+1

	
	f=[i_i, i_o, i_t, alphaT2sobreT1]
	
	#a saída fornece uma lista
	#onde
	# f[0] corresponde ao i_i
	# f[1] corresponde ao i_o
	# f[2] corresponde ao i_t
	# f[3] corresponde à razão D1/D2
	
	return (f)

def plotFatores(nps, fat, nomeFigura=0):
#x=fatores2_n(nps, T, D_o, t, d_o)
	
	#alocando as variáveis da entrada em novas variáveis
	i_i=fat[0]
	i_o=fat[1]
	i_t=fat[2]
	alphaT2sobreT1=fat[3]
	
	#SIFS
	
	fig, ax1 = plt.subplots(figsize=(6,6))
	
	ax2 = ax1.twinx()
	ax1.plot(nps, i_i, 'b-', marker='o', markersize=10, mfc='white', alpha=.7, label='$i_{i}, i_{o}$, B31J')
	ax1.plot(nps, i_t, 'g-.', marker='s', markersize=10, mfc='white', alpha=.7, label='$i_{t}$, B31J')
	
	ax2.plot(nps, alphaT2sobreT1, 'kx', markersize=10, mfc='white', alpha=.7, label=r'$\alpha T_2/T_1$')
	
	
	ax1.set_ylabel('Fator de intensificação de tensão $(i_{i}, i_{o}, i_{t})$')
	ax1.set_xlabel('NPS')
	ax2.set_ylabel(r'$\alpha T_2/T_1$', color='b')
	
	ax1.yaxis.set_label_position("left")
	ax2.yaxis.set_label_position("right")
	
	ax1.yaxis.tick_left()
	ax2.yaxis.tick_right()
	
	ax1.legend(loc='upper left')
	ax2.legend(loc='lower right', bbox_to_anchor=(0,0.1,1,1))
			   
	plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
	
	if nomeFigura!=0:
		plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/plotFatores/' + str(nomeFigura) + '.eps', format='eps')

		
if True: #inserindo valores geométricos
	
	#nps, diâmetro externo e espessura para conforme diâmetro principal -- obtidos do ASME B16.9

	# -------------------------------------- NPS PRINCIPAL DE 10 ---------------------------------
	nps10=np.array(['10x8', '10x6', '10x5', '10x4'])
	T1_10=np.array([9.27, 9.27, 9.27, 9.27])
	T2_10=np.array([8.74, 7.11, 6.55, 6.02])
	D1_10=np.array([273.0, 273.0, 273.0, 273.0])
	D2_10=np.array([219.1, 168.3, 141.3, 114.3])


	# -------------------------------------- NPS PRINCIPAL DE 14 ---------------------------------
	nps14=np.array(['14x12', '14x10', '14x8', '14x6'])
	T1_14=np.array([11.13, 11.13, 11.13, 11.13])
	T2_14=np.array([10.31, 9.27, 8.74, 7.11])
	D1_14=np.array([355.6, 355.6, 355.6, 355.6])
	D2_14=np.array([323.8, 273.0, 219.1, 168.3])


	# -------------------------------------- NPS PRINCIPAL DE 18 ---------------------------------
	nps18=np.array(['18x16', '18x14', '18x12', '18x10'])
	T1_18=np.array([14.27, 14.27, 14.27, 14.27])
	T2_18=np.array([12.70, 11.13, 10.31, 9.27])
	D1_18=np.array([457, 457, 457, 457])
	D2_18=np.array([406.4, 355.6, 323.8, 273.0])


	# -------------------------------------- NPS PRINCIPAL DE 20 ---------------------------------
	nps20=np.array(['20x18', '20x16', '20x14', '20x12'])
	T1_20=np.array([15.09, 15.09, 15.09, 15.09])
	T2_20=np.array([14.27, 12.70, 11.13 ,10.31])
	D1_20=np.array([508.0, 508.0, 508.0, 508.0])
	D2_20=np.array([457.0, 406.4, 355.6, 323.8])

f10=fatores3_1(nps10, T1_10, T2_10, D1_10, D2_10)
f14=fatores3_1(nps14, T1_14, T2_14, D1_14, D2_14)
f18=fatores3_1(nps18, T1_18, T2_18, D1_18, D2_18)
f20=fatores3_1(nps20, T1_20, T2_20, D1_20, D2_20)

print('f10')
print (f10[0])
print(f10[2])

print('f14')
print (f14[0])
print(f14[2])

print('f18')
print (f18[0])
print(f18[2])

print('f20')
print (f20[0])
print(f20[2])

plotFatores(nps10, f10, nomeFigura='Caso 3.1 - nps10')
plotFatores(nps14, f14, nomeFigura='Caso 3.1 - nps14')
plotFatores(nps18, f18, nomeFigura='Caso 3.1 - nps18')
plotFatores(nps20, f20, nomeFigura='Caso 3.1 - nps20')

plt.show()
