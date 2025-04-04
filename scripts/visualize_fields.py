import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

def carregar_campo(caminho_csv):
    df = pd.read_csv(caminho_csv)
    return df

def reshape_3d(df, Nx, Ny, Nz):
    x = df['x'].unique()
    y = df['y'].unique()
    z = df['z'].unique()

    X = np.reshape(df['x'].values, (Nx, Ny, Nz))
    Y = np.reshape(df['y'].values, (Nx, Ny, Nz))
    Z = np.reshape(df['z'].values, (Nx, Ny, Nz))
    V = np.reshape(df['valor'].values, (Nx, Ny, Nz))
    return X, Y, Z, V

def plot_slice(V, X, Y, eixo='z', plano_valor=0.0, title='Campo'):
    if eixo == 'z':
        idx = np.argmin(np.abs(Z[0,0,:] - plano_valor))
        slice_data = V[:, :, idx]
        extent = [X[0,0,idx], X[-1,0,idx], Y[0,0,idx], Y[0,-1,idx]]
        eixo_x, eixo_y = 'x', 'y'
    elif eixo == 'y':
        idx = np.argmin(np.abs(Y[0,:,0] - plano_valor))
        slice_data = V[:, idx, :]
        extent = [X[0,idx,0], X[-1,idx,0], Z[0,idx,0], Z[0,idx,-1]]
        eixo_x, eixo_y = 'x', 'z'
    elif eixo == 'x':
        idx = np.argmin(np.abs(X[:,0,0] - plano_valor))
        slice_data = V[idx, :, :]
        extent = [Y[idx,0,0], Y[idx,-1,0], Z[idx,0,0], Z[idx,0,-1]]
        eixo_x, eixo_y = 'y', 'z'
    else:
        raise ValueError("Eixo inválido: use 'x', 'y' ou 'z'")

    plt.imshow(slice_data.T, origin='lower', extent=extent, aspect='auto', cmap='RdBu')
    plt.colorbar(label='Valor do campo')
    plt.xlabel(eixo_x)
    plt.ylabel(eixo_y)
    plt.title(title + f' - fatia em {eixo} = {plano_valor}')
    plt.tight_layout()
    plt.savefig("output_plot.png")
    #plt.show()

# ==== CONFIGURAÇÕES DO USUÁRIO ====
modo = "TE10"
componente = "Hz"
plano = 'z'         # fatiar em z (mostrar XY)
valor_fatia = 0.0   # coordenada z em que fatiar
Nx, Ny, Nz = 41, 41, 41  # precisa bater com resolução usada no C++
# ==================================

# Carrega CSV
caminho = f"data/campos/{modo}/{componente}.csv"
if not os.path.exists(caminho):
    print(f"Arquivo não encontrado: {caminho}")
    exit()

df = carregar_campo(caminho)
X, Y, Z, V = reshape_3d(df, Nx, Ny, Nz)

# Plota fatia
plot_slice(V, X, Y, eixo=plano, plano_valor=valor_fatia, title=f"{componente} - {modo}")
