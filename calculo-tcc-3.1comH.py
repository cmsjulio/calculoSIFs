#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys 						#para emitir mensagens de erro quando houver não conformidade
import numpy as np 				#para os cálculos
import matplotlib.pyplot as plt		#para os gráficos

plt.rcParams.update({'font.size' : 14}) 	#aumentando o tamanho da fonte dos gráficos

def fatores3_1 (nps,T1,T2,D1,D2, H, caso='exc'):
	
	H=H-(0.1*D2)
	
	
	print ('NPS de: ' + str(nps))
	
	#obtendo valores geométricos
	r2=0.1*D1
	L2=0.1*D2
	
	if caso=='j':
		#na ausência de alpha, usar o menor entre 60*((D1/D2)-1) e 60
		alphaJ=60*((D1/D2)-1) 
		
		print ('alphaJ antes do check >60')
		print (alphaJ)
		#nao pode ser alpha maior que 60
		count=0
		while count<len(alphaJ):
			if alphaJ[count]>60:
				alphaJ[count]=60
			count=count+1
		
		print ('alphaJ depois do check >60')
		print (alphaJ)
	
	if caso=='con':
		#alpha concêntrico (em graus) (sempre maior que 5)
		alphaCon=np.arctan((D1-D2)/(2*H))*(180/np.pi) 
		
		print ('alphaCon antes do check <5')
		print (alphaCon)
		count=0
		while count<len(alphaCon):
			if alphaCon[count]<5:
				alphaCon[count]=5
			count=count+1
		print ('alphaCon depois do check <5')
		print (alphaCon)
		
	if caso=='exc':	
		#alpha excêntrico (em graus)
		alphaExc=np.arctan((D1-D2)/(H))*(180/np.pi)
		
		print ('alphaExc antes do check <5')
		print (alphaExc)
		count=0
		while count<len(alphaExc):
			if alphaExc[count]<5:
				alphaExc[count]=5
			count=count+1
		print ('alphaExc depois do check <5')
		print (alphaExc)
		
	#definiçãod de qual alpha deve ser utilizado
	if caso=='con':
		alpha=alphaCon
	if caso=='exc':
		alpha=alphaExc
	if caso=='j':
		alpha=alphaJ
	
	print('no caso ' + str(caso) + ', alpha vale:')
	print (alpha)
	
	
	###############
	#check de conformidade com 5<alpha<=60
	for a in alpha:
		if not (5<=a and a<=60):
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
	
	
	i_i=0.6+0.003*(alpha*T2/T1)**0.8*(D2/T2)**0.25*(D2/r2)
	i_o=0.6+0.003*(alpha*T2/T1)**0.8*(D2/T2)**0.25*(D2/r2)
	i_t=0.3+0.0015*(alpha*T2/T1)**0.8*(D2/T2)**0.25*(D2/r2)
	
	multiplicador=2-(L2/((D2*T2)**2))
	#condição
	D2T2raiz=(D2*T2)**(.5)
	
	print('L2: ')
	print(str(L2))
	print ('(D2*T2)^.5:') 
	print(str(D2T2raiz))
		
	count=0
	while count<len(D2T2raiz):
		if L2[count]<D2T2raiz[count]:
			print('#########################33')
			print('L2: ' + str(L2[count]))
			print ('(D2*T2)^.5:' + str(D2T2raiz[count]))
			print('mult. ' + str(multiplicador[count]))
			
			print('alteração no sif em '+ nps[count])
			print ('de: i_i' + str(i_i[count]))
			print ('de: i_o' +str(i_o[count]))
			print ('de: i_t' + str(i_t[count]))
			i_i[count]=i_i[count]*multiplicador[count]
			i_o[count]=i_o[count]*multiplicador[count]
			i_t[count]=i_t[count]*multiplicador[count]
			
			print ('de: i_i' + str(i_i[count]))
			print ('de: i_o' +str(i_o[count]))
			print ('de: i_t' + str(i_t[count]))
			count+=1
			
	
	#nenhum SIF menor que 1 ou maior que 2
	count=0
	while count<len(i_i):
		if i_i[count]<1:
			i_i[count]=1
		if i_i[count]>2:
			i_i[count]=2
		count=count+1
	#nenhum SIF menor que 1 ou maior que 2
	count=0
	while count<len(i_o):
		if i_o[count]<1:
			i_o[count]=1
		if i_o[count]>2:
			i_o[count]=2
		count=count+1
	#nenhum SIF menor que 1 ou maior que 2
	count=0
	while count<len(i_t):
		if i_t[count]<1:
			i_t[count]=1
		if i_t[count]>2:
			i_t[count]=2
		count=count+1
		
	
	#para utilizar no plot
	alphaT2sobreT1=(alpha*T2/T1)**.8
	D2sobrer2=(D2/r2)
	param=alphaT2sobreT1*D2sobrer2
	f=[i_i, i_o, i_t, param, caso]
	
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
	fator=fat[3]
	caso=fat[4]
	
	if caso=='j':
		descricao='(caso geral B31J)'
	if caso=='exc':
		descricao='(reduções excêntricas)'
	if caso=='con':
		descricao='(reduções concêntricas)'
	
	#SIFS
	
	fig, ax1 = plt.subplots(figsize=(6,6))
	
	ax2 = ax1.twinx()
	ax1.plot(nps, i_i, 'b-', marker='o', markersize=10, mfc='white', alpha=.7, label='$i_{i}, i_{o}$, B31J')
	ax1.plot(nps, i_t, 'g-.', marker='s', markersize=10, mfc='white', alpha=.7, label='$i_{t}$, B31J')
	
	ax2.plot(nps, fator, 'k^:', markersize=10, mfc='black', alpha=.3, label=r'$({\alpha} T_2/T_1)^{0.8}(D_2/r_2)$')
	
	ax1.set_ylabel('Fator de intensificação de tensão $(i_{i}, i_{o}, i_{t})$')
	ax1.set_xlabel('NPS ' + descricao)
	ax2.set_ylabel(r'$(\alpha T_2/T_1)^{0.8}(D_2/r_2)$', color='b')
	
	ax1.yaxis.set_label_position("left")
	ax2.yaxis.set_label_position("right")
	
	ax1.yaxis.tick_left()
	ax2.yaxis.tick_right()
	
	#limitando o eixo y a de 1 a 2
	x1,x2,y1,y2 = ax1.axis()  
	ax1.axis((x1,x2,0.95,2.05))
	
	#ax1.legend(loc='center left', bbox_to_anchor=(0,0.1,1,1))
	#ax2.legend(loc='center right', bbox_to_anchor=(0,-0.1,1,1))
	
	##ax1.legend(loc='center left', bbox_to_anchor=(0,-0.18,1,1), borderaxespad=1.)
	##ax2.legend(loc='center right', bbox_to_anchor=(0,-0.18,1.02,1), borderaxespad=1.)
	
	legend_1 = ax1.legend(loc='center left', bbox_to_anchor=(0,-0.18,1,1), borderaxespad=1.)
	legend_1.remove()
	ax2.legend(loc='center right', bbox_to_anchor=(0,-0.18,1.02,1), borderaxespad=1.)
	ax2.add_artist(legend_1)
			   
	plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
	
	if nomeFigura!=0:
		plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/plotFatores/' + str(nomeFigura) + str(caso) + '.eps', format='eps')

		
