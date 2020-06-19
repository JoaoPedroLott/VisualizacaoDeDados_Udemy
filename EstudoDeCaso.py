import matplotlib.pyplot as plt

dados = open('original.csv').readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

#plt.plot(x,y)
plt.bar(x,y, color="#e4e4e4")
plt.plot(x,y, color="k", linestyle='--')
plt.title("Crescimento da população brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População (Milhão)")
#plt.show()
plt.savefig("Grafico1.png", dpi=300)