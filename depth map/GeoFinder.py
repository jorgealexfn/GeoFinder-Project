import math
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c * 1000
    return distance

def estah_dentro_area(lat, lon, lat_min, lon_min, lat_max, lon_max):
    return lat_min <= lat <= lat_max and lon_min <= lon <= lon_max

def ler_arquivo(file_path):
    with open(file_path, 'r') as file:
        dados = [linha.strip().split() for linha in file.readlines()]
        dados = [(float(lon), float(lat), float(prof)) for lon, lat, prof in dados]
        lat_min = min(dados, key=lambda x: x[1])[1]
        lon_min = min(dados, key=lambda x: x[0])[0]
        lat_max = max(dados, key=lambda x: x[1])[1]
        lon_max = max(dados, key=lambda x: x[0])[0]
    return dados, lat_min, lon_min, lat_max, lon_max

def encontrar_posicao_mais_proxima(dados, lat, lon):
    min_distance = float('inf')
    closest_position = None
    closest_depth = None

    for row in dados:
        lat2, lon2, depth = row
        distance = haversine(lat, lon, lat2, lon2)
        if distance < min_distance:
            min_distance = distance
            closest_position = (lat2, lon2)
            closest_depth = depth

    return closest_position, min_distance, closest_depth

# Lê o arquivo e obtém os dados
dados, lat_min, lon_min, lat_max, lon_max = ler_arquivo('Datas_Received.txt')

# Imprime os limites de latitude e longitude
print(f'Latitude mínima: {lat_min}, Longitude mínima: {lon_min}')
print(f'Latitude máxima: {lat_max}, Longitude máxima: {lon_max}')

# Recebe a entrada do usuário
lat = float(input("Digite a latitude: ").replace(',', '.'))
lon = float(input("Digite a longitude: ").replace(',', '.'))

# Verifica se o ponto está dentro da área e imprime o resultado
dentro_da_area = estah_dentro_area(lat, lon, lat_min, lon_min, lat_max, lon_max)
print(f'O ponto está dentro da área? {dentro_da_area}')

if dentro_da_area:
    # Mede o tempo antes da chamada da função
    inicio = time.time()

    # Chama a função e obtém o resultado
    closest_position, min_distance, closest_depth = encontrar_posicao_mais_proxima(dados, lat, lon)

    # Mede o tempo após a chamada da função
    fim = time.time()

    # Imprime os resultados
    print(f"Posição mais próxima: {closest_position}")
    print(f"Distância para a posição mais próxima: {min_distance:.2f} metros")
    print(f"Profundidade na posição mais próxima: {closest_depth:.2f} metros")
    print(f"Tempo decorrido: {fim - inicio:.2f} segundos")

    # Plota os pontos usando contorno em 3D
    lons, lats, depths = zip(*dados)
    
    # Gera uma grade para interpolação
    lon_grid, lat_grid = np.meshgrid(np.linspace(min(lons), max(lons), 100), np.linspace(min(lats), max(lats), 100))
    depth_grid = griddata((lons, lats), depths, (lon_grid, lat_grid), method='cubic')

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    contour = ax.contour3D(lon_grid, lat_grid, depth_grid, 50, cmap='viridis')
    fig.colorbar(contour, ax=ax, label='Profundidade (metros)')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Profundidade')
    ax.set_title('Mapa de Profundidade 3D')

    plt.show()
