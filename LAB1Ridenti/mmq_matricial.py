# coding: utf-8
import numpy as np
import csv
import matplotlib.pyplot as plt

input_data_file_1 = 'hubble_data.csv'
input_data_file_2 = 'key_project_data.csv'

# Leitura dos dados de notificação acumulada

# Cria array vazio que receberá os valores de distância em Mpc
r = np.array([], dtype=np.float64)
# Cria array vazio que receberá os valores de velocidade em km/s
v = np.array([], dtype=np.float64)

# modifique para input_data_file_1 para analisar os dados originais de Edwin Hubble
with open(input_data_file_2, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    # Desconsidera a linha de cabeçalho (ou header, em inglês)
    next(spamreader, None)
    for row in spamreader:
        r = np.append(r, np.float(row[0]))
        v = np.append(v, np.float(row[1]))

# Monta a matriz projeto

#ones_column = np.ones(len(v), dtype=np.float64)  # vetor coluna 1
X = r  # agrega vetor coluna 1 ao vetor coluna tempo para montar a matriz projeto
# de modelo linear (ajuste de reta com coeficiente angular)


# Obtém solução assumindo S = 1, matriz de covariância unitária

#b = np.linalg.tensorsolve(np.matmul(X.T, X), np.matmul(X.T, v.T))
alpha = np.dot(r,v)/np.dot(r,r)
v_fit = alpha*r  # valores ajustados segundo a solução
v_res = v - v_fit  # resíduos absolutos


_, ax = plt.subplots()
plt.title(u'Ajuste aos dados originais de Hubble')
plt.plot(r, v, 'o')
plt.plot(r, v_fit, '-')
plt.xlabel(u'distância(Mpc)')
plt.ylabel(u'velocidade(km/s)')

_, ax = plt.subplots()
plt.title(u'Gráfico de resíduos')
plt.plot(r, v_res, 'o')
plt.axhline(0)
plt.xlabel(u'distância(Mpc)')
plt.ylabel(u'velocidade(km/s)')

plt.show()

# Estima variância dos dados
chi2 = np.dot(v - v_fit, v - v_fit)
ngl = len(v) - 1
var = chi2 / ngl

# Não é necessário calcular novamente os parâmetros
# Variância constante não afeta a estimativa dos parâme tros

# Calcula a matriz de covariância dos parâmetros
cov = var/np.dot(r,r)

# Calcula constante de Hubble
H0 = alpha
s_H0 = np.sqrt(cov)
print(u'Constante de Hubble = %.2f km/s/Mpc / Incerteza = %.3f km/s/Mpc' % (H0, s_H0))
