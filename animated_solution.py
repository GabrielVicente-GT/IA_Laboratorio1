
import time as temporizador
from wr_functions import *
from wr_bmp import *
import numpy as np
import pygame

class Animate(object):

    def __init__(self, height, widht, visitados, corto):
        self.width = widht*10
        self.height = height*10
        self.CeldasX, self.CeldasY = height, widht
        self.DimensionX = self.width / self.CeldasX
        self.DimensionY = self.height / self.CeldasY
        self.camino_naranja = corto
        self.camino_morado = visitados

        #Mapa con posicions x, y volteadas
        bmp_read =  Read("./Laberintos/NewMaze.bmp")
        self.mapa = [[color(bmp_read.pixels[y][x][0],bmp_read.pixels[y][x][1],bmp_read.pixels[y][x][2]) for x in range(bmp_read.width)]for y in range(bmp_read.height)]

        #Animacion
        self.animar()

    def animar(self):
        pygame.init()
        PantallaVisualiation = pygame.display.set_mode((self.width, self.height))
        PantallaVisualiation.fill((0,0,0))
        EstadoActual = np.zeros((self.CeldasX,self.CeldasY))

        #Cambiar la posicion de los arreglos
        mapa_casillas = list(map(list, zip(*self.mapa[::-1])))
        dividendo = self.CeldasY/2-0.5
        CaminoCorto = [(x, 2*dividendo-y) for x, y in self.camino_naranja]
        CaminoCorto = CaminoCorto[::-1]
        TodosLosPasos = [(x, 2*dividendo-y) for x, y in self.camino_morado]

        EjecucionEstado = 0
        while True:

            SiguienteEstado = np.copy(EstadoActual)

            #Se agrega un delay para apreciar los frames
            temporizador.sleep(0.0)

            PantallaVisualiation.fill((0,0,0))
            try:
                if len(TodosLosPasos) != 0:
                    pixel = TodosLosPasos.pop(0)
                else:
                    pixel = CaminoCorto.pop(0)
            except:
                pass

            #Se espera si el usuario cierra la pantalla
            EventoUsuario = pygame.event.get()
            for interaccion in EventoUsuario:
                if pygame.QUIT == interaccion.type:
                    pygame.quit()

            #Se pinta cada pixel en la ventana creada
            #y el color varia dependiendo del numero asignado
            for y in range(0,self.CeldasX):
                for x in range(0,self.CeldasY):

                    #Ancho y largo representado en cada pixel
                    FormaPixel = [((x) * self.DimensionX, y * self.DimensionY),
                            ((x+1) * self.DimensionX, y * self.DimensionY),
                            ((x+1) * self.DimensionX, (y+1) * self.DimensionY),
                            ((x) * self.DimensionX, (y+1) * self.DimensionY)]

                    #Si el color obtenido es rojo, verde, negro. Se le asigna un valor
                    #a los estados siguientes
                    if  mapa_casillas[x][y] == color(0,0,0):
                        SiguienteEstado[x,y] = 3
                    if  mapa_casillas[x][y] == color(255,0,0):
                        SiguienteEstado[x,y] = 4
                    if  mapa_casillas[x][y] == color(0,255,0):
                        SiguienteEstado[x,y] = 5
                    #Si el estado actual es 0 o 7 asignar a siguiente estados el color a pintar
                    if EstadoActual[x,y]==7 and (x,y) == pixel and len(TodosLosPasos) == 0:
                        SiguienteEstado[x,y] = 1
                    if EstadoActual[x,y]==0 and (x,y) == pixel and len(TodosLosPasos) != 0:
                        SiguienteEstado[x,y] = 7

                    #Dependiendo la asignacion en Siguientes estados se dibuja el polgono
                    if SiguienteEstado[x,y] == 0:
                        pygame.draw.polygon(PantallaVisualiation, (255,255,255),FormaPixel,0)
                    if SiguienteEstado[x,y] == 1:
                        pygame.draw.polygon(PantallaVisualiation,(243, 156, 18),FormaPixel,0)
                    if SiguienteEstado[x,y] == 3:
                        pygame.draw.polygon(PantallaVisualiation, (0,0,0),FormaPixel,0)
                    if SiguienteEstado[x,y] == 4:
                        pygame.draw.polygon(PantallaVisualiation, (255,0,0),FormaPixel,0)
                    if SiguienteEstado[x,y] == 5:
                        pygame.draw.polygon(PantallaVisualiation, (0,255,0),FormaPixel,0)
                    if SiguienteEstado[x,y] == 7:
                        pygame.draw.polygon(PantallaVisualiation, (125, 60, 152),FormaPixel,0)

            EjecucionEstado +=1
            EstadoActual = np.copy(SiguienteEstado)
            pygame.display.update()
