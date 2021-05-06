import random
import math

from bokeh.plotting import figure, output_file, show


"""
Geenera graficas de como se van uniendo los vectores, puesto que no hay como hacer
dendogramas en bokeh 

"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, otro_vector):
        return ((self.x - otro_vector.x) ** 2 + (self.y - otro_vector.y) ** 2)**(1/2)

def grafica_dendograma():
    pass

def graficar(clusters):
    x_axis = []
    y_axis = []

    for i in range(len(clusters)):
        x_vector_promedio_1 = sum([clusters[i][x].x for x in range(len(clusters[i]))])  / len(clusters[i])
        y_vector_promedio_1 = sum([clusters[i][y].y for y in range(len(clusters[i]))])  / len(clusters[i])
        vector_promedio_1 = Vector(x_vector_promedio_1,y_vector_promedio_1)
        x_axis.append(vector_promedio_1.x)
        y_axis.append(vector_promedio_1.y)

    

    p = figure(title= 'Agrupamiento Jerarquico')

    # add a circle renderer with a size, color, and alpha
    p.circle(x_axis, y_axis, size=30, color="navy", alpha=0.5)

    # show the results
    show(p)


def clustering(clusters):
    minimo = math.inf
    clusters_cercanos = math.inf

    for i in range(len(clusters) - 1):
        x_vector_promedio_1 = sum([clusters[i][x].x for x in range(len(clusters[i]))])  / len(clusters[i])
        y_vector_promedio_1 = sum([clusters[i][y].y for y in range(len(clusters[i]))])  / len(clusters[i])
        vector_promedio_1 = Vector(x_vector_promedio_1,y_vector_promedio_1)
        for j in range(i + 1 ,len(clusters)):
            print('i:', i, 'j: ', j)
            x_vector_promedio_2 = sum([clusters[j][x].x for x in range(len(clusters[j]))])  / len(clusters[j])
            y_vector_promedio_2 = sum([clusters[j][y].y for y in range(len(clusters[j]))])  / len(clusters[j])
            vector_promedio_2 = Vector(x_vector_promedio_2,y_vector_promedio_2)

            if  vector_promedio_1.distance(vector_promedio_2) <= minimo:
                clusters_cercanos = (clusters[i], clusters[j])
                minimo = vector_promedio_1.distance(vector_promedio_2)

    try:
        clusters.remove(clusters_cercanos[0])
        clusters.remove(clusters_cercanos[1]) 
        clusters_cercanos[0].extend(clusters_cercanos[1])
        clusters.append(clusters_cercanos[0])
        return 
    except:
        return




def main(vectors):

    clusters = [[x] for x in vectors] # Crea los clusters que son listas de objetos Vector
    while len(clusters) > 1: # Mientras haya mas de 1 cluster
        clustering(clusters) # Agrupa los mas cercanos
        graficar(clusters)

        
if __name__ == "__main__":
    # Entry ponit 
    # Le preguntamos cuantos data points quiere ingresar
    
    numero_de_puntos = int(input('Cuantos data point quieres procesar: '))
    vectors = []
    
    for _ in range(numero_de_puntos): # Función que saca los puntos aleatorios
        x = random.uniform(1,10)
        y = random.uniform(1,10)
        v = Vector(x, y) # Crea un objeto vector con las coordenadas
        vectors.append(v) # Los añade a una lista
    
    # vectors = [Vector(1,1),Vector(1,1.1),Vector(8,8)]
    main(vectors) # Función main