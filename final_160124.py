# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 10:15:13 2022

@author: alexa
"""

import numpy as np
import os
import random
import pandas as pd
import pyautogui
import time
import scipy.io
import matplotlib.pyplot as plt
from scipy.io import loadmat
import shutil
import time
import math

#%% Quantas amostras vc quer ?:
samples_n=1000

#%% Etapa de entrada de parâmetros:

#Parâmetros de projeto
u=0.3 #Sensibilidade dos parametros => 0 para valores de projeto 0.3 para 30% de variação
s_design = 0.029
k_estimated = 0.68677 #Para estimar o k use o k_parameter_estimator.py
radius_turbine1_design = 0.197
radius_turbine2_design = 0.197
radius_turbine3_design = 0.197
height_turbine1_design = 0.43
height_turbine2_design = 0.43
height_turbine3_design = 0.43
ε_design = 7.9686E-11
μ_design = 1.26E-06
length_he1_design = 7.5
length_he2_design = 7.5
radius_he1_design = 0.003337791
radius_he2_design = 0.003337791
deep_he1_design = 0.12
deep_he2_design = 0.12
pcu = 17.2
S_design = 35

#Valores da resistividade aparente no solo
pa_f_design = np.array([81.1, 99.3, 80.1])																																					

'''
# Valores aleatorios 
k =  random.uniform(k_estimated*(1+u),k_estimated*(1-u))
radius_turbine1 = random.uniform(radius_turbine1_design*(1+u),radius_turbine1_design*(1-u))
radius_turbine2 = random.uniform(radius_turbine2_design*(1+u),radius_turbine2_design*(1-u))
radius_turbine3 = random.uniform(radius_turbine3_design*(1+u),radius_turbine3_design*(1-u))
height_turbine1 = random.uniform(height_turbine1_design*(1+u),height_turbine1_design*(1-u))
height_turbine2 = random.uniform(height_turbine2_design*(1+u),height_turbine2_design*(1-u))
height_turbine3 = random.uniform(height_turbine3_design*(1+u),height_turbine3_design*(1-u))
ε = random.uniform(ε_design*(1+u),ε_design*(1-u))
μ = random.uniform(μ_design*(1+u),μ_design*(1-u))
length_he1 = random.uniform(length_he1_design*(1+u),length_he1_design*(1-u))
length_he2 = random.uniform(length_he2_design*(1+u),length_he2_design*(1-u))
radius_he1 = random.uniform(radius_he1_design*(1+u),radius_he1_design*(1-u))
radius_he2 = random.uniform(radius_he2_design*(1+u),radius_he2_design*(1-u))
deep_he1 = random.uniform(deep_he1_design*(1+u),deep_he1_design*(1-u))
deep_he2 = random.uniform(deep_he2_design*(1+u),deep_he2_design*(1-u))
pcu = 17.2
S = random.uniform(S_design*(1+u),S_design*(1-u))
#Valores da resistividade aparente no solo
pa_f = random.uniform(pa_f_design*(1+u),pa_f_design*(1-u))
pa_p = np.array([(pa_f[0]+pa_f[1])/2 , (pa_f[1]+pa_f[2])/2 ])

#pa_p = random.uniform(pa_p_design*(1+u),pa_p_design*(1-u))

Rf = [0,0,0]
Cf = [0,0,0]
Rs = [0,0]
Ls = [0,0]
Rp = [0,0]
Cp = [0,0]
Req = [0,0,0]
Cep = [0,0,0]
Rc = [0,0,0]
Cc = [0,0,0]

radius_hemispherical_turbine1  = math.sqrt(((2 * math.pi * radius_turbine1 * height_turbine1) + (math.pi * radius_turbine1 ** 2)) / (2 * math.pi))
radius_hemispherical_turbine2  = math.sqrt(((2 * math.pi * radius_turbine2 * height_turbine2) + (math.pi * radius_turbine2 ** 2)) / (2 * math.pi))
radius_hemispherical_turbine3  = math.sqrt(((2 * math.pi * radius_turbine3 * height_turbine3) + (math.pi * radius_turbine3 ** 2)) / (2 * math.pi))


Rf[0] = pa_f[0] / (2 * math.pi * radius_hemispherical_turbine1)
Rf[1] = pa_f[1] / (2 * math.pi * radius_hemispherical_turbine2)
Rf[2] = pa_f[2] / (2 * math.pi * radius_hemispherical_turbine3)
Cf[0] = pa_f[0] * ε / Rf[0]
Cf[1] = pa_f[1] * ε / Rf[1]
Cf[2] = pa_f[2] * ε / Rf[2]

Rs[0] = (pcu / S) * (length_he1 / 1000)
Rs[1] = (pcu / S) * (length_he2 / 1000)

Ls[0] = (μ * length_he1) / (2 * math.pi) * (math.log(2 * length_he1 / radius_he1) - 1)
Ls[1] = (μ * length_he2) / (2 * math.pi) * (math.log(2 * length_he2 / radius_he2) - 1)

Rp[0] = (pa_p[0] / (math.pi * length_he1)) * (math.log((2 * length_he1) / (math.sqrt(2 * radius_he1 * deep_he1))) - 1)
Rp[1] = (pa_p[1] / (math.pi * length_he2)) * (math.log((2 * length_he2) / (math.sqrt(2 * radius_he2 * deep_he2))) - 1)
Cp[0] = pa_p[0] * ε / Rp[0]
Cp[1] = pa_p[1] * ε / Rp[1]

#Calculo resistências equivalentes
Req[0] = Rp[0]*2
Cep[0] = Cp[0]/2
Req[1] = 1 / (1 / (2 * Rp[0]) + 1 / (2 * Rp[1]))
Cep[1] = Cp[0] / 2 + Cp[1] / 2
Req[2] = Rp[1]*2
Cep[2] = Cp[1]/2

#Calculo resistências de compensação - acoplamento mutuo

Rc[0] = (Rf[0] + Req[0]) * k / (1 - k)
Rc[1] = (Rf[1] + Req[1]) * k / (1 - k)
Rc[2] = (Rf[2] + Req[2]) * k / (1 - k)

Cc[0] = (1 / (1 / Cf[0] + 1 / Cep[0])) * (1 - k) / k
Cc[1] = (1 / (1 / Cf[1] + 1 / Cep[1])) * (1 - k) / k
Cc[2] = (1 / (1 / Cf[2] + 1 / Cep[2])) * (1 - k) / k


#%% Preparação para alocação dentro do programa

E = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Circuito 1
E[0]=Rc[0]
E[1]=Cc[0]*1e6
E[2]=Rf[0]
E[3]=Cf[0]*1e6
E[4]=2*Rp[0]
E[5]=Cp[0]/2*1e6
E[6]=Rs[0]
E[7]=Ls[0]*1e3
E[8]=Rp[0]*(4-2*k)
E[9]=Cp[0]/(4-2*k)*1e6
E[10]=Rf[1]*(2-k)
E[11]=Cf[1]/(2-k)*1e6
E[12]=Rp[1]*(4-2*k)
E[13]=Cp[1]/(4-2*k)*1e6
E[14]=Rs[1]
E[15]=Ls[1]*1e3
E[16]=Rp[1]*(4-2*k)
E[17]=Cp[1]/(4-2*k)*1e6
E[18]=Rf[2]*(2-k)
E[19]=Cf[2]/(2-k)*1e6

# Circuito 2
E[20]=Rf[0]*(2-k)
E[21]=Cf[0]/(2-k)*1e6
E[22]=Rp[0]*(4-2*k)
E[23]=Cp[0]/(4-2*k)*1e6
E[24]=Rs[0]
E[25]=Ls[0]*1e3
E[26]=2*Rp[0]
E[27]=Cp[0]/2*1e6
E[28]=Rc[1]
E[29]=Cc[1]*1e6
E[30]=Rf[1]
E[31]=Cf[1]*1e6
E[32]=2*Rp[1]
E[33]=Cp[1]/2*1e6
E[34]=Rs[1]
E[35]=Ls[1]*1e3
E[36]=Rp[1]*(4-2*k)
E[37]=Cp[1]/(4-2*k)*1e6
E[38]=Rf[2]*(2-k)
E[39]=Cf[2]/(2-k)*1e6


# Circuito 3
E[40]=Rf[0]*(2-k)
E[41]=Cf[0]/(2-k)*1e6
E[42]=Rp[0]*(4-2*k)
E[43]=Cp[0]/(4-2*k)*1e6
E[44]=Rs[0]
E[45]=Ls[0]*1e3
E[46]=Rp[0]*(4-2*k)
E[47]=Cp[0]/(4-2*k)*1e6
E[48]=Rf[1]*(2-k)
E[49]=Cf[1]/(2-k)*1e6
E[50]=Rp[1]*(4-2*k)
E[51]=Cp[1]/(4-2*k)*1e6
E[52]=Rs[1]
E[53]=Ls[1]*1e3
E[54]=Rp[1]*2
E[55]=Cp[1]/2*1e6
E[56]=Rc[2]
E[57]=Cc[2]*1e6
E[58]=Rf[2]
E[59]=Cf[2]*1e6'''



#%%

#Dataframes que conterão os valores dos componentes do circuito
E_df_float = pd.DataFrame({'E1':[], 'E2':[], 'E3':[], 'E4':[], 'E5':[], 'E6':[], 'E7':[], 'E8':[], 'E9':[], 'E10':[], 'E11':[], 'E12':[], 'E13':[], 'E14':[], 'E15':[], 'E16':[], 'E17':[], 'E18':[], 'E19':[], 'E20':[], 'E21':[], 'E22':[], 'E23':[], 'E24':[], 'E25':[], 'E26':[], 'E27':[], 'E28':[], 'E29':[], 'E30':[],'E31':[], 'E32':[], 'E33':[], 'E34':[], 'E35':[], 'E36':[], 'E37':[], 'E38':[], 'E39':[], 'E40':[],'E41':[], 'E42':[], 'E43':[], 'E44':[], 'E45':[], 'E46':[], 'E47':[], 'E48':[], 'E49':[], 'E50':[], 'E51':[], 'E52':[], 'E53':[], 'E54':[], 'E55':[], 'E56':[], 'E57':[], 'E58':[], 'E59':[], 'E60':[],  'k':[], 'Zmed1':[], 'Zmed2':[], 'Zmed3':[]  })
E_df_new_fixed = pd.DataFrame({'E1':[], 'E2':[], 'E3':[], 'E4':[], 'E5':[], 'E6':[], 'E7':[], 'E8':[], 'E9':[], 'E10':[], 'E11':[], 'E12':[], 'E13':[], 'E14':[], 'E15':[], 'E16':[], 'E17':[], 'E18':[], 'E19':[], 'E20':[], 'E21':[], 'E22':[], 'E23':[], 'E24':[], 'E25':[], 'E26':[], 'E27':[], 'E28':[], 'E29':[], 'E30':[],'E31':[], 'E32':[], 'E33':[], 'E34':[], 'E35':[], 'E36':[], 'E37':[], 'E38':[], 'E39':[], 'E40':[],'E41':[], 'E42':[], 'E43':[], 'E44':[], 'E45':[], 'E46':[], 'E47':[], 'E48':[], 'E49':[], 'E50':[], 'E51':[], 'E52':[], 'E53':[], 'E54':[], 'E55':[], 'E56':[], 'E57':[], 'E58':[], 'E59':[], 'E60':[],  'k':[], 'Zmed1':[], 'Zmed2':[], 'Zmed3':[]  })


index_rf=0
while index_rf<(samples_n):
    #k=random.uniform(0.3, 1)
    print('Amostra', index_rf+1, 'de', samples_n)
    #converte o arquivo que eu vou utilizar para txt.
    shutil.copyfile('C:/Pl42mat09/final.atp','C:/Pl42mat09/final.txt')
    arquivo_original = open('C:/Pl42mat09/final.txt', 'r')
    arquivo_novo = open('C:/Pl42mat09/final_copia.txt', 'a')

    #digitar aqui os valores para propósito posicional no ATP
    E_list_orig = ['10001.','10002.','10003.','10004.','10005.','10006.','10007.','10008.','10009.','10010.','10011.','10012.','10013.','10014.','10015.','10016.','10017.','10018.','10019.','10020.','10021.','10022.','10023.','10024.','10025.','10026.','10027.','10028.','10029.','10030.', '10031.','10032.','10033.','10034.','10035.','10036.','10037.','10038.','10039.','10040.','10041.','10042.','10043.','10044.','10045.','10046.','10047.','10048.','10049.','10050.','10051.','10052.','10053.','10054.','10055.','10056.','10057.','10058.','10059.','10060.']
    
    #lista com o  tamanho de cada string E
    E_list_orig_len = []
    h=0
    while h < len(E_list_orig):
        E_list_orig_len.append(len(E_list_orig[h]))
        h=h+1    
    
    
    # Valores aleatorios 
    k =  random.uniform(k_estimated*(1+u),k_estimated*(1-u))
    radius_turbine1 = random.uniform(radius_turbine1_design*(1+u),radius_turbine1_design*(1-u))
    radius_turbine2 = random.uniform(radius_turbine2_design*(1+u),radius_turbine2_design*(1-u))
    radius_turbine3 = random.uniform(radius_turbine3_design*(1+u),radius_turbine3_design*(1-u))
    height_turbine1 = random.uniform(height_turbine1_design*(1+u),height_turbine1_design*(1-u))
    height_turbine2 = random.uniform(height_turbine2_design*(1+u),height_turbine2_design*(1-u))
    height_turbine3 = random.uniform(height_turbine3_design*(1+u),height_turbine3_design*(1-u))
    ε = random.uniform(ε_design*(1+u),ε_design*(1-u))
    μ = random.uniform(μ_design*(1+u),μ_design*(1-u))
    length_he1 = random.uniform(length_he1_design*(1+u),length_he1_design*(1-u))
    length_he2 = random.uniform(length_he2_design*(1+u),length_he2_design*(1-u))
    radius_he1 = random.uniform(radius_he1_design*(1+u),radius_he1_design*(1-u))
    radius_he2 = random.uniform(radius_he2_design*(1+u),radius_he2_design*(1-u))
    deep_he1 = random.uniform(deep_he1_design*(1+u),deep_he1_design*(1-u))
    deep_he2 = random.uniform(deep_he2_design*(1+u),deep_he2_design*(1-u))
    pcu = 17.2
    S = random.uniform(S_design*(1+u),S_design*(1-u))
    #Valores da resistividade aparente no solo
    pa_f = random.uniform(pa_f_design*(1+u),pa_f_design*(1-u))
    pa_p = np.array([(pa_f[0]+pa_f[1])/2 , (pa_f[1]+pa_f[2])/2 ])

    Rf = [0,0,0]
    Cf = [0,0,0]
    Rs = [0,0]
    Ls = [0,0]
    Rp = [0,0]
    Cp = [0,0]
    Req = [0,0,0]
    Cep = [0,0,0]
    Rc = [0,0,0]
    Cc = [0,0,0]

    radius_hemispherical_turbine1  = math.sqrt(((2 * math.pi * radius_turbine1 * height_turbine1) + (math.pi * radius_turbine1 ** 2)) / (2 * math.pi))
    radius_hemispherical_turbine2  = math.sqrt(((2 * math.pi * radius_turbine2 * height_turbine2) + (math.pi * radius_turbine2 ** 2)) / (2 * math.pi))
    radius_hemispherical_turbine3  = math.sqrt(((2 * math.pi * radius_turbine3 * height_turbine3) + (math.pi * radius_turbine3 ** 2)) / (2 * math.pi))


    Rf[0] = pa_f[0] / (2 * math.pi * radius_hemispherical_turbine1)
    Rf[1] = pa_f[1] / (2 * math.pi * radius_hemispherical_turbine2)
    Rf[2] = pa_f[2] / (2 * math.pi * radius_hemispherical_turbine3)
    Cf[0] = pa_f[0] * ε / Rf[0]
    Cf[1] = pa_f[1] * ε / Rf[1]
    Cf[2] = pa_f[2] * ε / Rf[2]

    Rs[0] = (pcu / S) * (length_he1 / 1000)
    Rs[1] = (pcu / S) * (length_he2 / 1000)

    Ls[0] = (μ * length_he1) / (2 * math.pi) * (math.log(2 * length_he1 / radius_he1) - 1)
    Ls[1] = (μ * length_he2) / (2 * math.pi) * (math.log(2 * length_he2 / radius_he2) - 1)

    Rp[0] = (pa_p[0] / (math.pi * length_he1)) * (math.log((2 * length_he1) / (math.sqrt(2 * radius_he1 * deep_he1))) - 1)
    Rp[1] = (pa_p[1] / (math.pi * length_he2)) * (math.log((2 * length_he2) / (math.sqrt(2 * radius_he2 * deep_he2))) - 1)
    Cp[0] = pa_p[0] * ε / Rp[0]
    Cp[1] = pa_p[1] * ε / Rp[1]

    #Calculo resistências equivalentes
    Req[0] = Rp[0]*2
    Cep[0] = Cp[0]/2
    Req[1] = 1 / (1 / (2 * Rp[0]) + 1 / (2 * Rp[1]))
    Cep[1] = Cp[0] / 2 + Cp[1] / 2
    Req[2] = Rp[1]*2
    Cep[2] = Cp[1]/2

    #Calculo resistências de compensação - acoplamento mutuo

    Rc[0] = (Rf[0] + Req[0]) * k / (1 - k)
    Rc[1] = (Rf[1] + Req[1]) * k / (1 - k)
    Rc[2] = (Rf[2] + Req[2]) * k / (1 - k)

    Cc[0] = (1 / (1 / Cf[0] + 1 / Cep[0])) * (1 - k) / k
    Cc[1] = (1 / (1 / Cf[1] + 1 / Cep[1])) * (1 - k) / k
    Cc[2] = (1 / (1 / Cf[2] + 1 / Cep[2])) * (1 - k) / k


    #Preparação para alocação dentro do programa

    #E = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    E = [0] * 60
    
    # Circuito 1
    E[0]=Rc[0]
    E[1]=Cc[0]*1e6
    E[2]=Rf[0]
    E[3]=Cf[0]*1e6
    E[4]=2*Rp[0]
    E[5]=Cp[0]/2*1e6
    E[6]=Rs[0]
    E[7]=Ls[0]*1e3
    E[8]=Rp[0]*(4-2*k)
    E[9]=Cp[0]/(4-2*k)*1e6
    E[10]=Rf[1]*(2-k)
    E[11]=Cf[1]/(2-k)*1e6
    E[12]=Rp[1]*(4-2*k)
    E[13]=Cp[1]/(4-2*k)*1e6
    E[14]=Rs[1]
    E[15]=Ls[1]*1e3
    E[16]=Rp[1]*(4-2*k)
    E[17]=Cp[1]/(4-2*k)*1e6
    E[18]=Rf[2]*(2-k)
    E[19]=Cf[2]/(2-k)*1e6

    # Circuito 2
    E[20]=Rf[0]*(2-k)
    E[21]=Cf[0]/(2-k)*1e6
    E[22]=Rp[0]*(4-2*k)
    E[23]=Cp[0]/(4-2*k)*1e6
    E[24]=Rs[0]
    E[25]=Ls[0]*1e3
    E[26]=2*Rp[0]
    E[27]=Cp[0]/2*1e6
    E[28]=Rc[1]
    E[29]=Cc[1]*1e6
    E[30]=Rf[1]
    E[31]=Cf[1]*1e6
    E[32]=2*Rp[1]
    E[33]=Cp[1]/2*1e6
    E[34]=Rs[1]
    E[35]=Ls[1]*1e3
    E[36]=Rp[1]*(4-2*k)
    E[37]=Cp[1]/(4-2*k)*1e6
    E[38]=Rf[2]*(2-k)
    E[39]=Cf[2]/(2-k)*1e6


    # Circuito 3
    E[40]=Rf[0]*(2-k)
    E[41]=Cf[0]/(2-k)*1e6
    E[42]=Rp[0]*(4-2*k)
    E[43]=Cp[0]/(4-2*k)*1e6
    E[44]=Rs[0]
    E[45]=Ls[0]*1e3
    E[46]=Rp[0]*(4-2*k)
    E[47]=Cp[0]/(4-2*k)*1e6
    E[48]=Rf[1]*(2-k)
    E[49]=Cf[1]/(2-k)*1e6
    E[50]=Rp[1]*(4-2*k)
    E[51]=Cp[1]/(4-2*k)*1e6
    E[52]=Rs[1]
    E[53]=Ls[1]*1e3
    E[54]=Rp[1]*2
    E[55]=Cp[1]/2*1e6
    E[56]=Rc[2]
    E[57]=Cc[2]*1e6
    E[58]=Rf[2]
    E[59]=Cf[2]*1e6
    
    
    E_list_float_new = E
    
    
    #Conversão de float para string - E

    E_list_new = []
    c=0
    lixo=[]
    for i in E_list_float_new:
        E_list_new.append((str(round(E_list_float_new[c],5))).lstrip('0'))
        c=c+1
        
    #etapa de tratamento para inserção no arquivo txt - para encaixe no atp - Rf
    E_list_new_fixed = []
    h=0
    while h < len(E_list_orig):
        l=E_list_orig_len[h]
        if l==2:
            E_list_new_fixed.append('%.2s' % ((E_list_new[h]).ljust(2, '0')))#trunca o número
        elif l==3:
            E_list_new_fixed.append('%.3s' % ((E_list_new[h]).ljust(3, '0')))#trunca o número
        elif l==4:
            E_list_new_fixed.append('%.4s' % ((E_list_new[h]).ljust(4, '0')))
        elif l==5:
            E_list_new_fixed.append('%.5s' % ((E_list_new[h]).ljust(5, '0')))
        elif l==6:
            E_list_new_fixed.append('%.6s' % ((E_list_new[h]).ljust(6, '0')))     
             
        h=h+1
        
        
       
       
        
        ###############################
    
    
    for linha in arquivo_original:
        i=0
        for item in E_list_orig:
            palavra = E_list_orig[i]
            palavra_nova = E_list_new_fixed[i]
            i=i+1
            if (palavra in linha) == True: #and (palavra_check in linha) == True:
                linha = linha.replace(palavra,palavra_nova)
            else:
                pass
        arquivo_novo.write(linha)

             
    arquivo_original.close()
    arquivo_novo.close()

    os.rename('C:/Pl42mat09/final_copia.txt','C:/Pl42mat09/final_copia.atp')


    #agora vamos rodar o atp
    if index_rf == 0:
        pyautogui.PAUSE = 1
        pyautogui.press('winleft')
        pyautogui.PAUSE = 1
        pyautogui.write('cmd')
        pyautogui.press('enter')
        pyautogui.PAUSE = 1

        pyautogui.write('cd..')
        pyautogui.press('enter')
        pyautogui.PAUSE = 1

        pyautogui.write('cd..')
        pyautogui.press('enter')
        pyautogui.PAUSE = 1

        pyautogui.write('cd pl42mat09')
        pyautogui.press('enter')
        pyautogui.PAUSE = 0.5
    

    pyautogui.write('runATP final_copia.atp')
    pyautogui.press('enter')
    pyautogui.PAUSE = 3
    pyautogui.press('enter')

    pyautogui.write('pl42mat final_copia.pl4')
    pyautogui.press('enter')
      
    time.sleep(0.5)

    
    mat = scipy.io.loadmat('C:/Pl42mat09/final_copia.mat')

    #plt.plot(mat['t'], mat['t39'])

    t = mat['t']
    t1 = mat['t1']
    t2 = mat['t2']
    t3 = mat['t3']
    
    tgeral=[t1,t2,t3]

    wtg = np.linspace(7997,8000,3)
    rf=[]   
    i=7997
    cont=0
    for item in wtg:
        rf.append(float(tgeral[cont][i]))
        i=i+1
        cont=cont+1
        
    
    #armazena valor atual de k dentro do vetor Rp
    E_list_float_new.append(k) 
    
    #armazena valores no dataframe E_df_float
    i=0
    for item in rf:
        E_list_float_new.append(rf[i])
        i=i+1
    
           
    E_df_float.loc[index_rf] = E_list_float_new
    
    #E_df_new_fixed.loc[index_rf] = E_list_new_fixed
         
    os.remove('C:/Pl42mat09/final_copia.atp')

     
    index_rf=index_rf+1

pyautogui.write('TASKKILL /F /IM cmd.exe /T')
pyautogui.press('enter')

#Dataframe principal
E_df_float.to_excel('C:/Users/alexa/OneDrive/Área de Trabalho/E.xlsx')

# Resultados: Rf1=E3 ; Rf2=E31 ; Rf3=E59 

#E_df_new_fixed.to_excel('C:/Users/alexa/OneDrive/Área de Trabalho/E_df_new_fixed.xlsx')
