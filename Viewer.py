import os
import ezdxf
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Ruta al archivo DXF
ruta_archivo = '.dxf'

# Verificar si el archivo existe
if not os.path.isfile(ruta_archivo):
    print(f"El archivo {ruta_archivo} no existe.")
    exit()

# Leer el archivo DXF y crear un objeto Point para cada entidad Point
doc = ezdxf.readfile(ruta_archivo)
msp = doc.modelspace()
puntos = []

for entidad in msp:
    if entidad.dxftype() == 'POINT':
        x = entidad.dxf.location[0]
        y = entidad.dxf.location[1]
        z = entidad.dxf.location[2] if entidad.dxf.location[2] is not None else 0
        punto = Point(x, y, z)
        puntos.append(punto)

# Visualizar los puntos
for punto in puntos:
    plt.scatter(punto.x, punto.y)
    plt.text(punto.x, punto.y, f"({punto.x}, {punto.y})")

plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.title('Visualización de puntos DXF')
plt.show()