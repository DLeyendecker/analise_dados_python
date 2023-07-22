# -*- coding: utf-8 -*-
"""Análise de Empresas de Energia na B3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18ei_Hno9aRynEvlOKtzK0Dd2wd5GrfDF
"""

#bibliotecas
from google.colab import files
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

uploaded = files.upload()

#lendo a base de dados
Base_Dados = pd.read_excel('Dados_Empresas_Energia.xlsx')

#verificando
Base_Dados.head()

#series semporais - Setor o Index
Base_Dados.set_index('Data', inplace=True)

#verificando
Base_Dados.head()

#grafico

#estilo do grafico
plt.style.use('seaborn-darkgrid')

#tamanho
plt.figure(figsize=(16,7))

#titulo
plt.title('Análise de ações das empresas de Energia', loc='left',fontsize=18, fontweight=0)

#plot da petrobras
plt.plot(Base_Dados.index, Base_Dados['Petrobras'], color='#008c4a', linewidth=4, alpha=0.7)

#texto da petrobras
plt.text(Base_Dados.index[-1], Base_Dados['Petrobras'].tail(1), 'Petrobras', color='#008c4a', size='large', horizontalalignment='left')

#plot de todas as colunas
for Coluna in Base_Dados.columns[1:]:
  #plot das outras ações
  plt.plot(Base_Dados.index, Base_Dados[Coluna], color='gray', linewidth=2, alpha=0.7)
  #texto das outras ações
  plt.text(Base_Dados.index[-1], Base_Dados[Coluna].tail(1), Coluna, color='gray', size='large', horizontalalignment='left')



#tabelas
plt.xlabel('Período')
plt.ylabel('Preço de Fechamento (R$)');









