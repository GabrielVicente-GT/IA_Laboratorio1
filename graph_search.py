from bfs_algorithm import *
from wr_functions import *
import cv2 as opencv
from wr_bmp import *
import itertools

#C
from a_star_euclidean_algorithm import *
from a_star_manhattan_algorithm import *
from dfs_algorithm import *

#Clase que permite obtener el arreglo bidimensional de colores
#Y escribe el mapa discretizado
class GraphSearch(object):

    def __init__(self, filename, height, width):
        #Ubicacion y cantidad resolucion
        self.filename   = filename
        self.height     = height
        self.width      = width
        #Nuevo bmp
        self.imagen     = Write(self.width, self.height)
        self.morados    = []
        self.naranja     = []

        #Escritura y aplicacion de solucion
        self.wr_image()

    def wr_image(self):
        #Minimizar mapa
        MazeColors = opencv.imread(self.filename)
        MazeColors = opencv.resize(MazeColors, (self.width, self.height))
        opencv.imwrite("./Laberintos/NewMaze.bmp", MazeColors)

        #Limpiar mapa
        #Se crea un render con la altura y anchura deseada
        #Se agrega en la propiedad laberinto los pixeles limpios de la self.imagen minimzada
        self.imagen.laberinto = Read("./Laberintos/NewMaze.bmp")
        pixels = self.imagen.laberinto.pixels
        #En el framebuffer de la self.imagen se escriben los nuevos pixeles obtenidos
        self.imagen.framebuffer = [[color(pixels[y][x][0],pixels[y][x][1],pixels[y][x][2]) for x in range(Read("./Laberintos/NewMaze.bmp").width)]for y in range(Read("./Laberintos/NewMaze.bmp").height)]

        #Quitar pixeles extra de verde y rojo
        #Posiciones a limpiar
        A,B = [-2,-1,0,1,2],[-2,1,0,-1,2]
        pairs = list(itertools.product(A, B))

        #Se limpian los pixeles al rededor del inicio y final
        for x in range(self.width):
            for y in range(self.height):
                if self.imagen.framebuffer[y][x] == color(0,255,0):
                    for pareja in pairs:
                        if pareja != (0,0):
                            if self.imagen.framebuffer[y+pareja[0]][x+pareja[1]] == color(0,255,0):
                                self.imagen.framebuffer[y+pareja[0]][x+pareja[1]] = color(255,255,255)
                elif self.imagen.framebuffer[y][x] == color(255,0,0):
                    for pareja in pairs:
                        if pareja != (0,0):
                            if self.imagen.framebuffer[y+pareja[0]][x+pareja[1]] == color(255,0,0):
                                self.imagen.framebuffer[y+pareja[0]][x+pareja[1]] = color(255,255,255)

        #Delimitar areas del maze
        for x in range(self.width):
            for y in range(self.height):
                if x == 0 or x == self.width-1 or y == 0 or y == self.height-1:
                    self.imagen.framebuffer[y][x] = color(0,0,0)

        #Escribir el nuevo mapa discretizado
        self.imagen.write("./Laberintos/NewMaze.bmp")

    def apply_solution(self):
        self.wr_image()
        #Solution
        #BFS algorithm general
        maze_solution = BFS(self.imagen.framebuffer, self.width, self.height)

        #Reasignacion de valores de pixeles visitados y camino corto
        self.naranja = maze_solution.shortest_path
        self.morados = maze_solution.all_pixels

        #Se pintan los pixeles morados
        for pixel in maze_solution.all_pixels:
            x,y = pixel
            if pixel != maze_solution.inicio and pixel not in maze_solution.final:
                self.imagen.framebuffer[y][x] = color(125, 60, 152)

        #Se pintan los pixeles anaranjados
        for pixel in maze_solution.shortest_path:
            x,y = pixel
            if pixel != maze_solution.inicio and pixel not in maze_solution.final:
                self.imagen.framebuffer[y][x] = color(243, 156, 18)

        #Se escribe la self.imagen
        self.imagen.write("./Laberintos/NewMazeSolution.bmp")

    def apply_solution_DFS(self):
        self.wr_image()
        #Solution
        #DFS algorithm general
        maze_solution = DFS(self.imagen.framebuffer, self.width, self.height)

        #Reasignacion de valores de pixeles visitados y camino corto
        self.naranja = maze_solution.result_path
        self.morados = maze_solution.all_pixels

        #Se pintan los pixeles morados
        for pixel in maze_solution.all_pixels:
            x,y = pixel
            if pixel != maze_solution.inicio and pixel not in maze_solution.final:
                self.imagen.framebuffer[y][x] = color(125, 60, 152)

        #Se pintan los pixeles anaranjados
        for pixel in maze_solution.result_path:
            x,y = pixel
            if pixel != maze_solution.inicio and pixel not in maze_solution.final:
                self.imagen.framebuffer[y][x] = color(243, 156, 18)

        #Se escribe la self.imagen
        self.imagen.write("./Laberintos/NewMazeSolution.bmp")
        
        
    def apply_solution_a_euclidean(self):
        self.wr_image()
        #Solution
        # A STAR SEARCH ALGORITHM CON HEURISTICA DE DISTANCIA EUCLIDEANA
        maze_solution = A_STAR_EUCLIDEAN(self.imagen.framebuffer, self.width, self.height)

        #Reasignacion de valores de pixeles visitados y camino corto
        self.naranja = maze_solution.shortest_path
        self.morados = maze_solution.all_pixels

        #Se pintan los pixeles morados
        for pixel in maze_solution.all_pixels:
            x,y = pixel
            if pixel != maze_solution.inicio and pixel not in maze_solution.final:
                self.imagen.framebuffer[y][x] = color(125, 60, 152)

        #Se pintan los pixeles anaranjados
        for pixel in maze_solution.shortest_path:
            x,y = pixel
            if pixel != maze_solution.inicio and pixel not in maze_solution.final:
                self.imagen.framebuffer[y][x] = color(243, 156, 18)

        #Se escribe la self.imagen
        self.imagen.write("./Laberintos/NewMazeSolution.bmp")
        
        
    def apply_solution_a_manhattan(self):
        self.wr_image()
        #Solution
        # A STAR SEARCH ALGORITHM CON HEURISTICA DE DISTANCIA DE MANHATTAN
        maze_solution = A_STAR_MANHATTAN(self.imagen.framebuffer, self.width, self.height)

        #Reasignacion de valores de pixeles visitados y camino corto
        self.naranja = maze_solution.shortest_path
        self.morados = maze_solution.all_pixels

        #Se pintan los pixeles morados
        for pixel in maze_solution.all_pixels:
            x,y = pixel
            if pixel != maze_solution.inicio and pixel not in maze_solution.final:
                self.imagen.framebuffer[y][x] = color(125, 60, 152)

        #Se pintan los pixeles anaranjados
        for pixel in maze_solution.shortest_path:
            x,y = pixel
            if pixel != maze_solution.inicio and pixel not in maze_solution.final:
                self.imagen.framebuffer[y][x] = color(243, 156, 18)

        #Se escribe la self.imagen
        self.imagen.write("./Laberintos/NewMazeSolution.bmp")
