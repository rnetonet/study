# cusumdm.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from stream import abrupt_stream as stream

# Plot
plt.ylim(-1.1, 1.1)

# Parâmetros
min_instancias = 30
redutor = 0.005
limite = 50.0

# Algoritmo
n_valores = 1
media = 0
soma = 0

x,y, drifts = [], [], []

for posicao, valor in enumerate(stream):
    media = media + (valor - media) / n_valores
    soma = max(0, soma + valor - media - redutor)
    n_valores += 1

    # plot
    x.append(posicao)
    y.append(media)
    
    if n_valores >= min_instancias and soma > limite:
        # drift
        plt.axvline(x=posicao, color='k', linestyle='--', linewidth=0.5)
        plt.draw()

        # reset
        n_valores = 1
        media = 0
        soma = 0

# plot
plt.plot(x, y, 'r-', linewidth=0.5)
for posicao in drifts:
    plt.axvline(x=posicao, color='k', linestyle='-', linewidth=0.5)
plt.show(block=True)