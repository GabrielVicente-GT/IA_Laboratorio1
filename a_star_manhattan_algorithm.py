from wr_functions import *
from framework import Framework

class A_STAR_MANHATTAN(Framework):

    def __init__(self, maze, w, h):
        self.anchura = w
        self.altura = h
        self.maze = maze

        #Inicio y final
        self.inicio = [(x, y) for x in range(self.anchura) for y in range(self.altura) if self.maze[y][x] == color(255, 0, 0)][0]
        self.final = [(x, y) for x in range(self.anchura) for y in range(self.altura) if self.maze[y][x] == color(0, 255, 0)]

        self.came_from = None
        
        self.line_up = []
        self.all_pixels = []
        self.shortest_path = []
        self.costos = []

        self.actions()

    def manhattan_distance(self, point_1, point_2):

        # sum of absolute difference between coordinates
        distance = 0
        for p_i, q_i in zip(point_1, point_2):
            distance += abs(p_i - q_i)
        
        return distance
    
    # La funcion results regresa los valores finales del algoritmo A* Search Algorithm
    def results(self):
        return self.shortest_path, self.all_pixels
        
    # La funcion goalTest permite verificar si la posicion alcanzada es la final
    def goalTest(self):
        if self.current in self.final:
            self.shortest_path = []
        while self.current != self.inicio:
            self.shortest_path.append(self.current)
            self.current = self.came_from[self.current]
        self.shortest_path.append(self.inicio)
        
        # Se reasignan las posiciones de los nodos
        self.shortest_path = self.shortest_path[::-1]
        
    # La funcion costTest calcula el costo de cada paso para determinar el shortest_path mas corto en base a la funcion f
    def costTest(self, caminos):
        
        costos_funcion_f = []
        nodos = caminos
    
        for nodo in (nodos):
            
            # El parametro g denota el costo del movimiento desde la posicion inicial a cualquier otra posicion.
            g = self.manhattan_distance(self.inicio, nodo)
            
            # Este denota la heuristica, el cual es el costo del movimiento desde el inicio hasta el final.
            h = []
            
            for nodo_final in self.final:
                # Se calcula la heuristica actual utilizando la distancia Euclideana
                heuristica =  self.manhattan_distance(nodo_final, nodo)
                h.append(heuristica)
                
            
            # Se calcula la funcion f
            f = round(g + min(h))
            
            costos_funcion_f.append(f)
        
        return costos_funcion_f

    # La funcion pathTest se encarga de analizar todos posibles caminos que se pueden tomar.
    def pathTest(self, posicion):
        
        caminos_posibles = []
        x, y = posicion
        
        '''
        Es importante tomar en cuenta todas las posibles posiciones a las que
        se puede mover, por lo tanto, se analiza cada nodo cercano al nodo en
        el cual se encuentra posicionado actualmente.
        
        '''
        
        # Se analiza el nodo cercano posicionado a la derecha
        if self.maze[y][x + 1] != color(0, 0, 0):
            caminos_posibles.append((x + 1, y))
        
        # Se analiza el nodo cercano posicionado a la izquierda
        if self.maze[y][x - 1] != color(0, 0, 0):
            caminos_posibles.append((x - 1, y))
        
        # Se analiza el nodo cercano posicionado abajo
        if self.maze[y - 1][x] != color(0, 0, 0):
            caminos_posibles.append((x, y - 1))
        
        # Se analiza el nodo cercano posicionado arriba
        if self.maze[y + 1][x] != color(0, 0, 0):
            caminos_posibles.append((x, y + 1))
        

        # Se regresa el valor de todos los posibles caminos
        return caminos_posibles
        
    # La funcion stepTest permite determinar los movimientos que se deben hacer para encontrar el shortest_path
    def stepTest(self):
        for cost_index in range(len(self.costos)):
            if self.vecinos[cost_index] not in self.all_pixels and self.costos[cost_index] == self.costo_minimo:
                self.line_up.append(self.vecinos[cost_index])
                self.all_pixels.append(self.vecinos[cost_index])
                self.came_from[self.vecinos[cost_index]] = self.current
                    
    # La funcion actions sirve para la implentacion del funcionamiento del algoritmo A* Search Algorithm
    def actions(self):
        self.line_up.append(self.inicio)
        self.all_pixels.append(self.inicio)
        self.came_from = {self.inicio: None}

        while self.line_up:
            
            self.current = self.line_up.pop(0)
            
            self.goalTest()
            
            
            self.vecinos = self.pathTest(self.current)
        
            self.costos = self.costTest(self.vecinos)
        
            for costIndex in range(len(self.costos)):
                if self.vecinos[costIndex] in self.all_pixels:
                
                    self.costos[costIndex] = 999999
                
            self.costo_minimo = min(self.costos)
            self.stepTest()
