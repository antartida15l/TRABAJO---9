import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Análisis de Mínimos Globales y Locales de Funciones")

# Ejercicio 1: Verificar minimizadores globales/locales para f(x) = x^2 - 4x + 5
st.header("1. Verificar minimizadores de f(x) = x² - 4x + 5")

# Mostrar la función en forma estándar
st.latex(r"f(x) = x^2 - 4x + 5 = (x - 2)^2 + 1")
st.write("El vértice es \(x = 2\), y el valor mínimo es \(f(2) = 1\).")

# Generar gráfico
x_vals = np.linspace(-2, 6, 100)
f_vals = (x_vals - 2) ** 2 + 1
fig, ax = plt.subplots()
ax.plot(x_vals, f_vals, label=r"$f(x) = (x - 2)^2 + 1$")
ax.scatter([2], [1], color="red", label="Mínimo global en x=2")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
ax.axvline(2, color="gray", linestyle="--", linewidth=0.5)
ax.legend()
st.pyplot(fig)

# Ejercicio 2: Análisis de f(x) = |x|
st.header("2. Determinar mínimos para f(x) = |x|")
st.write("El mínimo global y local ocurre en \(x = 0\), donde \(f(0) = 0\).")

# Gráfico de |x|
x_vals = np.linspace(-5, 5, 100)
abs_vals = np.abs(x_vals)
fig, ax = plt.subplots()
ax.plot(x_vals, abs_vals, label=r"$f(x) = |x|$")
ax.scatter([0], [0], color="red", label="Mínimo global en x=0")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
ax.axvline(0, color="gray", linestyle="--", linewidth=0.5)
ax.legend()
st.pyplot(fig)

# Ejercicio 3: Teorema de Weierstrass para f(x) = sin(x) en [0, π]
st.header("3. Mínimos globales para f(x) = sin(x) en [0, π]")
st.write("Según el Teorema de Weierstrass, \(f(x) = \sin(x)\) tiene un mínimo global en \([0, \pi]\).")
st.latex(r"f(\pi) = 0 \text{ es el mínimo global.}")

# Gráfico de sin(x)
x_vals = np.linspace(0, np.pi, 100)
sin_vals = np.sin(x_vals)
fig, ax = plt.subplots()
ax.plot(x_vals, sin_vals, label=r"$f(x) = \sin(x)$")
ax.scatter([np.pi], [0], color="red", label="Mínimo global en x=π")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.axhline(0, color="black", linewidth=0.5, linestyle="--")
ax.axvline(np.pi, color="gray", linestyle="--", linewidth=0.5)
ax.legend()
st.pyplot(fig)

# Ejercicio 4: Mínimo global para f(x, y) = x^2 + y^2 con x^2 + y^2 <= 1
st.header("4. Mínimos para f(x, y) = x² + y² con x² + y² ≤ 1")
st.write("El mínimo global ocurre en el origen \((0, 0)\), donde \(f(0, 0) = 0\).")

# Gráfico de x^2 + y^2
x_vals = np.linspace(-1, 1, 100)
y_vals = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = X**2 + Y**2
fig, ax = plt.subplots()
contour = ax.contourf(X, Y, Z, levels=20, cmap="viridis")
fig.colorbar(contour, ax=ax, label="f(x, y)")
ax.scatter([0], [0], color="red", label="Mínimo global en (0,0)")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# Ejercicio 5: Mínimo global no único
st.header("5. Mínimo global no único")
st.latex(r"f(x) = \max(|x - 1|, |x + 1|)")
st.write("El mínimo global ocurre en el intervalo \([-1, 1]\), donde \(f(x) = 1\).")

# Gráfico de máximo(|x-1|, |x+1|)
x_vals = np.linspace(-3, 3, 100)
max_vals = np.maximum(np.abs(x_vals - 1), np.abs(x_vals + 1))
fig, ax = plt.subplots()
ax.plot(x_vals, max_vals, label=r"$f(x) = \max(|x - 1|, |x + 1|)$")
ax.axhline(1, color="red", linestyle="--", label="Mínimo global en [-1, 1]")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
st.pyplot(fig)
