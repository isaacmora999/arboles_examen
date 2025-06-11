from collections import deque

# -------------------------
# Clase Nodo para árbol N-ario
# -------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# -------------------------
# Operaciones
# -------------------------

def preorden(node):
    """Recorrido en preorden (DFS)"""
    if node:
        print(node.value, end=" ")
        for child in node.children:
            preorden(child)

def bfs(root):
    """Recorrido por niveles (BFS)"""
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.value, end=" ")
        for child in current.children:
            queue.append(child)

def contar_hojas(node):
    """Cuenta los nodos hoja (sin hijos)"""
    if not node.children:
        return 1
    return sum(contar_hojas(child) for child in node.children)

def altura(node):
    """Altura del árbol"""
    if not node.children:
        return 1
    return 1 + max(altura(child) for child in node.children)

def buscar(node, objetivo):
    """Buscar un valor en el árbol"""
    if node.value == objetivo:
        return node
    for child in node.children:
        resultado = buscar(child, objetivo)
        if resultado:
            return resultado
    return None

def contar_nodos(node):
    """Contar todos los nodos del árbol"""
    return 1 + sum(contar_nodos(child) for child in node.children)

# -------------------------
# Crear un árbol de ejemplo
# -------------------------

# Estructura:
#         A
#      /  |  \
#     B   C   D
#    / \       \
#   E   F       G

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

a.add_child(b)
a.add_child(c)
a.add_child(d)
b.add_child(e)
b.add_child(f)
d.add_child(g)

# -------------------------
# Demostración
# -------------------------

print("▶ Recorrido Preorden:")
preorden(a)

print("\n\n▶ Recorrido BFS (por niveles):")
bfs(a)

print("\n\n▶ Número de hojas:", contar_hojas(a))
print("▶ Altura del árbol:", altura(a))
print("▶ Total de nodos:", contar_nodos(a))

buscado = "E"
encontrado = buscar(a, buscado)
print(f"▶ Buscar '{buscado}':", "Encontrado" if encontrado else "No encontrado")
