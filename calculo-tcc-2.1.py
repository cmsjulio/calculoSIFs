#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys 						#para emitir mensagens de erro quando houver não conformidade
import numpy as np 				#para os cálculos
import matplotlib.pyplot as plt		#para os gráficos

plt.rcParams.update({'font.size' : 14}) 	#aumentando o tamanho da fonte dos gráficos

# -------------------------------------- NPS PRINCIPAL DE 10 ---------------------------------
#nps, diâmetro externo e espessura para principal com NPS 10-- obtidos da ASME B31.10M
nps=np.array(['10x10x8', '10x10x6', '10x10x5', '10x10x4'])

T=np.array([9.27, 9.27, 9.27, 9.27])
D_o=np.array([273, 273, 273, 273])

t=np.array([8.74, 7.11, 6.55, 6.02])
d_o=np.array([219.1, 168.3, 141.3, 114.3])

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
k_irJ10=0.18*(R/T)**0.8*(d/D)**5
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_irJ10):
	if k_irJ10[count]<1:
		k_irJ10[count]=1
	count=count+1


#fora do plano=1, mas precisa criar lista da mesma dimensão com vários uns.
k_orJ10=(0*R)+1

#torcional
k_trJ10=0.08*(R/T)**0.91*(d/D)**5.7
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_trJ10):
	if k_trJ10[count]<1:
		k_trJ10[count]=1
	count=count+1

#RAMAL

#no plano
k_ibJ10=(1.91*(d/D)-4.32*(d/D)**2+2.7*(d/D)**3)*(R/T)**.77*(d/D)**.47*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_ibJ10):
	if k_ibJ10[count]<1:
		k_ibJ10[count]=1
	count=count+1

#fora do plano
k_obJ10=(0.34*(d/D)-0.49*(d/D)**2+0.18*(d/D)**3)*(R/T)**1.46*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_obJ10):
	if k_obJ10[count]<1:
		k_obJ10[count]=1
	count=count+1

#torcional
k_tbJ10=(1.08*(d/D)-2.44*(d/D)**2+1.52*(d/D)**3)*(R/T)**.77*(d/D)**1.61*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_tbJ10):
	if k_tbJ10[count]<1:
		k_tbJ10[count]=1
	count=count+1

#SIF conforme APÊNDICE D

#carcaterística de flexibilidade
h=3.1*(T/R)

#SIF - principal e ramal são iguais
#fora do plano
i_or10D=0.9/(h**(2/3))
#nenhum SIF menor que 1
count=0
while count<len(i_or10D):
	if i_or10D[count]<1:
		i_or10D[count]=1
	count=count+1
i_ob10D=i_or10D


#no plano
i_ir10D=(3/4)*(0.9/(h**(2/3)))+(1/4)
#nenhum SIF menor que 1
count=0
while count<len(i_ir10D):
	if i_ir10D[count]<1:
		i_ir10D[count]=1
	count=count+1

i_ib10D=i_ir10D


#torcional
i_tr10D=np.array([1.0, 1, 1, 1])
i_tb10D=np.array([1.0, 1, 1, 1])

#SIF conforme B31J
#PRINCIPAL

#no plano
i_ir10J=0.98*(R/T)**.35*(d/D)**.72*(t/T)**(-.52)
#nenhum SIF menor que 1
count=0
while count<len(i_ir10J):
	if i_ir10J[count]<1:
		i_ir10J[count]=1
	count=count+1

#fora do plano
i_or10J=0.61*(R/T)**(.29)*(d/D)**(1.95)*(t/T)**(-.53)
#nenhum SIF menor que 1
count=0
while count<len(i_or10J):
	if i_or10J[count]<1:
		i_or10J[count]=1
	count=count+1

#torcional
i_tr10J=0.34*(R/T)**(2/3)*(d/D)*(t/T)**(-.5)
#nenhum SIF menor que 1
count=0
while count<len(i_tr10J):
	if i_tr10J[count]<1:
		i_tr10J[count]=1
	count=count+1


#RAMAL

#no plano
i_ib10J=0.33*(R/T)**(2/3)*(d/D)**.18*(t/T)**(0.7)
#nenhum SIF menor que 1
count=0
while count<len(i_ib10J):
	if i_ib10J[count]<1:
		i_ib10J[count]=1
	count=count+1

#fora do plano
i_ob10J=0.42*(R/T)**(2/3)*(d/D)**0.37*(t/T)**(0.37)
#nenhum SIF menor que 1
count=0
while count<len(i_ob10J):
	if i_ob10J[count]<1:
		i_ob10J[count]=1
	count=count+1

#torcional
i_tb10J=0.42*(R/T)**(2/3)*(d/D)**1.1*(t/T)**(1.1)
#nenhum SIF menor que 1
count=0
while count<len(i_tb10J):
	if i_tb10J[count]<1:
		i_tb10J[count]=1
	count=count+1

#----------------------CONDIÇÕES DO B31J para o caso 2.1 --------------#
#SE i_ob<i_ib, fazer i_ob=i_ib
count=0
while count<len(i_ob10J):
	if i_ob10J[count]<i_ib10J[count]:
		i_ob10J[count]=i_ib10J[count]
	count=count+1

