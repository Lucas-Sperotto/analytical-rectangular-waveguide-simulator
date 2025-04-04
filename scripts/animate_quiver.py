import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ========== CONFIGURAÇÕES ==========
modo = "TE10"
componentes = ("Ex", "Ey")     # ou ("Hx", "Hy")
frequencia = 10e9              # Hz
Nx, Ny, Nz = 41, 41, 41
z_val = 0.0                    # valor fixo de z
n_frames = 90
interval = 200                 # ms entre frames
# ===================================

c = 299792458
omega = 2 * np.pi * frequencia

# Função para carregar campo e reorganizar
def carregar_3d(nome_arquivo, Nx, Ny, Nz):
    df = pd.read_csv(nome_arquivo)
    V = np.reshape(df['valor'].values, (Nx, Ny, Nz))
    x = np.unique(df['x'].values)
    y = np.unique(df['y'].values)
    z = np.unique(df['z'].values)
    return V, x, y, z

# Carregar campos
Vx, x_vals, y_vals, z_vals = carregar_3d(f"data/campos/{modo}/{componentes[0]}.csv", Nx, Ny, Nz)
Vy, _, _, _ = carregar_3d(f"data/campos/{modo}/{componentes[1]}.csv", Nx, Ny, Nz)

# Seleciona fatia em z
iz = np.argmin(np.abs(z_vals - z_val))
U0 = Vx[:, :, iz]
V0 = Vy[:, :, iz]

X, Y = np.meshgrid(x_vals, y_vals, indexing='ij')

# Figura
fig, ax = plt.subplots(figsize=(8, 6))
q = ax.quiver(X, Y, U0, V0, np.sqrt(U0**2 + V0**2), cmap='plasma', pivot='middle')
cbar = fig.colorbar(q)
cbar.set_label('Magnitude')
ax.set_title(f"{modo} - Campo vetorial {componentes[0]}/{componentes[1]}")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
plt.tight_layout()

# Função de atualização no tempo
def update(frame):
    t = frame / n_frames * (1 / frequencia)
    fator = np.cos(omega * t)
    U = U0 * fator
    V = V0 * fator
    mag = np.sqrt(U**2 + V**2)
    q.set_UVC(U, V, mag)
    ax.set_title(f"{modo} - {componentes[0]}/{componentes[1]} | t = {1e9 * t:.2f} ns")
    return q,

ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=interval, blit=True)

# Salvar vídeo
saida = f"data/campos/{modo}/quiver_{componentes[0]}_{componentes[1]}.mp4"
ani.save(saida, writer='ffmpeg', fps=30)
print(f"Animação salva em: {saida}")

plt.show()