if True: #inserindo valores geométricos
	
	#nps, diâmetro externo e espessura para conforme diâmetro principal -- obtidos do ASME B16.9

	# -------------------------------------- NPS PRINCIPAL DE 10 ---------------------------------
	nps10=np.array(['10x8', '10x6', '10x5', '10x4'])
	T1_10=np.array([9.27, 9.27, 9.27, 9.27])
	T2_10=np.array([8.74, 7.11, 6.55, 6.02])
	D1_10=np.array([273.0, 273.0, 273.0, 273.0])
	D2_10=np.array([219.1, 168.3, 141.3, 114.3])
	H_10=np.array([178.0, 178.0, 178.0, 178.0])


	# -------------------------------------- NPS PRINCIPAL DE 14 ---------------------------------
	nps14=np.array(['14x12', '14x10', '14x8', '14x6'])
	T1_14=np.array([11.13, 11.13, 11.13, 11.13])
	T2_14=np.array([10.31, 9.27, 8.74, 7.11])
	D1_14=np.array([355.6, 355.6, 355.6, 355.6])
	D2_14=np.array([323.8, 273.0, 219.1, 168.3])
	H_14=np.array([330.0, 330.0, 330.0, 330.0])


	# -------------------------------------- NPS PRINCIPAL DE 18 ---------------------------------
	nps18=np.array(['18x16', '18x14', '18x12', '18x10'])
	T1_18=np.array([14.27, 14.27, 14.27, 14.27])
	T2_18=np.array([12.70, 11.13, 10.31, 9.27])
	D1_18=np.array([457, 457, 457, 457])
	D2_18=np.array([406.4, 355.6, 323.8, 273.0])
	H_18=np.array([381.0, 381.0, 381.0, 381.0])


	# -------------------------------------- NPS PRINCIPAL DE 20 ---------------------------------
	nps20=np.array(['20x18', '20x16', '20x14', '20x12'])
	T1_20=np.array([15.09, 15.09, 15.09, 15.09])
	T2_20=np.array([14.27, 12.70, 11.13 ,10.31])
	D1_20=np.array([508.0, 508.0, 508.0, 508.0])
	D2_20=np.array([457.0, 406.4, 355.6, 323.8])
	H_20=np.array([508.0, 508.0, 508.0, 508.0])

f10=fatores3_1(nps10, T1_10, T2_10, D1_10, D2_10, H_10)
f14=fatores3_1(nps14, T1_14, T2_14, D1_14, D2_14, H_14)
f18=fatores3_1(nps18, T1_18, T2_18, D1_18, D2_18, H_18)
f20=fatores3_1(nps20, T1_20, T2_20, D1_20, D2_20, H_20)

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