#SE i_ir<i_or, fazer i_ir=i_or
count=0
while count<len(i_ir10J):
	if i_ir10J[count]<i_or10J[count]:
		i_ir10J[count]=i_or10J[count]
	count=count+1


##obtendo medias para os sifs
#principal
i_irM10D=np.average(i_ir10D)
i_irM10J=np.average(i_ir10J)
i_orM10D=np.average(i_or10D)
i_orM10J=np.average(i_or10J)
i_trM10D=np.average(i_tr10D)
i_trM10J=np.average(i_tr10J)

#ramal
i_ibM10D=np.average(i_ib10D)
i_ibM10J=np.average(i_ib10J)
i_obM10D=np.average(i_ob10D)
i_obM10J=np.average(i_ob10J)
i_tbM10D=np.average(i_tb10D)
i_tbM10J=np.average(i_tb10J)

##obtendo medias para flexibilidade
#principal

k_irMJ10=np.average(k_irJ10)
k_orMJ10=np.average(k_orJ10)
k_trMJ10=np.average(k_trJ10)

#ramal

k_ibMJ10=np.average(k_ibJ10)
k_obMJ10=np.average(k_obJ10)
k_tbMJ10=np.average(k_tbJ10)


##plotando
#FLEXIBILIDADE
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6), sharey=True)
for ax in fig.get_axes():
    ax.label_outer()


