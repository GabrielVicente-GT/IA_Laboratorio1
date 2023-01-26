from framework import Framework
from wr_functions import *

#Clase que aplica el algoritmo BFS
class BFS(Framework):

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
        self.previus_cost = {}
        self.all_pixels = []
        self.checked = []
        self.line_up = []
        self.objetive = False
        #Se llama a acciones
        print('Camino mas corto BFS:', self.algorithmBFS())
        print('¿Se cumplio con el objetivo?', self.objetive)

    #Accion que realiza a partir del pixel en el que se esta actualmente
    def actions(self):
        contiguous_pixels = [(self.pxl_actual[0]+1,self.pxl_actual[1]), (self.pxl_actual[0]-1,self.pxl_actual[1]), (self.pxl_actual[0],self.pxl_actual[1]+1), (self.pxl_actual[0],self.pxl_actual[1]-1)]
        contiguous_pixels = [pxl for pxl in contiguous_pixels if self.maze[pxl[1]][pxl[0]]!=color(0,0,0)]
        return contiguous_pixels

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

    #Costo de pasar de un pixel a otro ("Yo vengo de")
    def stepTest(self, pxl,current):
        self.previus_cost[pxl] = current

    #Devuelve el camino mas corto encontrado
    def pathTest(self):
            self.shortest_path = []
            while self.pxl_actual != self.inicio:
                self.shortest_path.append(self.pxl_actual)
                self.pxl_actual = self.previus_cost[self.pxl_actual]
            self.shortest_path.append(self.inicio)
            return self.shortest_path[::-1]

    #Lleva el control de manera ciclica del algoritmo
    #Ejecutando los algoritmos anteriores
    def algorithmBFS(self):
        print('Inicio:',self.inicio)
        print('Fin',self.final)
        #Algoritmo BFS
        self.previus_cost = {self.inicio: None}
        self.checked.append(self.inicio)
        self.line_up.append(self.inicio)

        #Mientras line_up tenga elementos
        while  self.line_up:
            #Se asigna el pixel actual y se lleva control de todos los pieles
            self.pxl_actual =  self.line_up.pop(0)
            self.all_pixels.append(self.pxl_actual)

            #Si se cumple la meta devolver el camino mas corto
            if self.goalTest():
                return self.pathTest()

            #Si aun no se cumple la meta
            #Obtener los pixeles contiguos posibles
            contiguous_pixels = self.actions()

            #Y por cada nodo posible, llamar a results para
            #Agregarlo a los arrreglos respectivos (line_up, checked y llevar el costo)
            for pxl in contiguous_pixels:
                if pxl not in self.checked:
                    self.results(self.pxl_actual, pxl)
