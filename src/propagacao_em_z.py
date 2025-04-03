import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ========== CONFIGURAÇÕES ==========
modo = "TE10"
componente = "Hz"
Nx, Ny, Nz = 41, 41, 21  # resolução usada no main.cpp
interval = 150           # intervalo entre frames (ms)
# ===================================

# Caminho e leitura
caminho = f"data/campos/{modo}/{componente}.csv"
if not os.path.exists(caminho):
    print(f"Arquivo não encontrado: {caminho}")
    exit()

df = pd.read_csv(caminho)

# Extrai valores únicos
x_vals = np.unique(df['x'].values)
y_vals = np.unique(df['y'].values)
z_vals = np.unique(df['z'].values)

X = x_vals
Y = y_vals
Z = z_vals

# Organiza o campo em 3D
V = np.reshape(df['valor'].values, (Nx, Ny, Nz))

# Configura figura e imagem inicial
fig, ax = plt.subplots()
im = ax.imshow(V[:, :, 0].T, origin='lower', extent=[X[0], X[-1], Y[0], Y[-1]],
               cmap='RdBu', aspect='auto', animated=True)
cbar = plt.colorbar(im)
cbar.set_label('Valor do campo')
ax.set_title(f"Propagação em z – {componente} do modo {modo}")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

# Função de atualização (varia z)
def update(frame):
    frame_idx = frame % Nz
    im.set_array(V[:, :, frame_idx].T)
    ax.set_title(f"{componente} - z = {Z[frame_idx]:.4f} m")
    return [im]

ani = animation.FuncAnimation(fig, update, frames=Nz, interval=interval, blit=True)

plt.tight_layout()
plt.show()
