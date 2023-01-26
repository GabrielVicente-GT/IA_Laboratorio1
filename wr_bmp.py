#Archivo que contiene las clases Write y Read
#Que permiten escribir y leer un archivo BMP
#Implementacion general vista en graficas

from wr_functions import *

class Write(object):

    def __init__(self, width, height):
            self.width  = width
            self.heigth = height
            self.laberinto = None

    def write(self, filename):
        file_access = open(filename, 'bw')
        file_access.write( char('B'))
        file_access.write( char('M'))
        file_access.write( dword(54 + self.width * self.heigth * 3))
        file_access.write( word(0))
        file_access.write( word(0))
        file_access.write( dword(54))

        #info header

        file_access.write( dword(40))
        file_access.write( dword(self.width))
        file_access.write( dword(self.heigth))
        file_access.write( word(1))
        file_access.write( word(24))
        file_access.write( dword(0))
        file_access.write( dword(self.width*self.heigth*3))
        file_access.write( dword(0))
        file_access.write( dword(0))
        file_access.write( dword(0))
        file_access.write( dword(0))

        for y in range(self.heigth):
            for x in range(self.width):
                file_access.write(self.framebuffer[y][x])

        file_access.close()

class Read:
    def __init__(self, path):
        self.path = path

        with open (self.path, "rb") as image:

            image.seek(10)
            header_size = struct.unpack("=l", image.read(4))[0]

            image.seek(2+4+2+2+4+4)
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            image.seek(header_size)
            self.pixels = []

            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))

                    #Dependiendo del rango de valores b,g,r, se agrega en sef.pixels[y]
                    #Un arreglo de rojo, verde,negro o blanco
                    if b<50 and g<50 and r<50:
                        self.pixels[y].append((0,0,0))
                    elif b>50 and g>50 and r>50:
                        self.pixels[y].append((255,255,255))
                    elif r>200 and g<50 and b<50:
                        self.pixels[y].append((255,0,0))
                    elif g>200 and r<50 and b<50:
                        self.pixels[y].append((0,255,0))
                    else:
                        self.pixels[y].append((0,0,0))