ax1.plot(nps, k_irJ10, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ir}$, B31J')
ax1.plot(nps, k_orJ10, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{or}$, B31J')
ax1.plot(nps, k_trJ10, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tr}$, B31J')

ax2.plot(nps, k_ibJ10, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ib}$, B31J')
ax2.plot(nps, k_obJ10, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{ob}$, B31J')
ax2.plot(nps, k_tbJ10, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tb}$, B31J')

#ax2.set_ylabel('Fator de flexibilidade no ramal $(i_{ib}, i_{ob}, i_{tb})$')
ax1.set_ylabel('Fator de flexibilidade na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')

secax= ax.secondary_yaxis('right')
secax.set_ylabel('Fator de flexibilidade no ramal $(i_{ib}, i_{ob}, i_{tb})$')


ax2.set_xlabel('NPS')
ax1.set_xlabel('NPS')
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()

ax1.legend(bbox_to_anchor=(.98, 0, 1, 1), loc='upper left')
ax2.legend(bbox_to_anchor=(-.98, 0, 1, 1), loc='lower right')
           
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.subplots_adjust(wspace=.37)

plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 2.1/Figurak1.eps', format='eps')

#SIFS
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
for ax in fig.get_axes():
    ax.label_outer()


ax1.plot(nps, i_ir10D, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, Ap.D')
ax1.plot(nps, i_ir10J, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, B31J')
ax1.plot(nps, i_or10D, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, Ap.D')
ax1.plot(nps, i_or10J, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, B31J')
ax1.plot(nps, i_tr10D, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, Ap.D')
ax1.plot(nps, i_tr10J, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, B31J')

ax2.plot(nps, i_ib10D, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, Ap.D')
ax2.plot(nps, i_ib10J, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, B31J')
ax2.plot(nps, i_ob10D, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, Ap.D')
ax2.plot(nps, i_ob10J, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, B31J')
ax2.plot(nps, i_tb10D, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, Ap.D')
ax2.plot(nps, i_tb10J, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, B31J')

ax2.set_ylabel('SIFs no ramal $(i_{ib}, i_{ob}, i_{tb})$')
ax1.set_ylabel('SIFs na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')
ax2.set_xlabel('NPS')
ax1.set_xlabel('NPS')
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()

ax1.legend(bbox_to_anchor=(.98, 0, 1, 1), loc='upper left')
ax2.legend(bbox_to_anchor=(-.98, 0, 1, 1), loc='lower right')
           
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.subplots_adjust(wspace=.37)

plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 2.1/Figura1.eps', format='eps')

######################################## B A S E ################################################


# -------------------------------------- NPS PRINCIPAL DE 14 ---------------------------------
#nps, diâmetro externo e espessura para principal com NPS 14-- obtidos da ASME B31.10M
nps=np.array(['14x14x12', '14x14x10', '14x14x8', '14x14x6'])

T=np.array([11.13, 11.13, 11.13, 11.13])
D_o=np.array([355.6, 355.6, 355.6, 355.6])

t=np.array([10.31, 9.27, 8.74, 7.11])
d_o=np.array([323.8, 273.0, 219.1, 168.3])

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
k_irJ10=0.18*(R/T)**0.8*(d/D)**5
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_irJ10):
	if k_irJ10[count]<1:
		k_irJ10[count]=1
	count=count+1


#fora do plano=1, mas precisa criar lista da mesma dimensão com vários uns.
k_orJ10=(0*R)+1

#torcional
k_trJ10=0.08*(R/T)**0.91*(d/D)**5.7
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_trJ10):
	if k_trJ10[count]<1:
		k_trJ10[count]=1
	count=count+1

#RAMAL

#no plano
k_ibJ10=(1.91*(d/D)-4.32*(d/D)**2+2.7*(d/D)**3)*(R/T)**.77*(d/D)**.47*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_ibJ10):
	if k_ibJ10[count]<1:
		k_ibJ10[count]=1
	count=count+1

#fora do plano
k_obJ10=(0.34*(d/D)-0.49*(d/D)**2+0.18*(d/D)**3)*(R/T)**1.46*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_obJ10):
	if k_obJ10[count]<1:
		k_obJ10[count]=1
	count=count+1

#torcional
k_tbJ10=(1.08*(d/D)-2.44*(d/D)**2+1.52*(d/D)**3)*(R/T)**.77*(d/D)**1.61*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_tbJ10):
	if k_tbJ10[count]<1:
		k_tbJ10[count]=1
	count=count+1

#SIF conforme APÊNDICE D

#carcaterística de flexibilidade
h=3.1*(T/R)

#SIF - principal e ramal são iguais
#fora do plano
i_or10D=0.9/(h**(2/3))
#nenhum SIF menor que 1
count=0
while count<len(i_or10D):
	if i_or10D[count]<1:
		i_or10D[count]=1
	count=count+1
i_ob10D=i_or10D


#no plano
i_ir10D=(3/4)*(0.9/(h**(2/3)))+(1/4)
#nenhum SIF menor que 1
count=0
while count<len(i_ir10D):
	if i_ir10D[count]<1:
		i_ir10D[count]=1
	count=count+1

i_ib10D=i_ir10D


#torcional
i_tr10D=np.array([1.0, 1, 1, 1])
i_tb10D=np.array([1.0, 1, 1, 1])

#SIF conforme B31J
#PRINCIPAL

#no plano
i_ir10J=0.98*(R/T)**.35*(d/D)**.72*(t/T)**(-.52)
#nenhum SIF menor que 1
count=0
while count<len(i_ir10J):
	if i_ir10J[count]<1:
		i_ir10J[count]=1
	count=count+1

#fora do plano
i_or10J=0.61*(R/T)**(.29)*(d/D)**(1.95)*(t/T)**(-.53)
#nenhum SIF menor que 1
count=0
while count<len(i_or10J):
	if i_or10J[count]<1:
		i_or10J[count]=1
	count=count+1

#torcional
i_tr10J=0.34*(R/T)**(2/3)*(d/D)*(t/T)**(-.5)
#nenhum SIF menor que 1
count=0
while count<len(i_tr10J):
	if i_tr10J[count]<1:
		i_tr10J[count]=1
	count=count+1


#RAMAL

#no plano
i_ib10J=0.33*(R/T)**(2/3)*(d/D)**.18*(t/T)**(0.7)
#nenhum SIF menor que 1
count=0
while count<len(i_ib10J):
	if i_ib10J[count]<1:
		i_ib10J[count]=1
	count=count+1

#fora do plano
i_ob10J=0.42*(R/T)**(2/3)*(d/D)**0.37*(t/T)**(0.37)
#nenhum SIF menor que 1
count=0
while count<len(i_ob10J):
	if i_ob10J[count]<1:
		i_ob10J[count]=1
	count=count+1

#torcional
i_tb10J=0.42*(R/T)**(2/3)*(d/D)**1.1*(t/T)**(1.1)
#nenhum SIF menor que 1
count=0
while count<len(i_tb10J):
	if i_tb10J[count]<1:
		i_tb10J[count]=1
	count=count+1

#----------------------CONDIÇÕES DO B31J para o caso 2.1 --------------#
#SE i_ob<i_ib, fazer i_ob=i_ib
count=0
while count<len(i_ob10J):
	if i_ob10J[count]<i_ib10J[count]:
		i_ob10J[count]=i_ib10J[count]
	count=count+1

#SE i_ir<i_or, fazer i_ir=i_or
count=0
while count<len(i_ir10J):
	if i_ir10J[count]<i_or10J[count]:
		i_ir10J[count]=i_or10J[count]
	count=count+1


##obtendo medias para os SIFs
#principal
i_irM10D=np.append(i_irM10D, np.average(i_ir10D))
i_irM10J=np.append(i_irM10J, np.average(i_ir10J))
i_orM10D=np.append(i_orM10D, np.average(i_or10D))
i_orM10J=np.append(i_orM10J, np.average(i_or10J))
i_trM10D=np.append(i_trM10D, np.average(i_tr10D))
i_trM10J=np.append(i_trM10J, np.average(i_tr10J))

#ramal
i_ibM10D=np.append(i_ibM10D, np.average(i_ib10D))
i_ibM10J=np.append(i_ibM10J, np.average(i_ib10J))
i_obM10D=np.append(i_obM10D, np.average(i_ob10D))
i_obM10J=np.append(i_obM10J, np.average(i_ob10J))
i_tbM10D=np.append(i_tbM10D, np.average(i_tb10D))
i_tbM10J=np.append(i_tbM10J, np.average(i_tb10J))


##obtendo medias para flexibilidade
#principal

k_irMJ10=np.append(k_irMJ10, np.average(k_irJ10))
k_orMJ10=np.append(k_orMJ10, np.average(k_orJ10))
k_trMJ10=np.append(k_trMJ10, np.average(k_trJ10))

#ramal

k_ibMJ10=np.append(k_ibMJ10, np.average(k_ibJ10))
k_obMJ10=np.append(k_obMJ10, np.average(k_obJ10))
k_tbMJ10=np.append(k_tbMJ10, np.average(k_tbJ10))


##plotando
#FLEXIBILIDADE
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6), sharey=True)
for ax in fig.get_axes():
    ax.label_outer()


ax1.plot(nps, k_irJ10, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ir}$, B31J')
ax1.plot(nps, k_orJ10, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{or}$, B31J')
ax1.plot(nps, k_trJ10, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tr}$, B31J')

ax2.plot(nps, k_ibJ10, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ib}$, B31J')
ax2.plot(nps, k_obJ10, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{ob}$, B31J')
ax2.plot(nps, k_tbJ10, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tb}$, B31J')

#ax2.set_ylabel('Fator de flexibilidade no ramal $(i_{ib}, i_{ob}, i_{tb})$')
ax1.set_ylabel('Fator de flexibilidade na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')

secax= ax.secondary_yaxis('right')
secax.set_ylabel('Fator de flexibilidade no ramal $(i_{ib}, i_{ob}, i_{tb})$')


ax2.set_xlabel('NPS')
ax1.set_xlabel('NPS')
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()

ax1.legend(bbox_to_anchor=(.98, 0, 1, 1), loc='upper left')
ax2.legend(bbox_to_anchor=(-.98, 0, 1, 1), loc='lower right')
           
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.subplots_adjust(wspace=.37)

plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 2.1/Figurak2.eps', format='eps')

#SIFS
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
for ax in fig.get_axes():
    ax.label_outer()


ax1.plot(nps, i_ir10D, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, Ap.D')
ax1.plot(nps, i_ir10J, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, B31J')
ax1.plot(nps, i_or10D, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, Ap.D')
ax1.plot(nps, i_or10J, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, B31J')
ax1.plot(nps, i_tr10D, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, Ap.D')
ax1.plot(nps, i_tr10J, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, B31J')

ax2.plot(nps, i_ib10D, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, Ap.D')
ax2.plot(nps, i_ib10J, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, B31J')
ax2.plot(nps, i_ob10D, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, Ap.D')
ax2.plot(nps, i_ob10J, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, B31J')
ax2.plot(nps, i_tb10D, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, Ap.D')
ax2.plot(nps, i_tb10J, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, B31J')

ax2.set_ylabel('SIFs no ramal $(i_{ib}, i_{ob}, i_{tb})$')
ax1.set_ylabel('SIFs na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')
ax2.set_xlabel('NPS')
ax1.set_xlabel('NPS')
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()


ax1.legend(bbox_to_anchor=(.98, 0, 1, 1), loc='upper left')
ax2.legend(bbox_to_anchor=(-.98, 0, 1, 1), loc='lower right')
           
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.subplots_adjust(wspace=.37)


plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 2.1/Figura2.eps', format='eps')

# -------------------------------------- NPS PRINCIPAL DE 18 ---------------------------------
#nps, diâmetro externo e espessura para principal com NPS 10-- obtidos da ASME B31.10M
nps=np.array(['18x18x16', '18x18x14', '18x18x12', '18x18x10'])

T=np.array([14.27, 14.27, 14.27, 14.27])
D_o=np.array([457, 457, 457, 457])

t=np.array([12.70, 11.13, 10.31, 9.27])
d_o=np.array([406.4, 355.6, 323.8, 273.0])

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
k_irJ10=0.18*(R/T)**0.8*(d/D)**5
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_irJ10):
	if k_irJ10[count]<1:
		k_irJ10[count]=1
	count=count+1


#fora do plano=1, mas precisa criar lista da mesma dimensão com vários uns.
k_orJ10=(0*R)+1

#torcional
k_trJ10=0.08*(R/T)**0.91*(d/D)**5.7
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_trJ10):
	if k_trJ10[count]<1:
		k_trJ10[count]=1
	count=count+1

#RAMAL

#no plano
k_ibJ10=(1.91*(d/D)-4.32*(d/D)**2+2.7*(d/D)**3)*(R/T)**.77*(d/D)**.47*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_ibJ10):
	if k_ibJ10[count]<1:
		k_ibJ10[count]=1
	count=count+1

#fora do plano
k_obJ10=(0.34*(d/D)-0.49*(d/D)**2+0.18*(d/D)**3)*(R/T)**1.46*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_obJ10):
	if k_obJ10[count]<1:
		k_obJ10[count]=1
	count=count+1

#torcional
k_tbJ10=(1.08*(d/D)-2.44*(d/D)**2+1.52*(d/D)**3)*(R/T)**.77*(d/D)**1.61*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_tbJ10):
	if k_tbJ10[count]<1:
		k_tbJ10[count]=1
	count=count+1

#SIF conforme APÊNDICE D

#carcaterística de flexibilidade
h=3.1*(T/R)

#SIF - principal e ramal são iguais
#fora do plano
i_or10D=0.9/(h**(2/3))
#nenhum SIF menor que 1
count=0
while count<len(i_or10D):
	if i_or10D[count]<1:
		i_or10D[count]=1
	count=count+1
i_ob10D=i_or10D


#no plano
i_ir10D=(3/4)*(0.9/(h**(2/3)))+(1/4)
#nenhum SIF menor que 1
count=0
while count<len(i_ir10D):
	if i_ir10D[count]<1:
		i_ir10D[count]=1
	count=count+1

i_ib10D=i_ir10D


#torcional
i_tr10D=np.array([1.0, 1, 1, 1])
i_tb10D=np.array([1.0, 1, 1, 1])

#SIF conforme B31J
#PRINCIPAL

#no plano
i_ir10J=0.98*(R/T)**.35*(d/D)**.72*(t/T)**(-.52)
#nenhum SIF menor que 1
count=0
while count<len(i_ir10J):
	if i_ir10J[count]<1:
		i_ir10J[count]=1
	count=count+1

#fora do plano
i_or10J=0.61*(R/T)**(.29)*(d/D)**(1.95)*(t/T)**(-.53)
#nenhum SIF menor que 1
count=0
while count<len(i_or10J):
	if i_or10J[count]<1:
		i_or10J[count]=1
	count=count+1

#torcional
i_tr10J=0.34*(R/T)**(2/3)*(d/D)*(t/T)**(-.5)
#nenhum SIF menor que 1
count=0
while count<len(i_tr10J):
	if i_tr10J[count]<1:
		i_tr10J[count]=1
	count=count+1


#RAMAL

#no plano
i_ib10J=0.33*(R/T)**(2/3)*(d/D)**.18*(t/T)**(0.7)
#nenhum SIF menor que 1
count=0
while count<len(i_ib10J):
	if i_ib10J[count]<1:
		i_ib10J[count]=1
	count=count+1

#fora do plano
i_ob10J=0.42*(R/T)**(2/3)*(d/D)**0.37*(t/T)**(0.37)
#nenhum SIF menor que 1
count=0
while count<len(i_ob10J):
	if i_ob10J[count]<1:
		i_ob10J[count]=1
	count=count+1

#torcional
i_tb10J=0.42*(R/T)**(2/3)*(d/D)**1.1*(t/T)**(1.1)
#nenhum SIF menor que 1
count=0
while count<len(i_tb10J):
	if i_tb10J[count]<1:
		i_tb10J[count]=1
	count=count+1

#----------------------CONDIÇÕES DO B31J para o caso 2.1 --------------#
#SE i_ob<i_ib, fazer i_ob=i_ib
count=0
while count<len(i_ob10J):
	if i_ob10J[count]<i_ib10J[count]:
		i_ob10J[count]=i_ib10J[count]
	count=count+1

#SE i_ir<i_or, fazer i_ir=i_or
count=0
while count<len(i_ir10J):
	if i_ir10J[count]<i_or10J[count]:
		i_ir10J[count]=i_or10J[count]
	count=count+1


##obtendo medias para os sifs
#principal
i_irM10D=np.append(i_irM10D, np.average(i_ir10D))
i_irM10J=np.append(i_irM10J, np.average(i_ir10J))
i_orM10D=np.append(i_orM10D, np.average(i_or10D))
i_orM10J=np.append(i_orM10J, np.average(i_or10J))
i_trM10D=np.append(i_trM10D, np.average(i_tr10D))
i_trM10J=np.append(i_trM10J, np.average(i_tr10J))
#ramal
i_ibM10D=np.append(i_ibM10D, np.average(i_ib10D))
i_ibM10J=np.append(i_ibM10J, np.average(i_ib10J))
i_obM10D=np.append(i_obM10D, np.average(i_ob10D))
i_obM10J=np.append(i_obM10J, np.average(i_ob10J))
i_tbM10D=np.append(i_tbM10D, np.average(i_tb10D))
i_tbM10J=np.append(i_tbM10J, np.average(i_tb10J))


##obtendo medias para flexibilidade
#principal

k_irMJ10=np.append(k_irMJ10, np.average(k_irJ10))
k_orMJ10=np.append(k_orMJ10, np.average(k_orJ10))
k_trMJ10=np.append(k_trMJ10, np.average(k_trJ10))

#ramal

k_ibMJ10=np.append(k_ibMJ10, np.average(k_ibJ10))
k_obMJ10=np.append(k_obMJ10, np.average(k_obJ10))
k_tbMJ10=np.append(k_tbMJ10, np.average(k_tbJ10))


##plotando
#FLEXIBILIDADE
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6), sharey=True)
for ax in fig.get_axes():
    ax.label_outer()


ax1.plot(nps, k_irJ10, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ir}$, B31J')
ax1.plot(nps, k_orJ10, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{or}$, B31J')
ax1.plot(nps, k_trJ10, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tr}$, B31J')

ax2.plot(nps, k_ibJ10, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ib}$, B31J')
ax2.plot(nps, k_obJ10, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{ob}$, B31J')
ax2.plot(nps, k_tbJ10, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tb}$, B31J')

#ax2.set_ylabel('Fator de flexibilidade no ramal $(i_{ib}, i_{ob}, i_{tb})$')
ax1.set_ylabel('Fator de flexibilidade na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')

secax= ax.secondary_yaxis('right')
secax.set_ylabel('Fator de flexibilidade no ramal $(i_{ib}, i_{ob}, i_{tb})$')


ax2.set_xlabel('NPS')
ax1.set_xlabel('NPS')
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()

ax1.legend(bbox_to_anchor=(.98, 0, 1, 1), loc='upper left')
ax2.legend(bbox_to_anchor=(-.98, 0, 1, 1), loc='lower right')
           
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.subplots_adjust(wspace=.37)

plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 2.1/Figurak3.eps', format='eps')

#SIFS
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
for ax in fig.get_axes():
    ax.label_outer()


ax1.plot(nps, i_ir10D, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, Ap.D')
ax1.plot(nps, i_ir10J, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, B31J')
ax1.plot(nps, i_or10D, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, Ap.D')
ax1.plot(nps, i_or10J, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, B31J')
ax1.plot(nps, i_tr10D, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, Ap.D')
ax1.plot(nps, i_tr10J, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, B31J')

ax2.plot(nps, i_ib10D, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, Ap.D')
ax2.plot(nps, i_ib10J, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, B31J')
ax2.plot(nps, i_ob10D, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, Ap.D')
ax2.plot(nps, i_ob10J, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, B31J')
ax2.plot(nps, i_tb10D, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, Ap.D')
ax2.plot(nps, i_tb10J, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, B31J')

ax2.set_ylabel('SIFs no ramal $(i_{ib}, i_{ob}, i_{tb})$')
ax1.set_ylabel('SIFs na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')
ax2.set_xlabel('NPS')
ax1.set_xlabel('NPS')
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()


ax1.legend(bbox_to_anchor=(.98, 0, 1, 1), loc='upper left')
ax2.legend(bbox_to_anchor=(-.98, 0, 1, 1), loc='lower right')
           
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.subplots_adjust(wspace=.37)


plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 2.1/Figura3.eps', format='eps')

# -------------------------------------- NPS PRINCIPAL DE 24 ---------------------------------
#nps, diâmetro externo e espessura para principal com NPS 10-- obtidos da ASME B31.10M
nps=np.array(['24x24x20', '24x24x18', '24x24x16', '24x24x14'])

T=np.array([17.48, 17.48, 17.48, 17.48])
D_o=np.array([610, 610, 610, 610])

t=np.array([15.09, 14.27, 12.70, 11.13])
d_o=np.array([508.0, 457.0, 406.4, 355.6])

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
k_irJ10=0.18*(R/T)**0.8*(d/D)**5
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_irJ10):
	if k_irJ10[count]<1:
		k_irJ10[count]=1
	count=count+1


#fora do plano=1, mas precisa criar lista da mesma dimensão com vários uns.
k_orJ10=(0*R)+1

#torcional
k_trJ10=0.08*(R/T)**0.91*(d/D)**5.7
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_trJ10):
	if k_trJ10[count]<1:
		k_trJ10[count]=1
	count=count+1

#RAMAL

#no plano
k_ibJ10=(1.91*(d/D)-4.32*(d/D)**2+2.7*(d/D)**3)*(R/T)**.77*(d/D)**.47*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_ibJ10):
	if k_ibJ10[count]<1:
		k_ibJ10[count]=1
	count=count+1

#fora do plano
k_obJ10=(0.34*(d/D)-0.49*(d/D)**2+0.18*(d/D)**3)*(R/T)**1.46*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_obJ10):
	if k_obJ10[count]<1:
		k_obJ10[count]=1
	count=count+1

#torcional
k_tbJ10=(1.08*(d/D)-2.44*(d/D)**2+1.52*(d/D)**3)*(R/T)**.77*(d/D)**1.61*(t/T)
#nenhum fator de flexibilidade menor que 1
count=0
while count<len(k_tbJ10):
	if k_tbJ10[count]<1:
		k_tbJ10[count]=1
	count=count+1

#SIF conforme APÊNDICE D

#carcaterística de flexibilidade
h=3.1*(T/R)

#SIF - principal e ramal são iguais
#fora do plano
i_or10D=0.9/(h**(2/3))
#nenhum SIF menor que 1
count=0
while count<len(i_or10D):
	if i_or10D[count]<1:
		i_or10D[count]=1
	count=count+1
i_ob10D=i_or10D


#no plano
i_ir10D=(3/4)*(0.9/(h**(2/3)))+(1/4)
#nenhum SIF menor que 1
count=0
while count<len(i_ir10D):
	if i_ir10D[count]<1:
		i_ir10D[count]=1
	count=count+1

i_ib10D=i_ir10D


#torcional
i_tr10D=np.array([1.0, 1, 1, 1])
i_tb10D=np.array([1.0, 1, 1, 1])

#SIF conforme B31J
#PRINCIPAL

#no plano
i_ir10J=0.98*(R/T)**.35*(d/D)**.72*(t/T)**(-.52)
#nenhum SIF menor que 1
count=0
while count<len(i_ir10J):
	if i_ir10J[count]<1:
		i_ir10J[count]=1
	count=count+1

#fora do plano
i_or10J=0.61*(R/T)**(.29)*(d/D)**(1.95)*(t/T)**(-.53)
#nenhum SIF menor que 1
count=0
while count<len(i_or10J):
	if i_or10J[count]<1:
		i_or10J[count]=1
	count=count+1

#torcional
i_tr10J=0.34*(R/T)**(2/3)*(d/D)*(t/T)**(-.5)
#nenhum SIF menor que 1
count=0
while count<len(i_tr10J):
	if i_tr10J[count]<1:
		i_tr10J[count]=1
	count=count+1


#RAMAL

#no plano
i_ib10J=0.33*(R/T)**(2/3)*(d/D)**.18*(t/T)**(0.7)
#nenhum SIF menor que 1
count=0
while count<len(i_ib10J):
	if i_ib10J[count]<1:
		i_ib10J[count]=1
	count=count+1

#fora do plano
i_ob10J=0.42*(R/T)**(2/3)*(d/D)**0.37*(t/T)**(0.37)
#nenhum SIF menor que 1
count=0
while count<len(i_ob10J):
	if i_ob10J[count]<1:
		i_ob10J[count]=1
	count=count+1

#torcional
i_tb10J=0.42*(R/T)**(2/3)*(d/D)**1.1*(t/T)**(1.1)
#nenhum SIF menor que 1
count=0
while count<len(i_tb10J):
	if i_tb10J[count]<1:
		i_tb10J[count]=1
	count=count+1

#----------------------CONDIÇÕES DO B31J para o caso 2.1 --------------#
#SE i_ob<i_ib, fazer i_ob=i_ib
count=0
while count<len(i_ob10J):
	if i_ob10J[count]<i_ib10J[count]:
		i_ob10J[count]=i_ib10J[count]
	count=count+1

#SE i_ir<i_or, fazer i_ir=i_or
count=0
while count<len(i_ir10J):
	if i_ir10J[count]<i_or10J[count]:
		i_ir10J[count]=i_or10J[count]
	count=count+1


##obtendo medias para os sifs
#principal
i_irM10D=np.append(i_irM10D, np.average(i_ir10D))
i_irM10J=np.append(i_irM10J, np.average(i_ir10J))
i_orM10D=np.append(i_orM10D, np.average(i_or10D))
i_orM10J=np.append(i_orM10J, np.average(i_or10J))
i_trM10D=np.append(i_trM10D, np.average(i_tr10D))
i_trM10J=np.append(i_trM10J, np.average(i_tr10J))

#ramal
i_ibM10D=np.append(i_ibM10D, np.average(i_ib10D))
i_ibM10J=np.append(i_ibM10J, np.average(i_ib10J))
i_obM10D=np.append(i_obM10D, np.average(i_ob10D))
i_obM10J=np.append(i_obM10J, np.average(i_ob10J))
i_tbM10D=np.append(i_tbM10D, np.average(i_tb10D))
i_tbM10J=np.append(i_tbM10J, np.average(i_tb10J))


##obtendo medias para flexibilidade
#principal

k_irMJ10=np.append(k_irMJ10, np.average(k_irJ10))
k_orMJ10=np.append(k_orMJ10, np.average(k_orJ10))
k_trMJ10=np.append(k_trMJ10, np.average(k_trJ10))

#ramal

k_ibMJ10=np.append(k_ibMJ10, np.average(k_ibJ10))
k_obMJ10=np.append(k_obMJ10, np.average(k_obJ10))
k_tbMJ10=np.append(k_tbMJ10, np.average(k_tbJ10))


##plotando
#FLEXIBILIDADE
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6), sharey=True)
for ax in fig.get_axes():
    ax.label_outer()


ax1.plot(nps, k_irJ10, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ir}$, B31J')
ax1.plot(nps, k_orJ10, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{or}$, B31J')
ax1.plot(nps, k_trJ10, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tr}$, B31J')

ax2.plot(nps, k_ibJ10, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ib}$, B31J')
ax2.plot(nps, k_obJ10, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{ob}$, B31J')
ax2.plot(nps, k_tbJ10, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tb}$, B31J')

#ax2.set_ylabel('Fator de flexibilidade no ramal $(i_{ib}, i_{ob}, i_{tb})$')
ax1.set_ylabel('Fator de flexibilidade na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')

secax= ax.secondary_yaxis('right')
secax.set_ylabel('Fator de flexibilidade no ramal $(i_{ib}, i_{ob}, i_{tb})$')


ax2.set_xlabel('NPS')
ax1.set_xlabel('NPS')
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()

ax1.legend(bbox_to_anchor=(.98, 0, 1, 1), loc='upper left')
ax2.legend(bbox_to_anchor=(-.98, 0, 1, 1), loc='lower right')
           
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.subplots_adjust(wspace=.37)

plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 2.1/Figurak4.eps', format='eps')

#SIFS
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
for ax in fig.get_axes():
    ax.label_outer()


ax1.plot(nps, i_ir10D, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, Ap.D')
ax1.plot(nps, i_ir10J, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, B31J')
ax1.plot(nps, i_or10D, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, Ap.D')
ax1.plot(nps, i_or10J, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, B31J')
ax1.plot(nps, i_tr10D, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, Ap.D')
ax1.plot(nps, i_tr10J, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, B31J')

ax2.plot(nps, i_ib10D, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, Ap.D')
ax2.plot(nps, i_ib10J, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, B31J')
ax2.plot(nps, i_ob10D, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, Ap.D')
ax2.plot(nps, i_ob10J, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, B31J')
ax2.plot(nps, i_tb10D, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, Ap.D')
ax2.plot(nps, i_tb10J, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, B31J')

ax2.set_ylabel('SIFs no ramal $(i_{ib}, i_{ob}, i_{tb})$')
ax1.set_ylabel('SIFs na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')
ax2.set_xlabel('NPS')
ax1.set_xlabel('NPS')
ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()



ax1.legend(bbox_to_anchor=(.98, 0, 1, 1), loc='upper left')
ax2.legend(bbox_to_anchor=(-.98, 0, 1, 1), loc='lower right')
           
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.subplots_adjust(wspace=.37)


plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 2.1/Figura4.eps', format='eps')

#PLOTANDO VARIAÇÃO DAS MÉDIAS POR NPS DA TUBULAÇÃO PRINCIPAL
#SIFs
npsP=np.array(['10', '14', '18', '24'])

##plotando
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
for ax in fig.get_axes():
    ax.label_outer()


ax1.plot(npsP, i_irM10D, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, Ap.D')
ax1.plot(npsP, i_irM10J, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ir}$, B31J')
ax1.plot(npsP, i_orM10D, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, Ap.D')
ax1.plot(npsP, i_orM10J, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{or}$, B31J')
ax1.plot(npsP, i_trM10D, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, Ap.D')
ax1.plot(npsP, i_trM10J, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tr}$, B31J')


ax2.plot(npsP, i_ibM10D, 'b-', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, Ap.D')
ax2.plot(npsP, i_ibM10J, 'b-', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ib}$, B31J')
ax2.plot(npsP, i_obM10D, 'm:', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, Ap.D')
ax2.plot(npsP, i_obM10J, 'm:', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{ob}$, B31J')
ax2.plot(npsP, i_tbM10D, 'g-.', marker='$D$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, Ap.D')
ax2.plot(npsP, i_tbM10J, 'g-.', marker='$J$', markersize=10, mfc='white', alpha=.7, label='$i_{tb}$, B31J')


ax2.set_ylabel('SIF médio no ramal $(i_{ib}, i_{ob}, i_{tb})$')
ax1.set_ylabel('SIF médio na tubulação principal $(i_{ir}, i_{or}, i_{tr})$')
ax2.set_xlabel('NPS da tubulação principal')
ax1.set_xlabel('NPS da tubulação principal')

ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()

ax1.legend(bbox_to_anchor=(.98, 0, 1, 1), loc='upper left')
ax2.legend(bbox_to_anchor=(-.98, 0, 1, 1), loc='lower right')
           
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.subplots_adjust(wspace=.37)


plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 2.1/Figura5.eps', format='eps')


#SIFs
npsP=np.array(['10', '14', '18', '24'])

##plotando
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6), sharey=True)
for ax in fig.get_axes():
    ax.label_outer()


ax1.plot(npsP, k_irMJ10, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ir}$, B31J')
ax1.plot(npsP, k_orMJ10, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{or}$, B31J')
ax1.plot(npsP, k_trMJ10, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tr}$, B31J')


ax2.plot(npsP, k_ibMJ10, 'b-', marker='$i$', markersize=10, mfc='white', alpha=.7, label='$k_{ib}$, B31J')
ax2.plot(npsP, k_obMJ10, 'm:', marker='$o$', markersize=10, mfc='white', alpha=.7, label='$k_{ob}$, B31J')
ax2.plot(npsP, k_tbMJ10, 'g-.', marker='$t$', markersize=10, mfc='white', alpha=.7, label='$k_{tb}$, B31J')


#ax2.set_ylabel('F. de flex. médios por NPS da tub. principal $(k_{ib}, k_{ob}, k_{tb})$')
secax= ax.secondary_yaxis('right')
secax.set_ylabel('Fator de flex. médio no ramal $(k_{ib}, k_{ob}, k_{tb})$')

ax1.set_ylabel('Fator de flex. médio na tub. principal $(k_{ir}, k_{or}, k_{tr})$')
ax2.set_xlabel('NPS da tubulação principal')
ax1.set_xlabel('NPS da tubulação principal')


ax.yaxis.set_label_position("right")
ax.yaxis.tick_right()



ax1.legend(bbox_to_anchor=(.98, 0, 1, 1), loc='upper left')
ax2.legend(bbox_to_anchor=(-.98, 0, 1, 1), loc='lower right')
           
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.subplots_adjust(wspace=.38)


plt.savefig('/home/zh3ro/CORE/biblioteca/16. python/tcc/imagens/caso 2.1/Figurak5.eps', format='eps')


plt.show()



