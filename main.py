#Laboratorio 1 Inteligencia Artificial CC3085
#Gabriel Vicente 20498
#Oscar Lopez 20679
#Pedro Arriola 20188

from animated_solution import *
from graph_search import *

#Ancho, Alto y ruta de archivo a discretizar y solucionar
Ancho, Alto = 100,100
OriginalMaze = "./Laberintos/turing.bmp"

#Se llama a GraphSearch que discretiza la imagen y le aplica la solucion
SolvedMaze = GraphSearch(OriginalMaze,Ancho,Alto)
#Segun los valores obtenidos con GraphSearch se anima el algoritmo
Animate(Ancho, Alto, SolvedMaze.morados, SolvedMaze.naranja)
