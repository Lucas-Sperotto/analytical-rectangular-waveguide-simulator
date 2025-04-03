# Derivação dos Campos Eletromagnéticos para Modos TE em Guias Retangulares

## 1. Introdução

Neste documento, partimos da solução da equação de Helmholtz para a componente longitudinal $H_z$ no modo TE$_{mn}$, e deduzimos todas as componentes dos campos elétricos e magnéticos $\vec{E}$ e $\vec{H}$ nos eixos $x$, $y$ e $z$.

## 2. Hipóteses e Forma do Campo

Assumimos que:
- O guia é retangular com dimensões $a$ (largura) e $b$ (altura)
- Os campos têm dependência harmônica no tempo: $e^{j\omega t}$
- A propagação é na direção $z$, com dependência $e^{-j\beta z}$

A solução para $H_z$ é:

\[
H_z(x, y, z, t) = H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{j(\omega t - \beta z)}
\]

Para modos TE, temos $E_z = 0$.

## 3. Equações de Maxwell (Forma Fasorial)

Usaremos as seguintes equações:

\begin{align}
\nabla \times \vec{E} &= -j\omega\mu_0 \vec{H} \\
\nabla \times \vec{H} &= j\omega\epsilon_0 \vec{E}
\end{align}

## 4. Componentes dos Campos TE$_{mn}$

A partir das equações de Maxwell, obtemos:

### 4.1 Campos Elétricos

\begin{align}
E_x &= -\frac{j\omega\mu_0}{k_c^2} \frac{\partial H_z}{\partial y} \\
E_y &= \frac{j\omega\mu_0}{k_c^2} \frac{\partial H_z}{\partial x} \\
E_z &= 0
\end{align}

### 4.2 Campos Magnéticos

\begin{align}
H_x &= -\frac{\beta}{k_c^2} \frac{\partial H_z}{\partial x} \\
H_y &= -\frac{\beta}{k_c^2} \frac{\partial H_z}{\partial y} \\
H_z &= H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{j(\omega t - \beta z)}
\end{align}

## 5. Derivadas Parciais de $H_z$

\begin{align}
\frac{\partial H_z}{\partial x} &= -H_0 \left(\frac{m\pi}{a}\right) \sin\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{j(\omega t - \beta z)} \\
\frac{\partial H_z}{\partial y} &= -H_0 \left(\frac{n\pi}{b}\right) \cos\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{j(\omega t - \beta z)}
\end{align}

## 6. Campos Finais (Forma Geral)

Substituindo as derivadas nas expressões dos campos, temos:

### 6.1 Campos Elétricos

\begin{align}
E_x &= j\omega\mu_0 H_0 \frac{n\pi / b}{k_c^2} \cos\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{j(\omega t - \beta z)} \\
E_y &= j\omega\mu_0 H_0 \frac{m\pi / a}{k_c^2} \sin\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{j(\omega t - \beta z)} \\
E_z &= 0
\end{align}

### 6.2 Campos Magnéticos

\begin{align}
H_x &= \beta H_0 \frac{m\pi / a}{k_c^2} \sin\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{j(\omega t - \beta z)} \\
H_y &= \beta H_0 \frac{n\pi / b}{k_c^2} \cos\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{j(\omega t - \beta z)} \\
H_z &= H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{j(\omega t - \beta z)}
\end{align}

---

> Essas expressões podem ser implementadas numericamente para calcular os campos em cada ponto do guia, dado um modo $TE_{mn}$, com seus respectivos índices $m$, $n$, dimensões $a$, $b$, e frequência $f$. Em simulações, é comum usar a parte real desses campos para representar o valor físico no tempo.

