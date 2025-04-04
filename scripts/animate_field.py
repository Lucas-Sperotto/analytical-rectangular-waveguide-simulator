import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ========== CONFIGURAÇÕES ==========
modo = "TE10"
componente = "Hz"
plano = 'z'              # plano de corte: 'x', 'y', ou 'z'
valor_fatia = 0.0        # valor fixo do corte (ex: z = 0.0)
Nx, Ny, Nz = 41, 41, 41  # mesma resolução usada no C++
frequencia = 10e9        # frequência da onda (Hz)
n_frames = 60            # número de frames na animação
interval = 100           # intervalo entre frames (ms)
# ===================================

# Constantes
c = 299792458
omega = 2 * np.pi * frequencia

# Caminho e leitura
caminho = f"data/campos/{modo}/{componente}.csv"
if not os.path.exists(caminho):
    print(f"Arquivo não encontrado: {caminho}")
    exit()

df = pd.read_csv(caminho)
x_vals = np.unique(df['x'].values)
y_vals = np.unique(df['y'].values)
z_vals = np.unique(df['z'].values)

X = x_vals
Y = y_vals
Z = z_vals

V_raw = np.reshape(df['valor'].values, (Nx, Ny, Nz))

# Selecionar fatia
if plano == 'z':
    idx = np.argmin(np.abs(Z - valor_fatia))
    V0 = V_raw[:, :, idx]
    eixo_x, eixo_y = X, Y
elif plano == 'y':
    idx = np.argmin(np.abs(Y - valor_fatia))
    V0 = V_raw[:, idx, :]
    eixo_x, eixo_y = X, Z
elif plano == 'x':
    idx = np.argmin(np.abs(X - valor_fatia))
    V0 = V_raw[idx, :, :]
    eixo_x, eixo_y = Y, Z
else:
    raise ValueError("Plano inválido: use 'x', 'y' ou 'z'")

# Criação da figura
fig, ax = plt.subplots()
im = ax.imshow(V0.T, cmap='RdBu', origin='lower', extent=[eixo_x[0], eixo_x[-1], eixo_y[0], eixo_y[-1]],
               aspect='auto', animated=True)
cbar = plt.colorbar(im)
cbar.set_label('Valor do campo')
ax.set_title(f"Animação do campo {componente} - {modo}")
ax.set_xlabel(plano + '1')
ax.set_ylabel(plano + '2')

# Função de atualização
def update(frame):
    t = frame / n_frames * (2 * np.pi / omega)  # variação de tempo
    Vt = V0 * np.cos(omega * t)
    im.set_array(Vt.T)
    return [im]

ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=interval, blit=True)

ani.save("animacao.mp4", writer="ffmpeg", fps=30)

plt.tight_layout()
#plt.show()