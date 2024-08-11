from time import sleep
from sopaAleatoria import SopaAleatoria
import random
#debe instalar el modulo customtkinter con: pip install customtkinter o pip install -r requirements.txt
import customtkinter

#el programa se inicia con el boton "run python file" de arriba a la derecha

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sopa de letras")
        self.wordList = []
        self.sopaA = SopaAleatoria()
        self.sopaA.generar()
        self.wordsWidgets = []

        self.grid_columnconfigure(0, weight=1)

        self.textEntry = customtkinter.CTkEntry(self, placeholder_text="Ingrese una palabra")
        self.textEntry.grid(row=0, column=0, padx=50, pady=10, sticky="e")

        self.button = customtkinter.CTkButton(
            self, 
            text = "Agregar Palabra" if len(self.wordList) < 5 else "Iniciar", 
            command = self.ingresarPalabra if len(self.wordList) < 5 else self.iniciarJuego()
        )
        self.button.grid(row=0, column=1, padx=(0,30), pady=(10), sticky="w")

        self.counterLabel = customtkinter.CTkLabel(self, text="Ingrese 5 palabras")
        self.counterLabel.grid(row=1, pady=10, columnspan=2, sticky="ew")

        self.words_frame = customtkinter.CTkFrame(self)
        self.words_frame.grid(row=2, columnspan=2, padx=10, pady=(0,10), sticky="ew")

        for i in range(5):
            self.wordsWidgets.append(customtkinter.CTkLabel(self.words_frame, text=""))
            self.wordsWidgets[i].grid(row=i, column=0, padx=10, pady=5, sticky="w")

        self.mainloop()

    def ingresarPalabra(self):
        if(len(self.textEntry.get()) <= 15 and self.textEntry.get().isalpha() and " " not in self.textEntry.get()):
            self.wordList.append(self.textEntry.get().lower())
            self.counterLabel.configure(
                require_redraw=True, 
                text=f"Ingrese {5 - len(self.wordList)} palabras mas" if len(self.wordList) < 5 else "sopa de letras lista")
            for i in range(len(self.wordList)):
                self.wordsWidgets[i].configure(require_redraw=True, text=self.wordList[i])
                self.wordsWidgets[i].grid(row=i, column=0, padx=10, pady=5, sticky="w")
            self.textEntry.delete(0, "end")
            self.button.configure(
                require_redraw=True,
                text="Agregar Palabra" if len(self.wordList) < 5 else "Iniciar", 
                command = self.ingresarPalabra if len(self.wordList) < 5 else self.iniciarJuego
            )
        else:
            self.counterLabel.configure(require_redraw=True, text=f"'{self.textEntry.get()}' no es una palabra válida")
            self.textEntry.delete(0, "end")

    def iniciarJuego(self):
        for word in self.wordList:
            orientacion = random.choice(["verticalD", "verticalI", "horizontalD", "horizontalI"])
            if orientacion == "horizontalD":
                self.sopaA.ubicarHorizontalAlDerecho(word)
            elif orientacion == "horizontalI":
                self.sopaA.ubicarHorizontalAlReves(word)
            elif orientacion == "verticalD":
                self.sopaA.ubicarVerticalAlDerecho(word)
            elif orientacion == "verticalI":
                self.sopaA.ubicarVerticalAlReves(word)
        self.destroy()
        #self.sopaA.finalizarSopa() #comentar esta linea si quiere encontrar rapido las palabras (las pone en minusculas)
        app = VentanaSopa(self.sopaA)#.iniciarSopa(self.sopaA)

class VentanaSopa(customtkinter.CTk):
    def __init__(self, sopa):
        super().__init__()
        # self.geometry("550x480")
        self.title("Sopa de letras")
        self.sopaA = sopa.getSopa()
        self.solution = []
        self.notSolution = []
        solCounter = 0
        notSolCounter = 0
        for i in range(len(self.sopaA)):
            for j in range(len(self.sopaA)):
                if self.sopaA[i][j].isupper():
                    button = customtkinter.CTkButton(self, 
                        width=32, 
                        height=32, 
                        text=self.sopaA[i][j], 
                        fg_color="grey", 
                        corner_radius=10,
                        command=lambda pos=notSolCounter: self.setColorRed(pos)
                    )
                    button.grid(row=i, column=j, padx=0, pady=0)
                    self.notSolution.append(button)
                    notSolCounter += 1
                else:
                    button = customtkinter.CTkButton(self, 
                        width=32, 
                        height=32, 
                        text=self.sopaA[i][j].upper(), 
                        fg_color="grey", 
                        corner_radius=10,
                        command=lambda pos=solCounter: self.setColorGreen(pos),
                    )
                    button.grid(row=i, column=j, padx=0, pady=0)
                    self.solution.append(button)
                    solCounter += 1

        self.showSolution = customtkinter.CTkButton(self, text="Mostrar solucion", command=self.mostrarSolucion)
        self.showSolution.grid(row=7, column=16, padx=10, pady=0)
        self.mainloop()
    
    def mostrarSolucion(self):
        for i in range(len(self.solution)):
            self.solution[i].configure(require_redraw=True, fg_color="green", text_color="black")
    
    def setColorRed(self, pos):
        self.notSolution[pos].configure(require_redraw=True, fg_color="red", text_color="black", hover=False)
       
    def setColorGreen(self, pos):
        self.solution[pos].configure(require_redraw=True, fg_color="green", text_color="black", hover=False)

app = App()



