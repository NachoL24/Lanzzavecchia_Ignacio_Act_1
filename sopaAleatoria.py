import random
import string

class SopaAleatoria():
    __sopaSize = 15
    __sopa = []

    def generar(self) -> list:
        for _ in range(self.__sopaSize):
            fila = []
            for _ in range(self.__sopaSize):
                fila.append(random.choice(string.ascii_uppercase))
            self.__sopa.append(fila)
    
    def getSopa(self):
        return self.__sopa
    
    def modificarSopa(self, sopa):
        self.__sopa = sopa
    
    def finalizarSopa(self):
        for i in range(len(self.__sopa)):
            for j in range(len(self.__sopa)):
                self.__sopa[i][j] = self.__sopa[i][j].upper()

    def imprimirSopa(self):
        self.finalizarSopa()
        for fila in self.__sopa:
            print(fila)

    def ubicarHorizontalAlDerecho(self, palabra: str):
        lenPalabra = len(palabra)
        while True:
            try:
                randomRow = random.randint(0, self.__sopaSize - 1)
                randomCol = random.randint(0, self.__sopaSize - lenPalabra)
                for i in range(lenPalabra):
                    if self.__sopa[randomRow][randomCol + i].islower() and self.__sopa[randomRow][randomCol + i] != palabra[i]:
                        raise ValueError
                for i in range(lenPalabra):
                    self.__sopa[randomRow][randomCol + i] = palabra[i]
                return
            except ValueError:
                print("se busca otra ubicacion")   

    def ubicarHorizontalAlReves(self, palabra: str):
        lenPalabra = len(palabra)
        while True:
            try:
                randomRow = random.randint(0, self.__sopaSize - 1)
                randomCol = random.randint(lenPalabra - 1 , self.__sopaSize - 1)
                for i in range(lenPalabra):
                    if self.__sopa[randomRow][randomCol - i].islower() and self.__sopa[randomRow][randomCol - i] != palabra[i]:
                        raise ValueError
                for i in range(lenPalabra):
                    self.__sopa[randomRow][randomCol - i] = palabra[i]
                return 
            except ValueError:
                print("se busca otra ubicacion")

    def ubicarVerticalAlDerecho(self, palabra: str):
        lenPalabra = len(palabra)
        while True:
            try:
                randomCol = random.randint(0, self.__sopaSize - 1)
                randomRow = random.randint(0, self.__sopaSize - lenPalabra)
                for i in range(lenPalabra):
                    if self.__sopa[randomRow + i][randomCol].islower() and self.__sopa[randomRow + i][randomCol] != palabra[i]:
                        raise ValueError
                for i in range(lenPalabra):
                    self.__sopa[randomRow + i][randomCol] = palabra[i]
                return
            except ValueError:
                print("se busca otra ubicacion")

    def ubicarVerticalAlReves(self, palabra: str):
        lenPalabra = len(palabra)
        while True:
            try:
                randomCol = random.randint(0, self.__sopaSize - 1)
                randomRow = random.randint(lenPalabra - 1, self.__sopaSize - 1)
                for i in range(lenPalabra):
                    if self.__sopa[randomRow - i][randomCol].islower() and self.__sopa[randomRow - i][randomCol] != palabra[i]:
                        raise ValueError
                for i in range(lenPalabra):
                    self.__sopa[randomRow - i][randomCol] = palabra[i]
                return
            except ValueError:
                print("se busca otra ubicacion")