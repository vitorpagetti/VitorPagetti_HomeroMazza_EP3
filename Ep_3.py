# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 09:56:08 2015

@author: Homero e MLK GETTO
"""

import matplotlib.pyplot as plt
dicionario_infosnutri={}
arquivoalimentos=open('alimentos.csv','r')
alimentos=arquivoalimentos.readlines()



import csv
with open ("alimentos.csv", mode="r") as calorias:
    reader=csv.reader(calorias)
    calorias={rows[0]:rows[2] for rows in reader} # acha o valor das calorias de determinado alimento
    
    
with open ("alimentos.csv", mode="r") as proteinas:
    reader=csv.reader(proteinas)
    proteinas={rows[0]:rows[3] for rows in reader} # acha o valor de proteinas de determinado alimento
    
with open ("alimentos.csv", mode="r") as carbos:
    reader=csv.reader(carbos)
    carbos={rows[0]:rows[4] for rows in reader} # acha o valor de carboidratos de determinado alimento
    
with open ("alimentos.csv", mode="r") as gords:
    reader=csv.reader(gords)
    gords={rows[0]:rows[5] for rows in reader} # acha o valor de gordura de determinado alimento

usuario = open("usuario.csv","r+", encoding = "utf-8").readlines()
info = usuario[1].split(",")
nome = info[0] # pega o nome do usuário
idade = int(info[1]) # pega a idadae
peso = float(info[2]) # pega o peso
sexo = info[3].upper().strip() # pega o sexo
altura = float(info[4])*100 # pega a altura
atividade_fisica = info[5].upper().strip() # pega o nivel de atividade fisica

dieta = []
data = []

with open ("usuario.csv", mode="r") as usuario:
    reader=csv.reader(usuario)
    for i in reader:
        dieta.append(i)
    dieta.pop(0), dieta.pop(0), dieta.pop(0)    
dias = {}

for i in range (len(dieta)):
    
    if not dieta[i][0] in dias:
        dias[dieta[i][0]] = []
    dias[dieta[i][0]].append(dieta[i])  
totaldias=0
for d in dias:
    totaldias+=1
    print(d)
    prot = 0
    carbs = 0
    gord= 0
    cal=0
    for i in range(len(dias[d])):
            cal += float(calorias[dias[d][i][1]])*(float(dias[d][i][2])/100)
            prot += float(proteinas[dias[d][i][1]])*(float(dias[d][i][2])/100)
            carbs += float(carbos[dias[d][i][1]])*(float(dias[d][i][2])/100)
            gord += float(gords[dias[d][i][1]])*(float(dias[d][i][2])/100)

if sexo == "M": #calcula tmb masculino
    tmb = 88.36 + (13.4*peso) + (4.8*altura) - (5.7*idade)
    
elif sexo == "F": #calcula tmb feminino
    tmb = 447.6 + (9.2*peso) + (3.1*altura) - (4.3*idade)
    

if atividade_fisica == "MINIMO":
    necessidade_calorica = tmb*1.2
elif atividade_fisica == "BAIXO":
    necessidade_calorica = tmb*1.375
elif atividade_fisica == "MEDIO":
    necessidade_calorica = tmb*1.55
elif atividade_fisica == "ALTO":
    necessidade_calorica = tmb*1.725
else:
    necessidade_calorica = tmb*1.9
#calculo da necessidade calorica

if altura > 180:
    imc = (1.3 * peso/(altura/100)**2.5)-1
elif 150 < altura <= 180:
    imc = (1.3 * peso/(altura/100)**2.5)
else:
    imc = (1.3 * peso/(altura/100)**2.5)+1


if imc < 18.5:
    print("Você está abaixo do peso")
elif 18.5<= imc <= 24.9:
    print("Você está normal")
elif 24.9< imc <= 29.9:
    print("Você está com sobrepeso")
else: 
    print("Você é obeso")

listadias=[]
for x in range(1,totaldias+1):
    listadias.append(x)

    
    
    
    
import numpy as np


def gráfico_barras_acumuladas():

    
    N = totaldias# number of bins
    
    Gorduras = np.array([0] * N )
    Proteinas = np.array([0] * N )
    Carboidratos = np.array([0] * N )
    Calorias = np.array([0] * N )
    necessidade_caloricaa = np.array([0] * N )
    x=1
    #--- create two histogram. Values of 1 go in Bin 0 ---
    for x in listadias:
        Gorduras[x-1] += gord
    for x in listadias:
        Proteinas[x-1] += prot
    for x in listadias:
        Carboidratos[x-1] += carbs
                
    teste1="Proteina(g)", "Carboidratos(g)", "Gordura(g)"
    #--- display the bar-graph ---      
    ax1 = plt.subplot(111)
    plt.bar( np.arange(0,N)+0.55, Proteinas, 0.3, color='#FFFF00')
    plt.bar( np.arange(0,N)+0.85, Carboidratos, 0.3, color='#008000')
    plt.bar( np.arange(0,N)+1.15, Gorduras, 0.3, color='#3F62F5')
    plt.xlabel( 'Datas' )
    plt.ylabel( 'Quantidade Ingerida' )
    #plt.axis([1, 46, 0, 6])
    plt.legend(teste1,bbox_to_anchor=(1.0, -0.15),ncol=2,fancybox=True, shadow=True)
    plt.xlabel( 'Dias' )
    plt.ylabel( 'Quantidades ingeridas' )
    #Limite dos eixos do gráfico
    ax1.set_xticks(np.arange(1,N+1))
    ax1.set_xticklabels(listadias)
    plt.axis( [0.5, N+0.5, 0, max(Gorduras+Proteinas+Carboidratos)] )
    plt.show()
    
    for x in listadias:
        Calorias[x-1] += cal
    for x in listadias:
        necessidade_caloricaa[x-1] += necessidade_calorica
        
    ax2 = plt.subplot(111)
    plt.bar( np.arange(0,N)+0.55, Calorias, 0.45, color='#FF0350')
    plt.bar( np.arange(0,N)+1, necessidade_caloricaa, 0.45, color='#FF8500')
    teste2="Calorias ingeridas(Kcal)", "Calorias sugeridas(Kcal)"
    #Legenda do gráfico
    plt.legend(teste2,bbox_to_anchor=(1.0, -0.15),ncol=2,fancybox=True, shadow=True)
    plt.xlabel( 'Dias' )
    plt.ylabel( 'Quantidades' )
    #Limite dos eixos do gráfico
    ax2.set_xticks(np.arange(1,N+1))
    ax2.set_xticklabels(listadias)
    plt.axis( [0.5, N+0.5, 0, max(5+ Calorias+necessidade_caloricaa)] )
plt.show()
    

gráfico_barras_acumuladas()