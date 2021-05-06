import random
import math
from bokeh.plotting import figure, output_file, show

class Centroide:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.conjunto_vectores = []
        

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grupo = None

    def Medir_Distancia(self, centroide):
        return ((self.x - centroide.x) ** 2 + (self.y - centroide.y) ** 2)**(1/2)

def generar_Data_Points(numero_de_puntos):
    vectores = []
    for _ in range(numero_de_puntos):
        x = random.uniform(1,30)
        y = random.uniform(1,30)
        vectores.append(Vector(x, y))

    return vectores

def generar_Centroides(numero_clusters):
    centroides = []
    for _ in range(numero_clusters):
        x = random.uniform(1,30)
        y = random.uniform(1,30)
        centroides.append(Centroide(x, y))

    return centroides

def k_mean_clustering(vectores, centroides):
    i = 0 
    while i < 10:
        for vector in vectores: # Recorremos cada vector para verificar su clasificación
            minimo = math.inf
            for centroide in centroides: # Por cada vector comparamos con cada centroide
                distancia_al_centroide = vector.Medir_Distancia(centroide) # Sacamos la distancia del vector al dentroide

                if distancia_al_centroide <= minimo: # Si es menor que el minimo se actualiza y se guarda el centroide
                    centroide_cercano = centroide
                    minimo = distancia_al_centroide

            centroide_cercano.conjunto_vectores.append(vector) # Añade al vector mas cercano al que haya quedado

        grafica_K_Means(centroides)
        # Terminamos de iterar en los vectores -------------------------------------------------------------------------
        # Generamos el nuevo centroide ---------------------------------------------------------------------------------
        for centroide in centroides:
            x_nuevo, y_nuevo = generar_Nuevo_Centroide(centroide)
            centroide.x = x_nuevo
            centroide.y = y_nuevo
            centroide.conjunto_vectores = []

        i += 1

def generar_Nuevo_Centroide(centroide):
    x = 0
    y = 0
    for vector in centroide.conjunto_vectores:
        x += vector.x
        y += vector.y

    x_promedio = x / len(centroide.conjunto_vectores)
    y_promedio = y / len(centroide.conjunto_vectores)

    return(x_promedio, y_promedio)
    
def grafica_K_Means(centroides, colores = ['blue','orangered', 'blueviolet', 'crimson', 'lightslategray']):
    output_file("line.html")
    p = figure(title= 'Agrupamiento K-means')

    i = 0
    for centroide in centroides:
        x_axis = []
        y_axis = []
        for vector in centroide.conjunto_vectores:
            x_axis.append(vector.x)
            y_axis.append(vector.y)

        p.circle(x_axis, y_axis, size=10, color=colores[i], alpha=0.5)
        p.x(centroide.x, centroide.y, size = 20)
        i += 1

    show(p)

def grafica_inicial(vectores):
    x_axis = []
    y_axis = []
    output_file("line.html")
    p = figure(title= 'Agrupamiento K-means')
    for vector in vectores:
        x_axis.append(vector.x)
        y_axis.append(vector.y)
    
    p.circle(x_axis, y_axis, size=10, color='navy', alpha=0.5)
    show(p)

if __name__ == '__main__':

    numero_de_puntos = int(input('¿Cuantos data points quieres procesar? :'))
    vectores = generar_Data_Points(numero_de_puntos)
    grafica_inicial(vectores)
    numero_clusters = int(input('¿En cuantos clusters quieres clasificar? :'))
    centroides = generar_Centroides(numero_clusters)
    # En este punto ya tenemos los data points y los respectivos centroides ------------------------------
    k_mean_clustering(vectores, centroides)


