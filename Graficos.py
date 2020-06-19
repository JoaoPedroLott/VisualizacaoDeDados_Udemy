import matplotlib.pyplot as plt

#Grafico básico de linha

x = [1,2,5]
y = [2,3,7]

#Titulo
plt.title('Meu primeiro gráfico com Python')

#Eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.plot(x, y)
plt.show()


#Grafico básico de barras
titulo = 'Gráfico de barras'
eixoX = 'Eixo X'
eixoY = 'Eixo Y'

x1 = [1,3,5,7,9]
y1 = [2,4,6,8,10]

x2 = [3,7,1,5,9]
y2 = [4,8,10,2,6]

#Titulo
plt.title(titulo)

#Eixos
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.bar(x1, y1, label = 'Grupo 1')
plt.bar(x2, y2, label = 'Grupo 2')
plt.legend()
plt.show()

markSize = [100,400,150,305,260]

#Gráfico Scatterplot: gráfico de disperção
plt.title('Scatterplot')
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.scatter(x1,y2, label = 'Meus pontos', color = 'red', marker= '*', s=markSize)
plt.plot(x1,y2, color = 'k', linestyle = '-.')
plt.legend()
plt.show()
plt.savefig("Figura1.png", dpi=300)
plt.savefig("Figura2.pdf")

