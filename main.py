#Laboratorio 1 Inteligencia Artificial CC3085
#Gabriel Vicente 20498
#Oscar Lopez 20679
#Pedro Arriola 20188

from animated_solution import *
from graph_search import *

#Ancho, Alto y ruta de archivo a discretizar y solucionar
Ancho, Alto = 44,44
OriginalMaze = "./Laberintos/MazeA.bmp"

if OriginalMaze == "./Laberintos/MazeD.bmp":
    Ancho, Alto = 100,100

#Se llama a GraphSearch que discretiza la imagen y le aplica la solucion
SolvedMaze = GraphSearch(OriginalMaze,Ancho,Alto)

#Menu que permite visualizar las diferentes opciones
while True:
    print("Seleccione el algoritmo con el cual desea resolver ", OriginalMaze)
    print("> 1. BFS")
    print("> 2. DFS")
    print("> 3. AStart (manhattan)")
    print("> 4. AStart (euclidean)")
    print("> 5. Ver animacion (algoritmo visto anteriormente)")
    print("> 6. Salir")

    try:
        opcion = int(input(">> Ingresa el numero del algoritmo a utilizar: "))

        if opcion == 1:
            print("BFS")
            SolvedMaze.apply_solution()
        elif opcion == 2:
            print("DFS")
            SolvedMaze.apply_solution_DFS()
        elif opcion == 3:
            print("AStart (manhattan)")
            SolvedMaze.apply_solution_a_manhattan()
        elif opcion == 4:
            print("AStart (euclidean)")
            SolvedMaze.apply_solution_a_euclidean()
        elif opcion == 5:
            Animate(Ancho, Alto, SolvedMaze.morados, SolvedMaze.naranja)
        elif opcion == 6:
            break
        else:
            print("ERROR, vuelve a intentarlo")
        
        print("\n> Si se desea cambiar el mapa, actualizar valor de OriginalMaze.")
        print("> La discretizacion y la solucion se muestran respectivamente en:")
        print(" - NewMaze.bmp")
        print(" - NewMazeSolution.bmp\n")
        
    except ValueError:
        print("ERROR, vuelve a intentarlo")
