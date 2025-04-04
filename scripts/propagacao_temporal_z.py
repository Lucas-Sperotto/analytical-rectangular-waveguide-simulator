import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ========== CONFIGURAÇÕES ==========
modo = "TE10"
componente = "Hz"
Nx, Ny, Nz = 41, 41, 21        # mesma resolução usada no C++
frequencia = 10e9              # frequência da onda
n_frames = 60                  # número de quadros
interval = 80                  # tempo entre frames (ms)
# ===================================

# Constantes
c = 299792458
omega = 2 * np.pi * frequencia
k0 = omega / c

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

# Carregar campo base no tempo t=0
V0 = np.reshape(df['valor'].values, (Nx, Ny, Nz))

# Aproximação de beta a partir da variação em z
# (pegamos dois pontos ao longo de z e estimamos beta via cos(beta z))
delta_z = Z[1] - Z[0]
dz_cos = V0[0, 0, 1] / V0[0, 0, 0] if V0[0, 0, 0] != 0 else 0
beta = np.arccos(dz_cos) / delta_z if abs(dz_cos) <= 1 else k0  # fallback

# Figura
fig, ax = plt.subplots()
im = ax.imshow(V0[:, :, 0].T, origin='lower',
               extent=[X[0], X[-1], Y[0], Y[-1]],
               cmap='RdBu', aspect='auto', animated=True)
cbar = plt.colorbar(im)
cbar.set_label('Valor do campo')
ax.set_title(f"Campo {componente} - t = 0.00 ns")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

# Função de atualização
def update(frame):
    t = frame * (1 / frequencia) / n_frames  # tempo para este frame
    campo_frame = np.zeros((Nx, Ny))

    for ix in range(Nx):
        for iy in range(Ny):
            for iz in range(Nz):
                campo_frame[ix, iy] += V0[ix, iy, iz] * np.cos(omega * t - beta * Z[iz])
    campo_frame /= Nz  # média ao longo de z

    im.set_array(campo_frame.T)
    ax.set_title(f"{componente} - t = {1e9 * t:.2f} ns")
    return [im]

# Animação
ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=interval, blit=True)

# Salvar
saida = f"data/campos/{modo}/anim_{componente}_z.mp4"
ani.save(saida, writer='ffmpeg', fps=30)
print(f"Animação salva em: {saida}")

plt.tight_layout()
plt.show()
