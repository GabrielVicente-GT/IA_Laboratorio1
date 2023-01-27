#Laboratorio 1 Inteligencia Artificial CC3085
#Gabriel Vicente 20498
#Oscar Lopez 20679
#Pedro Arriola 20188

from animated_solution import *
from graph_search import *

#Ancho, Alto y ruta de archivo a discretizar y solucionar
Ancho, Alto = 44,44
OriginalMaze = "./Laberintos/MazeA.bmp"

#Se llama a GraphSearch que discretiza la imagen y le aplica la solucion
SolvedMaze = GraphSearch(OriginalMaze,Ancho,Alto)
SolvedMaze.apply_solution_a_euclidean()
SolvedMaze.apply_solution_a_manhattan()
#Segun los valores obtenidos con GraphSearch se anima el algoritmo
#Animate(Ancho, Alto, SolvedMaze.morados, SolvedMaze.naranja)
