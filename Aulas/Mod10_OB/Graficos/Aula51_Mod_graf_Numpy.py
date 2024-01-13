#importando matportlib
import matplotlib.pyplot as plt

#importando modulo numpy
import numpy as np

vendas = np.random.randint(1000, 3000, 50)
meses  = np.arange(1, 51)

#criando grafico 
plt.plot(meses, vendas) #Plota os dados de vendas para cada mes 
plt.axis([0, 50, 0, max(vendas) + 200]) #Define os limites do eixo x e y e valor ligeiramente maior que a venda max
plt.xlabel('Meses') #Adiciona uma etiqueta "Meses" ao eixo x do grafico
plt.ylabel('Vendas') #Adiciona uma etiqueta "Vendas" ao eixo y do grafico
plt.title('Distribuição de Vendas por Mês') #Adiciona titulo ao grafico
plt.show() #Exibe o grafico na tela 
 

#mudando a linha para apenas os marcadores

plt.plot(meses, vendas, color = 'red') #Plota os dados de vendas para cada mes e cor
plt.axis([0, 50, 0, max(vendas) + 200]) #Define os limites do eixo x e y e valor ligeiramente maior que a venda max
plt.xlabel("Meses") #Adiciona uma etiqueta "Meses" ao eixo x do grafico
plt.ylabel("Vendas") #Adiciona uma etiqueta "Vendas" ao eixo y do grafico
plt.title('Distribuição de Vendas por Mês') #Adiciona titulo ao grafico
plt.show() #Exibe o grafico na tela 

#Dispersao 
plt.scatter(meses, vendas) #Cria o grarfico de dispersao, onde valores "meses" eixo x e "vendas" eixo y
plt.title('Distribuição de Vendas por Mês') #Adiciona titulo ao grafico 
plt.show() #Exibe o grafico na tela

#Barras
plt.bar(meses, vendas) #Cria o grafico de barras 
plt.title('Distribuição de Vendas por Mês') #Adiciona titulo ao grafico
plt.show() #Exibe o grafico na tela

#Trabalhando com Multiplos graficos no mesmo "Plot" -> para melhor visualizacao/comparacao
plt.figure(1, figsize = (15, 3)) #Cria um objeto figure com tamento especifico para conter os graficos
plt.subplot(1, 3, 1) #O metodo é usado para criar o primeiro subplot. Os argumentos represetam n total de subplot, n colunas, e indice do subplot
plt.plot(meses, vendas, color='red')  #Plota os dados de vendas para cada mes e cor
plt.title('Grafico 1') #Adiciona titulo ao grafico

plt.subplot(1, 3 , 2) #O metodo é usado para criar o primeiro subplot. Os argumentos represetam n total de subplot, n colunas, e indice do subplot
plt.scatter(meses, vendas) #Cria o grarfico de dispersao, onde valores "meses" eixo x e "vendas" eixo y
plt.title('Grafico 2') #Adiciona titulo ao grafico

plt.subplot(1, 3, 3) #O metodo é usado para criar o primeiro subplot. Os argumentos represetam n total de subplot, n colunas, e indice do subplot
plt.title('Grafico 3') #Adiciona titulo ao grafico
plt.bar(meses, vendas) #Cria o grafico de barras 
plt.show() #Exibe o grafico na tela
