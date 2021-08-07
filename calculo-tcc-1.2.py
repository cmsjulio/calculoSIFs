#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys 							#para emitir mensagens de erro quando houver não conformidade
import numpy as np 				#para os cálculos
import matplotlib.pyplot as plt		#para os gráficos

plt.rcParams.update({'font.size' : 14}) 	#aumentando o tamanho da fonte

#nps, diâmetro externo e espessura -- obtidos da ASME B31.10M
nps=np.array([2,3,4,5,6,8,10,12,14,16,18,20,24])
T=np.array([3.91, 5.49, 6.02, 6.55, 7.11, 8.74, 9.27, 10.31, 11.13, 12.7, 14.27, 15.09, 17.48])
D_o=np.array([60.3, 88.9, 114.3, 141.3, 168.3, 219.1, 273, 323.8, 355.6, 406.4, 457, 508, 610])

#check de conformidade com D/T<=100
D=D_o-T
DsobreT=D/T
for x in DsobreT:
	if x>100:
		sys.exit('Não conformidade com D/T<=0')

#raio médio
R=(D_o-T)/2

#--------------------- ITEM 1.2 --------------------#
#---------------------- cálculo ----------------------#
#número de gomos
n=4

#espaçamento entre os gomos na linha de centro
s=D_o/4

#meio angulo entre gomos
theta=(90/(2*n))

#convertendo em radiano
theta=np.deg2rad(theta)

#raio de curvatura
R_1=s/(2*np.tan(theta))

#condição geométrica que precisa ser atendida (R(1+tan(theta))-s>0)
cond=R*(1+np.tan(theta))-s
for x in cond:
	if x<=0:
		sys.exit('Não conformidade com R(1+tan(theta))-s>0')


#característica de flexibilidade
h=(s*T)/(2*R**2*np.tan(theta))

#SIFs
i_i=0.9/(h**(2/3))
i_o=0.9/(h**(2/3))
i_t=1


#fatores de flexibilidade
k_i=1.52/(h**(5/6))
k_o=1.52/(h**(5/6))
k_t=1.52/(h**(5/6))


#considerando efeito da pressão na ovalização
#dados
E=138000000 	#módulo de elasticidade
P=100000		#pressão

#fator pelo qual se deve dividir os fatores de flexibilidade
k_factor=1+6*(P/E)*((R/T)**(7/3))*((R_1/R)**(1/3))

#fator pelo qual se deve dividir os SIF
i_factor=1+3.25*(P/E)*(R/T)**(5/2)*(R_1/R)**(2/3)

#SIFs
i_i=i_i/i_factor
i_o=i_o/i_factor
i_t=1

#fatores de flexibilidade
k_i=k_i/k_factor
k_o=k_o/k_factor
k_t=k_t/k_factor

#nenhum SIF menor que 1
count=0
while count<len(i_i):
	if i_i[count]<1:
		i_i[count]=1
	count=count+1

count=0
while count<len(i_o):
	if i_o[count]<1:
		i_o[count]=1
	count=count+1

#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_i):
	if k_i[count]<1:
		k_i[count]=1
	count=count+1

count=0
while count<len(k_o):
	if k_o[count]<1:
		k_o[count]=1
	count=count+1
	
count=0
while count<len(k_t):
	if k_t[count]<1:
		k_t[count]=1
	count=count+1
	

