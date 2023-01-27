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

        #Requeridos
        self.shortest_path = []
        self.all_pixels = []
        self.checked = []
        self.line_up = []
        self.objetive = False
        #Se llama a acciones
        print('Camino mas corto DFS:', self.algorithmDFS())
        print('¿Se cumplio con el objetivo?', self.objetive)

    #Accion que realiza a partir del pixel en el que se esta actualmente
    def actions(self):
        
        self.checked.append(self.inicio)
        self.line_up.append(self.inicio)

        #Mientras line_up tenga elementos
        while  self.line_up:
            #Se asigna el pixel actual y se lleva control de todos los pieles
            self.pxl_actual =  self.line_up.pop(0)
            self.all_pixels.append(self.pxl_actual)

    #El resultado de realizar una accion en el estado actual
    def results(self, current, pxl):
        self.stepTest(pxl, current)
        self.checked.append(pxl)
        self.line_up.append(pxl)

    #Verificacion de si el pixel actual esta dentro de alguno de los finales
    def goalTest(self):
        if self.pxl_actual in self.final:
            self.objetive = True
            return True
        return False

    def stepTest(self, pxl,current):
        pass

    #Devuelve el camino mas corto encontrado
    def pathTest(self):
        pass

    #Lleva el control de manera ciclica del algoritmo
    #Ejecutando los algoritmos anteriores
    def algorithmDFS(self):
        pass
