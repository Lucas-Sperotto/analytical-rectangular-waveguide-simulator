# Deduzindo a Equação de Helmholtz e a Frequência de Corte em Guias de Onda Retangulares

## 1. Introdução

Neste documento, partiremos das equações de Maxwell no vácuo para deduzir a equação de Helmholtz que rege a propagação de campos eletromagnéticos em guias de onda retangulares. A partir disso, obteremos a expressão para a frequência de corte dos modos TE e TM.

## 2. Equações de Maxwell no Vácuo

Considerando regiões sem cargas livres ($\rho = 0$) e sem correntes livres ($\vec{J} = 0$), as equações de Maxwell no vácuo são:

$\nabla \cdot \vec{E} &= 0 $ 
$\nabla \cdot \vec{H} &= 0 \\$
$\nabla \times \vec{E} &= -\mu_0 \frac{\partial \vec{H}}{\partial t} \\$
$\nabla \times \vec{H} &= \epsilon_0 \frac{\partial \vec{E}}{\partial t}$

Assumindo um regime senoidal no tempo, com dependência temporal $e^{j\omega t}$, temos as equações de Maxwell em sua forma fasorial:

\begin{align}
$\nabla \cdot \vec{E} &= 0 \\$
$\nabla \cdot \vec{H} &= 0 \\$
$\nabla \times \vec{E} &= -j\omega\mu_0 \vec{H} \\$
$\nabla \times \vec{H} &= j\omega\epsilon_0 \vec{E}$
$\end{align}$

## 3. Propagação em Guias de Onda

Consideremos a propagação de uma onda eletromagnética em um guia retangular ao longo do eixo $z$. Os campos dependem de $x$, $y$ e $z$, com uma dependência do tipo $e^{-j\beta z}$ na direção da propagação.

Para obter as equações diferenciais parciais que regem as componentes dos campos, substituímos a forma fasorial de Maxwell em suas equações e manipulamos vetorialmente para obter equações escalares.

Vamos focar, por exemplo, na componente longitudinal $H_z$, para os modos TE (Transversais Elétricos), onde $E_z = 0$. Com manipulações vetoriais apropriadas e uso da identidade:

$$
\nabla \times (\nabla \times \vec{H}) = \nabla(\nabla \cdot \vec{H}) - \nabla^2 \vec{H}
$$

e sabendo que $\nabla \cdot \vec{H} = 0$, obtemos:

$$
\nabla^2 \vec{H} + \omega^2 \mu_0 \epsilon_0 \vec{H} = 0
$$

Analogamente, vale para $\vec{E}$:

$$
\nabla^2 \vec{E} + \omega^2 \mu_0 \epsilon_0 \vec{E} = 0
$$

Essa é a equação vetorial de Helmholtz. Para a componente longitudinal $H_z$, obtemos a equação escalar:

$$
\nabla_t^2 H_z + k_c^2 H_z = 0
$$

Onde:
- $\nabla_t^2$ é o Laplaciano transversal: $\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$
- $k_c$ é o número de onda de corte

## 4. Solução da Equação de Helmholtz

Buscando soluções separáveis na forma:

$$
H_z(x, y) = X(x)Y(y)
$$

Substituindo na equação de Helmholtz e separando variáveis, obtemos duas equações diferenciais ordinárias:
$$
\begin{align}
\frac{d^2X}{dx^2} + \left(\frac{m\pi}{a}\right)^2 X &= 0 \\
\frac{d^2Y}{dy^2} + \left(\frac{n\pi}{b}\right)^2 Y &= 0
\end{align}
$$
Com soluções harmônicas (senos e cossenos) que satisfazem as condições de contorno nas paredes condutoras do guia, temos:

$$
H_z(x, y) = H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right)
$$

## 5. Frequência de Corte $f_c$

O número de onda de corte é dado por:

$$
k_c = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}
$$

A constante de propagação na direção $z$ é:

$$
\beta = \sqrt{k_0^2 - k_c^2}, \quad \text{onde } k_0 = \frac{\omega}{c} = \frac{2\pi f}{c}
$$

A frequência de corte é obtida quando $\beta = 0$, ou seja, $k_0 = k_c$, resultando:

$$
f_c = \frac{c}{2} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}
$$

Essa é a frequência abaixo da qual o modo $TE_{mn}$ não se propaga. Para os modos TM, o desenvolvimento é análogo, mas parte da componente longitudinal $E_z$.

---

