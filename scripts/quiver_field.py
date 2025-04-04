import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ========== CONFIGURAÇÕES ==========
modo = "TE10"
componentes = ("Ex", "Ey")     # ou ("Hx", "Hy")
Nx, Ny, Nz = 41, 41, 41        # resolução usada no cálculo
z_val = 0.0                    # fatia em z
# ===================================

# Função para carregar e moldar CSV
def carregar_3d(nome_arquivo, Nx, Ny, Nz):
    df = pd.read_csv(nome_arquivo)
    V = np.reshape(df['valor'].values, (Nx, Ny, Nz))
    x = np.unique(df['x'].values)
    y = np.unique(df['y'].values)
    z = np.unique(df['z'].values)
    return V, x, y, z

# Carrega Ex e Ey
Vx, x_vals, y_vals, z_vals = carregar_3d(f"data/campos/{modo}/{componentes[0]}.csv", Nx, Ny, Nz)
Vy, _, _, _ = carregar_3d(f"data/campos/{modo}/{componentes[1]}.csv", Nx, Ny, Nz)

# Índice da fatia z
iz = np.argmin(np.abs(z_vals - z_val))

# Plano XY
X, Y = np.meshgrid(x_vals, y_vals, indexing='ij')
U = Vx[:, :, iz]
V = Vy[:, :, iz]
magnitude = np.sqrt(U**2 + V**2)

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
q = ax.quiver(X, Y, U, V, magnitude, cmap='plasma', pivot='middle')
cbar = fig.colorbar(q)
cbar.set_label('Magnitude')

ax.set_title(f"Campo vetorial ({componentes[0]}, {componentes[1]}) - {modo} em z = {z_val:.3f} m")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
plt.tight_layout()
plt.savefig("outputQuiver_plot.png")
#plt.show()
