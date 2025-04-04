# Derivação dos Campos Eletromagnéticos – Modos TMₘₙ

Neste documento, apresentamos a derivação passo a passo das componentes dos campos elétricos e magnéticos nos **modos TM (Transversais Magnéticos)** em guias de onda retangulares metálicos.

---

## 1. Condição dos modos TM

Para os modos TM, temos:

- $H_z = 0$
- $E_z \neq 0$

A componente longitudinal do campo elétrico $E_z$ satisfaz a **equação de Helmholtz transversal**:

$$
\nabla_t^2 E_z + k_c^2 E_z = 0
$$

Com solução da forma:

$$
E_z(x, y) = E_0 \sin\left( \frac{m\pi x}{a} \right) \sin\left( \frac{n\pi y}{b} \right)
$$

Sendo $m, n = 1, 2, 3, \dots$ (modos com $m=0$ ou $n=0$ não existem em TM).

---

## 2. Cálculo dos campos transversais a partir de $E_z$

A partir das equações de Maxwell na forma fasorial:

$$
\nabla \times \vec{E} = -j\omega \mu_0 \vec{H}
\quad \text{e} \quad
\nabla \times \vec{H} = j\omega \epsilon_0 \vec{E}
$$

Obtemos:

### Campo magnético

Derivando $E_z$:

$$
\begin{aligned}
H_x &= \frac{j}{\omega\mu_0} \frac{\partial E_z}{\partial y} = \frac{j E_0}{\omega\mu_0} \left( \frac{n\pi}{b} \right) \sin\left( \frac{m\pi x}{a} \right) \cos\left( \frac{n\pi y}{b} \right) e^{j(\omega t - \beta z)} \\
H_y &= -\frac{j}{\omega\mu_0} \frac{\partial E_z}{\partial x} = -\frac{j E_0}{\omega\mu_0} \left( \frac{m\pi}{a} \right) \cos\left( \frac{m\pi x}{a} \right) \sin\left( \frac{n\pi y}{b} \right) e^{j(\omega t - \beta z)} \\
H_z &= 0
\end{aligned}
$$

### Campo elétrico

Derivando novamente $E_z$:

$$
\begin{aligned}
E_x &= -\frac{\beta}{k_c^2} \frac{\partial E_z}{\partial x} = -\frac{\beta E_0}{k_c^2} \left( \frac{m\pi}{a} \right) \cos\left( \frac{m\pi x}{a} \right) \sin\left( \frac{n\pi y}{b} \right) e^{j(\omega t - \beta z)} \\
E_y &= -\frac{\beta}{k_c^2} \frac{\partial E_z}{\partial y} = -\frac{\beta E_0}{k_c^2} \left( \frac{n\pi}{b} \right) \sin\left( \frac{m\pi x}{a} \right) \cos\left( \frac{n\pi y}{b} \right) e^{j(\omega t - \beta z)} \\
E_z &= E_0 \sin\left( \frac{m\pi x}{a} \right) \sin\left( \frac{n\pi y}{b} \right) e^{j(\omega t - \beta z)}
\end{aligned}
$$

---

## 3. Observações

- Para os modos TM, sempre temos $E_z \neq 0$, e $H_z = 0$.
- A frequência de corte é a mesma dos modos TE:

$$
f_c = \frac{c}{2} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}
$$

- Modos TM com $m=0$ ou $n=0$ não existem, pois violam as condições de contorno metálicas (não há corrente para sustentar o campo longitudinal $E_z$).

---

## 4. Conclusão

Os modos TMₘₙ são fundamentais em aplicações onde é necessário um campo elétrico longitudinal. Sua dedução é similar à dos modos TEₘₙ, mas com foco na componente $E_z$.

No projeto, esses campos serão gerados e salvos em arquivos CSV pelo código em C++, com visualização em Python.
