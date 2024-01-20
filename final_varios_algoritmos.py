# Gera o boxplot do erro das previsões para cada WTG e calcula o erro absoluto medio
# obtido com o uso dE algoritmoS de regressão a escolha
# Grupo com 3 aterramento de turbinas interconectadas por eletrodo horizontal
# Variacao de +-30% de todos os parâmetros de projeto - distribuicao uniforme


import warnings
warnings.filterwarnings('ignore')
from lightgbm import LGBMRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_percentage_error
import statistics

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.linear_model import RANSACRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel, RBF
import xgboost as xgb
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import ElasticNet

#Rf_total_pred = pd.DataFrame({'Rf1':[], 'Rf2':[], 'Rf3':[]})
Rf_total_pred = pd.DataFrame()
                           
arquivo = pd.read_excel('C:/Users/Alexa/OneDrive/Área de Trabalho/E_first_2.xlsx',sheet_name='0.2')
X = arquivo.iloc[:1000,62:] #68 to mix and 69 to variable k
num_linhas = len(X)
Y = arquivo.iloc[:1000,[3,31,59]]

#Entra aqui com as leituras do alicate terrômetro em cada uma das turbinas:
Zmed_meter = pd.DataFrame({'Zmed1': [37.8], 'Zmed2': [40.5], 'Zmed3': [37.5]})
result = pd.concat([X , Zmed_meter], axis=0)

#Normalizando as variaveis preditoras
normalizador = MinMaxScaler(feature_range=(0,1))
result_norm = pd.DataFrame(normalizador.fit_transform(result))
X_norm = result_norm.iloc[:num_linhas,:]
Zmed_meter_norm = result_norm.iloc[num_linhas:,:]

X_norm_teste = pd.DataFrame()
Y_teste = pd.DataFrame()
Y_pred = pd.DataFrame()


for item in Y:
    y = Y[item]
    print('Turbine', item)
    x_norm_treino, x_norm_teste, y_treino, y_teste = train_test_split(X_norm , y, test_size = 0.30, random_state = 12)#12
    #modelo = LGBMRegressor(n_estimators=177, learning_rate=0.062)
    #modelo = LinearRegression()
    #modelo = Ridge(alpha=0.001)
    #modelo = Lasso(alpha=0.001)
    #modelo = DecisionTreeRegressor(min_samples_split=5, max_depth=3, criterion='mse')
    #modelo = RandomForestRegressor(min_samples_split=5, max_depth=11, min_samples_leaf=4)
    modelo = SVR(kernel='rbf', degree=2, gamma='auto', C=60, epsilon=0.01)
    #modelo = RANSACRegressor(LinearRegression(), max_trials=100, min_samples=50, loss='absolute_loss', residual_threshold=5.0)
    #kernel = DotProduct()
    #modelo = GaussianProcessRegressor(kernel=kernel)
    #modelo = xgb.XGBRegressor(use_label_encoder=False)
    
    modelo.fit(x_norm_treino, y_treino)
    X_norm_teste = pd.concat([X_norm_teste,x_norm_teste], axis=1, ignore_index=True)
    Y_teste = pd.concat([Y_teste,y_teste], axis=1, ignore_index=True)
    
    y_pred = modelo.predict(x_norm_teste)
    Y_pred = pd.concat([Y_pred,pd.Series(y_pred)], axis=1, ignore_index=True)
    
    Rf_pred = modelo.predict(Zmed_meter_norm)
    Rf_total_pred = pd.concat([Rf_total_pred,pd.Series(Rf_pred)], axis=1, ignore_index=True)

from sklearn.metrics import mean_absolute_percentage_error  
erro_brut=  (Y_teste.values-Y_pred.values)/Y_teste.values*100
Erro = abs((Y_teste.values-Y_pred.values)/Y_teste.values*100)
mape = mean_absolute_percentage_error(Y_teste , Y_pred)


#%% Contando os outliers > 10%

ERRO = pd.DataFrame(Erro)
outliers= 0
l=0
while l<Erro.shape[0]:
    for i in ERRO.iloc[l,:]:
        if i > 10: 
            outliers=outliers+1
        else:
                pass
    l=l+1


print('MP Mean Absolute Percentage Error = ', round(mape*100,3), '%') 
print('Percentual de previsões com erro absoluto do MP> 10% = ', round(outliers/(ERRO.shape[0]*ERRO.shape[1])*100,3), '%')


#%% CGM ERRORS - Erros da aplicação direta do método do alicate terrometro

x_teste=pd.DataFrame(normalizador.inverse_transform(x_norm_teste))
mape_cgm = mean_absolute_percentage_error(Y_teste , x_teste)
erro_brut_cgm=  (Y_teste.values-x_teste.values)/Y_teste.values*100
Erro_cgm = abs((Y_teste.values-x_teste.values)/Y_teste.values*100)

ERRO_cgm = pd.DataFrame(Erro_cgm)
outliers_cgm= 0
l=0
while l<Erro_cgm.shape[0]:
    for i in ERRO_cgm.iloc[l,:]:
        if i > 10: 
            outliers_cgm=outliers_cgm+1
        else:
                pass
    l=l+1