#-------------------- plot --------------------#
#CARACTERÍSTICA DE FLEXIBILIDADE
fig = plt.figure (1, figsize=(6,6))
plt.plot(nps, h, marker='o', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$h$')
plt.xlabel('NPS')
plt.ylabel('Característica de flexibilidade $(h)$')
plt.tight_layout(pad=1)
plt.legend()
plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 1.2/Figura1.eps', format='eps')


#fator de flexibilidade (todos iguais, em todos os casos)
fig = plt.figure (2, figsize=(6,6))
plt.plot(nps, k_i, marker='o', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$k$ - ' + str(int(P/1000)) + ' kPa')
plt.xlabel('NPS')
plt.ylabel('Fator de flexibilidade $(k)$')
plt.tight_layout(pad=1)
plt.legend()


#SIF no plano e fora do plano (iguais)
fig = plt.figure (3, figsize=(6,6))
plt.plot(nps, i_i, marker='o', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$i_i$, $i_o$ - ' + str(int(P/1000)) + ' kPa')
plt.xlabel('NPS')
plt.ylabel('SIF no plano $(i_i)$ e fora do plano $(i_o)$')
plt.tight_layout(pad=1)
plt.legend()

#-------------------------------------------------------------------#-------------------------------------------------------------------#-------------------------------------------------------------------#-------------------------------------------------------------------#-----------------------


#SIFs
i_i=0.9/(h**(2/3))
i_o=0.9/(h**(2/3))
i_t=1


#fatores de flexibilidade
k_i=1.52/(h**(5/6))
k_o=1.52/(h**(5/6))
k_t=1.52/(h**(5/6))


#considerando efeito da pressão na ovalização
#dados
E=138000000 	#módulo de elasticidade
P=150000		#pressão

#fator pelo qual se deve dividir os fatores de flexibilidade
k_factor=1+6*(P/E)*((R/T)**(7/3))*((R_1/R)**(1/3))

#fator pelo qual se deve dividir os SIF
i_factor=1+3.25*(P/E)*(R/T)**(5/2)*(R_1/R)**(2/3)

#SIFs
i_i=i_i/i_factor
i_o=i_o/i_factor
i_t=1

#fatores de flexibilidade
k_i=k_i/k_factor
k_o=k_o/k_factor
k_t=k_t/k_factor

#nenhum SIF menor que 1
count=0
while count<len(i_i):
	if i_i[count]<1:
		i_i[count]=1
	count=count+1

count=0
while count<len(i_o):
	if i_o[count]<1:
		i_o[count]=1
	count=count+1

#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_i):
	if k_i[count]<1:
		k_i[count]=1
	count=count+1

count=0
while count<len(k_o):
	if k_o[count]<1:
		k_o[count]=1
	count=count+1
	
count=0
while count<len(k_t):
	if k_t[count]<1:
		k_t[count]=1
	count=count+1
	

#-------------------- plot --------------------#
plt.figure (2)
plt.plot(nps, k_i, marker='s', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$k$ - ' + str(int(P/1000)) + ' kPa')
plt.tight_layout(pad=1)
plt.legend()

#SIF no plano
fig = plt.figure (3, figsize=(6,6))
plt.plot(nps, i_i, marker='s', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$i_i$, $i_o$ - ' + str(int(P/1000)) + ' kPa')
plt.tight_layout(pad=1)
plt.legend()


#-------------------------------------------------------------------#-------------------------------------------------------------------#-------------------------------------------------------------------#-------------------------------------------------------------------#-----------------------


#SIFs
i_i=0.9/(h**(2/3))
i_o=0.9/(h**(2/3))
i_t=1


#fatores de flexibilidade
k_i=1.52/(h**(5/6))
k_o=1.52/(h**(5/6))
k_t=1.52/(h**(5/6))


#considerando efeito da pressão na ovalização
#dados
E=138000000 	#módulo de elasticidade
P=200000		#pressão

#fator pelo qual se deve dividir os fatores de flexibilidade
k_factor=1+6*(P/E)*((R/T)**(7/3))*((R_1/R)**(1/3))

#fator pelo qual se deve dividir os SIF
i_factor=1+3.25*(P/E)*(R/T)**(5/2)*(R_1/R)**(2/3)

#SIFs
i_i=i_i/i_factor
i_o=i_o/i_factor
i_t=1

#fatores de flexibilidade
k_i=k_i/k_factor
k_o=k_o/k_factor
k_t=k_t/k_factor

#nenhum SIF menor que 1
count=0
while count<len(i_i):
	if i_i[count]<1:
		i_i[count]=1
	count=count+1

count=0
while count<len(i_o):
	if i_o[count]<1:
		i_o[count]=1
	count=count+1

#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_i):
	if k_i[count]<1:
		k_i[count]=1
	count=count+1

count=0
while count<len(k_o):
	if k_o[count]<1:
		k_o[count]=1
	count=count+1
	
count=0
while count<len(k_t):
	if k_t[count]<1:
		k_t[count]=1
	count=count+1
	

#-------------------- plot --------------------#
plt.figure (2)
plt.plot(nps, k_i, marker='x', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$k$ - ' + str(int(P/1000)) + ' kPa')
plt.tight_layout(pad=1)
plt.legend()

#SIF no plano
fig = plt.figure (3, figsize=(6,6))
plt.plot(nps, i_i, marker='x', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$i_i$, $i_o$ - ' + str(int(P/1000)) + ' kPa')
plt.tight_layout(pad=1)
plt.legend()


#-------------------------------------------------------------------#-------------------------------------------------------------------#-------------------------------------------------------------------#-------------------------------------------------------------------#-----------------------


#SIFs
i_i=0.9/(h**(2/3))
i_o=0.9/(h**(2/3))
i_t=1


#fatores de flexibilidade
k_i=1.52/(h**(5/6))
k_o=1.52/(h**(5/6))
k_t=1.52/(h**(5/6))


#considerando efeito da pressão na ovalização
#dados
E=138000000 	#módulo de elasticidade
P=250000		#pressão

#fator pelo qual se deve dividir os fatores de flexibilidade
k_factor=1+6*(P/E)*((R/T)**(7/3))*((R_1/R)**(1/3))

#fator pelo qual se deve dividir os SIF
i_factor=1+3.25*(P/E)*(R/T)**(5/2)*(R_1/R)**(2/3)

#SIFs
i_i=i_i/i_factor
i_o=i_o/i_factor
i_t=1

#fatores de flexibilidade
k_i=k_i/k_factor
k_o=k_o/k_factor
k_t=k_t/k_factor

#nenhum SIF menor que 1
count=0
while count<len(i_i):
	if i_i[count]<1:
		i_i[count]=1
	count=count+1

count=0
while count<len(i_o):
	if i_o[count]<1:
		i_o[count]=1
	count=count+1

#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_i):
	if k_i[count]<1:
		k_i[count]=1
	count=count+1

count=0
while count<len(k_o):
	if k_o[count]<1:
		k_o[count]=1
	count=count+1
	
count=0
while count<len(k_t):
	if k_t[count]<1:
		k_t[count]=1
	count=count+1
	

#-------------------- plot --------------------#
plt.figure (2)
plt.plot(nps, k_i, marker='*', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$k$ - ' + str(int(P/1000)) + ' kPa')
plt.tight_layout(pad=1)
plt.legend()
plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 1.2/Figura2.eps', format='eps')

#SIF no plano
fig = plt.figure (3, figsize=(6,6))
plt.plot(nps, i_i, marker='*', markersize=10, mfc='white', linestyle='-',alpha=.7, label='$i_i$, $i_o$ - ' + str(int(P/1000)) + ' kPa')
plt.tight_layout(pad=1)
plt.legend()
plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 1.2/Figura3.eps', format='eps')


plt.show()



