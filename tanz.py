import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def calculate_function(z, z0):
    """
    Calcula tan(z) = sqrt((z0/z)^2 - 1)
    Maneja los casos donde la función no está definida o es compleja
    """
    # Evitar división por cero
    z = np.where(z == 0, np.nan, z)
    
    # Calcular (z0/z)^2 - 1
    ratio_squared = (z0 / z) ** 2
    argument = ratio_squared - 1
    
    # Solo tomar valores reales donde el argumento es >= 0
    result = np.where(argument >= 0, np.sqrt(argument), np.nan)
    
    return result

# Configurar los valores de z
z = np.linspace(-10, 10, 1000)
z = z[z != 0]  # Remover z = 0 para evitar división por cero

# Diferentes valores de z0 para graficar
z0_values = [1, 2, 3, 4, 5]
colors = ['blue', 'red', 'green', 'orange', 'purple']

# Crear la figura
plt.figure(figsize=(12, 8))

# Graficar para cada valor de z0
for i, z0 in enumerate(z0_values):
    y = calculate_function(z, z0)
    plt.plot(z, y, color=colors[i], label=f'z₀ = {z0}', linewidth=2)
    
    # También graficar la función negativa (ya que sqrt puede ser ±)
    plt.plot(z, -y, color=colors[i], linestyle='--', alpha=0.7, linewidth=2)

# Configurar el gráfico
plt.xlabel('z', fontsize=12)
plt.ylabel('tan(z) = √((z₀/z)² - 1)', fontsize=12)
plt.title('Gráfica tan(z) = √((z₀/z)² - 1)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.ylim(-10, 10)
plt.xlim(-10, 10)

# Añadir líneas de referencia
plt.axhline(y=0, color='black', linewidth=0.5)
plt.axvline(x=0, color='black', linewidth=0.5)

# Mejorar la presentación
plt.tight_layout()

# Mostrar información adicional
print("Información sobre la función tan(z) = √((z₀/z)² - 1):")
print("- Las líneas sólidas representan la raíz positiva")
print("- Las líneas punteadas representan la raíz negativa")
print("- La función solo está definida donde (z₀/z)² ≥ 1")
print("- Esto significa |z| ≤ |z₀|")
print("- Hay asíntotas verticales en z = ±z₀")

plt.show()

# Crear un segundo gráfico mostrando las regiones de definición
plt.figure(figsize=(10, 6))

z_fine = np.linspace(-6, 6, 2000)
z_fine = z_fine[z_fine != 0]

for i, z0 in enumerate([2, 4]):
    # Calcular donde la función está definida
    defined_mask = np.abs(z_fine) <= z0
    z_defined = z_fine[defined_mask]
    y_defined = calculate_function(z_defined, z0)
    

