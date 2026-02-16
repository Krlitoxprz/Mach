import matplotlib.pyplot as plt

# Datos experimentales
Distancia = [3.75, 4.10, 4.64, 5.42, 6.40, 7.63, 9.09, 10.74, 12.62, 14.73, 17.07, 19.62, 22.38, 25.34, 28.53, 32.00, 35.63, 39.46, 41.79, 41.78, 41.77]
Fuerza = [3.57, 3.51, 3.13, 2.21, 1.38, 0.97, 0.78, 0.64, 0.57, 0.52, 0.50, 0.48, 0.48, 0.51, 0.49, 0.51, 0.52, 0.50, 0.52, 0.51, 0.55]

# Crear figura con tamaño grande
plt.figure(figsize=(12, 8))

# Graficar puntos con marcadores y unir con línea
plt.plot(Distancia, Fuerza, marker='o', linestyle='-', linewidth=2, markersize=6, color='blue')

# Título y etiquetas de los ejes
plt.title('Fuerza vs Distancia', fontsize=16, fontweight='bold')
plt.xlabel('Distancia (cm)', fontsize=14)
plt.ylabel('Fuerza (mN)', fontsize=14)

# Mostrar cuadrícula
plt.grid(True, linestyle='--', alpha=0.7)

# Ajustar el diseño
plt.tight_layout()

# Guardar el gráfico como imagen
plt.savefig('grafico_fuerza_vs_distancia.png', dpi=300)

# Mostrar el gráfico
# plt.show()

print("Gráfico guardado como 'grafico_fuerza_vs_distancia.png'")