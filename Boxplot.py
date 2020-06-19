import matplotlib.pyplot as plt
import random

vetor = []

for i in range(30):
    num = random.randint(0,100)
    vetor.append(num)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()