import tkinter as tk
from collections import deque

class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.x = 0
        self.y = 0

class ArbolCompleto:
    def _init_(self):
        self.raiz = None
        self.cola = deque()  # para insertar hijos por niveles

    def insertar(self, valor):
        nuevo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo
            self.cola.append(nuevo)
        else:
            while self.cola:
                padre = self.cola[0]
                if padre.izquierda is None:
                    padre.izquierda = nuevo
                    self.cola.append(nuevo)
                    break
                elif padre.derecha is None:
                    padre.derecha = nuevo
                    self.cola.append(nuevo)
                    self.cola.popleft()
                    break

    def recorrido_inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        if nodo:
            self._inorden(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden(nodo.derecha, resultado)

class InterfazArbol:
    def _init_(self, arbol):
        self.arbol = arbol
        self.ventana = tk.Tk()
        self.ventana.title("Árbol Binario Completo (Letras)")
        self.canvas = tk.Canvas(self.ventana, width=800, height=600, bg="white")
        self.canvas.pack()

        self.entrada = tk.Entry(self.ventana)
        self.entrada.pack()

        self.boton = tk.Button(self.ventana, text="Insertar", command=self.insertar_valor)
        self.boton.pack()

        self.texto_resultado = tk.Label(self.ventana, text="", font=("Arial", 12))
        self.texto_resultado.pack()

    def insertar_valor(self):
        valor = self.entrada.get()
        if valor.isalpha() and len(valor) == 1:
            self.arbol.insertar(valor.upper())
            self.canvas.delete("all")
            self.dibujar_arbol(self.arbol.raiz, 400, 40, 200)
            recorrido = self.arbol.recorrido_inorden()
            self.texto_resultado.config(text="Recorrido Inorden: " + " - ".join(recorrido))

    def dibujar_arbol(self, nodo, x, y, espacio):
        if nodo is None:
            return

        r = 20
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="lightgreen")
        self.canvas.create_text(x, y, text=str(nodo.valor), font=("Arial", 12, "bold"))

        if nodo.izquierda:
            nx = x - espacio
            ny = y + 80
            self.canvas.create_line(x, y, nx, ny)
            self.dibujar_arbol(nodo.izquierda, nx, ny, espacio // 2)

        if nodo.derecha:
            nx = x + espacio
            ny = y + 80
            self.canvas.create_line(x, y, nx, ny)
            self.dibujar_arbol(nodo.derecha, nx, ny, espacio // 2)

    def ejecutar(self):
        self.ventana.mainloop()

# ---------------------------------------------
# Ejecutar la interfaz
arbol = ArbolCompleto()
interfaz = InterfazArbol(arbol)
interfaz.ejecutar()
