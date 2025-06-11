import tkinter as tk
from collections import deque

class NodoNArio:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class ArbolNArio:
    def __init__(self, n):
        self.n = n  # cantidad máxima de hijos por nodo
        self.raiz = None
        self.cola = deque()  # para insertar en orden de niveles

    def insertar(self, valor):
        nuevo = NodoNArio(valor)
        if self.raiz is None:
            self.raiz = nuevo
            self.cola.append(nuevo)
        else:
            while self.cola:
                padre = self.cola[0]
                if len(padre.hijos) < self.n:
                    padre.hijos.append(nuevo)
                    self.cola.append(nuevo)
                    break
                else:
                    self.cola.popleft()

    def recorrido_preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            for hijo in nodo.hijos:
                self._preorden(hijo, resultado)

class InterfazArbolNArio:
    def __init__(self, arbol):
        self.arbol = arbol
        self.ventana = tk.Tk()
        self.ventana.title(f"Árbol N-ario (máx {arbol.n} hijos por nodo)")
        self.canvas = tk.Canvas(self.ventana, width=1000, height=700, bg="white")
        self.canvas.pack()

        self.entrada = tk.Entry(self.ventana)
        self.entrada.pack()

        self.boton = tk.Button(self.ventana, text="Insertar", command=self.insertar_valor)
        self.boton.pack()

        self.resultado = tk.Label(self.ventana, text="", font=("Arial", 12))
        self.resultado.pack()

    def insertar_valor(self):
        valor = self.entrada.get().strip().upper()
        if valor.isalpha() and len(valor) == 1:
            self.arbol.insertar(valor)
            self.canvas.delete("all")
            self.dibujar_arbol(self.arbol.raiz, 500, 40, 400)
            recorrido = self.arbol.recorrido_preorden()
            self.resultado.config(text="Recorrido Preorden: " + " - ".join(recorrido))

    def dibujar_arbol(self, nodo, x, y, ancho_total):
        if nodo is None:
            return

        r = 20
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill="lightblue")
        self.canvas.create_text(x, y, text=str(nodo.valor), font=("Arial", 12, "bold"))

        num_hijos = len(nodo.hijos)
        if num_hijos == 0:
            return

        separacion = ancho_total / max(num_hijos, 1)
        inicio_x = x - (ancho_total / 2) + (separacion / 2)

        for i, hijo in enumerate(nodo.hijos):
            nuevo_x = inicio_x + i * separacion
            nuevo_y = y + 100
            self.canvas.create_line(x, y + r, nuevo_x, nuevo_y - r)
            self.dibujar_arbol(hijo, nuevo_x, nuevo_y, ancho_total / self.arbol.n)

    def ejecutar(self):
        self.ventana.mainloop()

# Cambia el valor aquí para probar diferentes árboles N-arios
N = 3  # Árbol ternario
arbol = ArbolNArio(N)
interfaz = InterfazArbolNArio(arbol)
interfaz.ejecutar()
