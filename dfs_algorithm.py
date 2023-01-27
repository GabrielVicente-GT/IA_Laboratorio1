from framework import Framework
from wr_functions import *

#Clase que aplica el algoritmo DFS
class DFS(Framework):

    def __init__(self, maze, w, h):
        #Parametros a recibir
        self.maze       = maze
        self.altura     = h
        self.anchura    = w

        #Inicio y final
        self.inicio     = [(x,y) for x in range(self.anchura) for y in range(self.altura) if self.maze[y][x] == color(255,0,0)][0]
        self.final      = [(x,y) for x in range(self.anchura) for y in range(self.altura) if self.maze[y][x] == color(0,255,0)]

        print(self.inicio)
        print(self.final)

        #Requeridos
        self.result_path = []
        self.all_pixels = []
        self.checked = []
        self.line_up = []
        self.objetive = False
        #Se llama a acciones
        self.actions()
        print('¿Se cumplio con el objetivo?', self.objetive)

    #Accion que realiza a partir del pixel en el que se esta actualmente
    def actions(self):
        
        self.line_up.append(self.inicio)

        #Mientras line_up tenga elementos
        while self.line_up:
            
            self.pxl_actual =  self.line_up.pop(0)
            self.result_path.append(self.pxl_actual)

            if self.goalTest == True:
                return self.result_path

            self.algorithmDFS(self.pxl_actual)

            

    def pathTest(self):
        pass

    def results(self):
        pass

    def stepTest(self):
        pass


    #Verificacion de si el pixel actual esta dentro de alguno de los finales
    def goalTest(self):
        if self.pxl_actual in self.final:
            self.objetive = True
            return True
        return False

    #Lleva el control de manera ciclica del algoritmo
    #Ejecutando los algoritmos anteriores
    def algorithmDFS(self, pxlactual):
        x, y = pxlactual[0], pxlactual[1]

        if self.maze[y][x - 1] != color(0, 0, 0) and (x - 1, y) not in self.result_path:
            self.line_up.append((x - 1, y))
            self.all_pixels.append((x - 1, y))
        elif self.maze[y + 1][x]  != color(0, 0, 0) and (x, y + 1) not in self.result_path:
            self.line_up.append((x, y + 1))
            self.all_pixels.append((x, y + 1))
        elif self.maze[y][x + 1]  != color(0, 0, 0) and (x + 1, y) not in self.result_path:
            self.line_up.append((x + 1, y))
            self.all_pixels.append((x + 1, y))
        elif self.maze[y - 1][x]  != color(0, 0, 0) and (x, y - 1) not in self.result_path:
            self.line_up.append((x, y - 1))
            self.all_pixels.append((x, y - 1))
