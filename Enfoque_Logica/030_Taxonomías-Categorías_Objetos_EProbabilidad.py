class Categoria:
    def __init__(self, nombre, subcategorias=None):
        self.nombre = nombre
        self.subcategorias = subcategorias if subcategorias is not None else []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)


# Definimos las categor�as de la taxonom�a
animalia = Categoria("Animalia")
mamiferos = Categoria("Mam�feros")
aves = Categoria("Aves")
reptiles = Categoria("Reptiles")

# Agregamos subcategor�as a la categor�a Animalia
animalia.agregar_subcategoria(mamiferos)
animalia.agregar_subcategoria(aves)
animalia.agregar_subcategoria(reptiles)

# Definimos algunos objetos en las categor�as
gato = Categoria("Gato")
perro = Categoria("Perro")
ballena = Categoria("Ballena")

mamiferos.agregar_subcategoria(gato)
mamiferos.agregar_subcategoria(perro)
mamiferos.agregar_subcategoria(ballena)

aguila = Categoria("�guila")
pinguino = Categoria("Ping�ino")
colibri = Categoria("Colibr�")

aves.agregar_subcategoria(aguila)
aves.agregar_subcategoria(pinguino)
aves.agregar_subcategoria(colibri)

cocodrilo = Categoria("Cocodrilo")
serpiente = Categoria("Serpiente")
lagartija = Categoria("Lagartija")

reptiles.agregar_subcategoria(cocodrilo)
reptiles.agregar_subcategoria(serpiente)
reptiles.agregar_subcategoria(lagartija)

# Funci�n para imprimir la taxonom�a
def imprimir_taxonomia(categoria, nivel=0):
    print("  " * nivel + categoria.nombre)
    for subcategoria in categoria.subcategorias:
        imprimir_taxonomia(subcategoria, nivel + 1)

# Imprimimos la taxonom�a
imprimir_taxonomia(animalia)
