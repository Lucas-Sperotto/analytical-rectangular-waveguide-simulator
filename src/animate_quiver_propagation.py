import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ========== CONFIGURAÇÕES ==========
modo = "TE10"
componentes = ("Ex", "Ey")       # ou ("Hx", "Hy")
frequencia = 10e9                # Hz
Nx, Ny, Nz = 41, 41, 21
n_frames = Nz                    # um frame por fatia z
interval = 100                   # tempo entre frames (ms)
# ===================================

c = 299792458
omega = 2 * np.pi * frequencia

# === Funções ===
def carregar_3d(nome_arquivo):
    df = pd.read_csv(nome_arquivo)
    V = np.reshape(df['valor'].values, (Nx, Ny, Nz))
    x = np.unique(df['x'].values)
    y = np.unique(df['y'].values)
    z = np.unique(df['z'].values)
    return V, x, y, z

# === Carregamento dos campos ===
Vx, x_vals, y_vals, z_vals = carregar_3d(f"data/campos/{modo}/{componentes[0]}.csv")
Vy, _, _, _ = carregar_3d(f"data/campos/{modo}/{componentes[1]}.csv")

X, Y = np.meshgrid(x_vals, y_vals, indexing='ij')

# Estimar beta
delta_z = z_vals[1] - z_vals[0]
dz_cos = Vx[0, 0, 1] / Vx[0, 0, 0] if Vx[0, 0, 0] != 0 else 0
k0 = omega / c
beta = np.arccos(dz_cos) / delta_z if abs(dz_cos) <= 1 else k0

# === Inicialização do gráfico ===
fig, ax = plt.subplots(figsize=(8, 6))
U0 = Vx[:, :, 0]
V0 = Vy[:, :, 0]
q = ax.quiver(X, Y, U0, V0, np.sqrt(U0**2 + V0**2), cmap='plasma', pivot='middle')
cbar = fig.colorbar(q)
cbar.set_label('Magnitude')
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title(f"{modo} - Campo vetorial {componentes[0]}/{componentes[1]}")
plt.tight_layout()

# === Função de animação combinada ===
def update(frame):
    t = frame / n_frames * (1 / frequencia)  # tempo em segundos
    iz = frame % Nz
    z = z_vals[iz]

    Ubase = Vx[:, :, iz]
    Vbase = Vy[:, :, iz]
    fator = np.cos(omega * t - beta * z)

    U = Ubase * fator
    V = Vbase * fator
    mag = np.sqrt(U**2 + V**2)

    q.set_UVC(U, V, mag)
    ax.set_title(f"{modo} - {componentes[0]}/{componentes[1]} | z = {z:.4f} m | t = {1e9 * t:.2f} ns")
    return q,

ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=interval, blit=True)

# === Salvar vídeo ===
saida = f"data/campos/{modo}/quiver_propagacao_{componentes[0]}_{componentes[1]}.mp4"
ani.save(saida, writer='ffmpeg', fps=30)
print(f"Animação salva em: {saida}")

plt.show()
