# 📡 Simulador Didático de Guias de Onda Retangulares Metálicos

Este repositório contém um projeto completo e didático para o estudo dos modos eletromagnéticos em **guias de onda retangulares metálicos**, com:

- Cálculo analítico dos campos $ \vec{E} $ e $ \vec{H} $ em C++
- Geração e exportação dos dados em arquivos CSV
- Visualizações e animações em Python
- Abordagem teórica detalhada para fins educacionais

> **📚 O projeto pode ser usado em disciplinas de Eletromagnetismo, Física das Ondas, Telecomunicações e Engenharia Elétrica.**

---

## 🧮 Equacionamento teórico

A base teórica do projeto está organizada nos seguintes documentos:

- [`doc/helmholtz.md`](doc/helmholtz.md) — Dedução da equação de Helmholtz e frequência de corte
- [`doc/campos_TE.md`](doc/campos_TE.md) — Derivação dos campos para modos TEₘₙ
- [`doc/campos_TM.md`](doc/campos_TM.md) — Derivação dos campos para modos TMₘₙ

As equações são apresentadas com LaTeX e seguem passo a passo os fundamentos das equações de Maxwell no vácuo.

---

## 🛠️ Organização do projeto

```
src/                     ← Códigos C++ para cálculo
├── calcular_frequencias.cpp
├── calcular_campos.cpp

data/
├── frequencias/        ← fc_lista.csv com modos e frequências de corte
└── campos/             ← Campos Ex, Ey, Hz etc. organizados por modo

scripts/                ← Visualizações e animações em Python
├── visualize_fields.py
├── animate_field.py
├── propagacao_em_z.py
├── quiver_field.py
└── animate_quiver_propagation.py

doc/                    ← Teoria completa
├── helmholtz.md
├── campos_TE.md
├── campos_TM.md
└── figuras/

README.md               ← Este arquivo
```

---

## ⚙️ Como compilar e rodar

### 1. Cálculo das frequências de corte

```bash
g++ -std=c++17 src/calcular_frequencias.cpp -o calcular_frequencias
./calcular_frequencias
```

Isso gera o arquivo `data/frequencias/fc_lista.csv`.

---

### 2. Geração dos campos

```bash
g++ -std=c++17 src/calcular_campos.cpp -o calcular_campos
./calcular_campos
```

Cria os campos em `data/campos/MODO/*.csv`.

---

### 3. Visualização (Python)

Instale dependências:
```bash
pip install numpy pandas matplotlib
```

E execute os scripts desejados, por exemplo:

```bash
python3 scripts/visualize_fields.py
python3 scripts/animate_field.py
python3 scripts/quiver_field.py
python3 scripts/animate_quiver_propagation.py
```

---

## 🎬 Exemplos de animações geradas

> ⚠️ As animações são salvas automaticamente como `.mp4` em `data/campos/MODO/`

- $Hz$ em plano XY: propagação espacial
- Vetores $ \vec{E}_t $ com animação em tempo
- Propagação em z com vetores pulsando (modo TE₁₀, $Ex/Ey$)

![Exemplo vetorial](doc/figuras/quiver_demo.png) <!-- opcional -->
![Exemplo propagação](doc/figuras/propagacao_demo.gif) <!-- opcional -->

---

## 📚 Referências

- SADIKU, M. N. O. *Elementos de Eletromagnetismo*. Bookman.
- BASTOS, J. P. A.; KOSYLOWSKI, M. E. *Eletromagnetismo: Fundamentos e Aplicações*. LTC.
- CHENG, D. K. *Field and Wave Electromagnetics*. Addison-Wesley.

---

## 🧑‍🏫 Licença e objetivo

Este projeto é **livre e aberto** para fins **didáticos e acadêmicos**.  
Você pode usar, adaptar, compartilhar e contribuir.

---

## ✨ Futuras melhorias

- Interface web (Jupyter ou Streamlit)
- Exportação para Paraview (`.vti`)
- Modo interativo para comparar modos TE e TM lado a lado

---

**Desenvolvido com ❤️ e Maxwell em mente.**
