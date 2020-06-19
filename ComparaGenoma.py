entradaBacteria = open("bacteria.fasta").read()
saidaBacteria = open("bacteria.html","w")
entradaHumano = open("human.fasta").read()
saidaHumano = open("humano.html","w")

contBac = {}
contHum = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        contBac[i+j] = 0
        contHum[i+j] = 0

entradaBacteria = entradaBacteria.replace("\n","")
entradaHumano = entradaHumano.replace("\n","")

for k in range(len(entradaBacteria)-1):
    contBac[entradaBacteria[k]+entradaBacteria[k+1]] += 1

for k in range(len(entradaHumano)-1):
    contHum[entradaHumano[k]+entradaHumano[k+1]] += 1

#Exportar em um HTML bactéria

saidaBacteria.write("<div>")

i = 1
for k in contBac:
    transparencia = contBac[k]/max(contBac.values())
    saidaBacteria.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color: rgba(0,0,0,"+str(transparencia)+")'>"+str(k)+" - "+str(contBac[k])+"</div>")

    if i%4==0:
        saidaBacteria.write("<div style='clear:both'></div>")
    i+= 1

saidaBacteria.close()

#Exportar em um HTML humano

saidaHumano.write("<div>")

i = 1
for k in contHum:
    transparencia = contHum[k]/max(contHum.values())
    saidaHumano.write("<div style='width:100px; border:1px solid #111; color:#fff; height:100px; float:left; background-color: rgba(0,0,0,"+str(transparencia)+")'>"+str(k)+" - "+str(contHum[k])+"</div>")

    if i%4==0:
        saidaHumano.write("<div style='clear:both'></div>")
    i+= 1

saidaHumano.close()