print('...')
print('CGM Mean Absolute Percentage Error = ', round(mape_cgm*100,3), '%') 
print('Percentual de previsões com erro absoluto do CGM > 10% = ', round(outliers_cgm/(ERRO_cgm.shape[0]*ERRO_cgm.shape[1])*100,3), '%')


#%% Boxplot do APE das previsões por aerogerador
 
ERRO.columns = Y.columns

plt.boxplot(ERRO, labels=ERRO.columns)
plt.gcf().set_size_inches(40, 20)#tamanho do grafico
plt.xlabel('Wind turbine generator', fontsize=40)
plt.ylabel('APE(%)', fontsize=40)
plt.xticks(fontsize=30)#tamanho da letra dos eixos
plt.xticks(rotation=45)
plt.yticks(fontsize=30)
plt.semilogy()
plt.grid(True)
plt.title('Boxplot of APEs between the real and LGBM estimated ground resistances', fontsize=40)
plt.annotate("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ", xy=(10, 12), xycoords='data', xytext=(0.7, 10.3), textcoords='data', color='red')
plt.show()
plt.close()



#%% Boxplot do APE das previsões por aerogerador PROPOSED SOLUTION

ERRO.columns = Y.columns
desired_order = ['E3', 'E31', 'E59']
ERRO = ERRO[desired_order]

#ERRO.columns = ['SB03', 'OD09', 'OD13','SB08','SB15',	'OD03'	,'SB04','SB05'	,'SB13'	,'SB11',	'SB10'	,'OD08', 'SB01'	,'OD01',	'SB09',	'OD15'	,'SB07',	'SB06'	,'OD05'	,'OD02'	,'SB12'	,'SB02'	,'SB14',	'OD10', 'OD11',	'OD12',	'OD04',	'OD07'	,'OD14'	,'OD06']

# Set the size of the circles for outliers (adjust as needed)
flierprops = dict(markerfacecolor='gray', markersize=2, linestyle='none', marker='o', alpha=0.7)

plt.boxplot(ERRO[desired_order], flierprops=flierprops, labels=ERRO.columns )
plt.gcf().set_size_inches(15, 8)  # Adjust the size of the plot
plt.xlabel('Wind Turbine Generator', fontsize=16)
plt.ylabel('Absolute Percentage Error (%)', fontsize=16)
plt.xticks(rotation=45, fontsize=12)  # Rotate and resize x-axis labels
plt.yticks(fontsize=12)
plt.semilogy()
plt.grid(True)
plt.title('Boxplot of proposed solution estimate error', fontsize=18)


plt.show()
plt.close()

#%% Boxplot do APE das previsões por aerogerador CGM DIRETO

ERRO_cgm.columns = Y.columns
desired_order = ['E3', 'E31', 'E59']
ERRO_cgm = ERRO_cgm[desired_order]

# Set the size of the circles for outliers (adjust as needed)
flierprops = dict(markerfacecolor='gray', markersize=1, linestyle='none', marker='o', alpha=0.7)

plt.boxplot(ERRO_cgm[desired_order], flierprops=flierprops, labels=ERRO_cgm.columns )
plt.gcf().set_size_inches(15, 8)  # Adjust the size of the plot
plt.xlabel('Wind Turbine Generator', fontsize=16)
plt.ylabel('Absolute Percentage Error (%)', fontsize=16)
plt.xticks(rotation=45, fontsize=12)  # Rotate and resize x-axis labels
plt.yticks(fontsize=12)
plt.semilogy()
plt.grid(True)
plt.title('Boxplot of clamp-on meter readings error', fontsize=18)


plt.show()
plt.close()


#%% Previsão da resistência de aterramento das turbinas pelo método proposto

#Medido com MTR-1522 Fall-of_Potential 820Hz (ENTRAR AQUI COM VALORES DE MEDIÇÃO QUE SERÃO OS VALORES REFERÊNCIA PRA COMPARAÇÃO COM OS ESTIMADOS)
Rf1_FoP = 40.00
Rf2_FoP = 49.00
Rf3_FoP = 39.50

APE1 = abs((Rf_total_pred.loc[0, 0]-Rf1_FoP)/Rf1_FoP*100)
APE2 = abs((Rf_total_pred.loc[0, 1]-Rf2_FoP)/Rf2_FoP*100)
APE3 = abs((Rf_total_pred.loc[0, 2]-Rf3_FoP)/Rf3_FoP*100)


print('...')
print('Turbine     Estimated       -->  Expected           -->  APE (%)')
print('Rf1         {:.2f} (Ohms)   '.format(round(Rf_total_pred.loc[0, 0], 2)), '-->  {:.2f} (Ohms)       -->  {:.2f}  '.format(round(Rf1_FoP, 2), APE1))
print('Rf2         {:.2f} (Ohms)   '.format(round(Rf_total_pred.loc[0, 1], 2)), '-->  {:.2f} (Ohms)       -->  {:.2f}  '.format(round(Rf2_FoP, 2), APE2))
print('Rf3         {:.2f} (Ohms)   '.format(round(Rf_total_pred.loc[0, 2], 2)), '-->  {:.2f} (Ohms)       -->  {:.2f}  '.format(round(Rf3_FoP, 2), APE3))