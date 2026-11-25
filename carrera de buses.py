
import time
import os
import random

# Configuración
META = 23
pos_f19 = 0
pos_h15 = 0

ANCHO_CONSOLA = 90
ANCHO_BUS = 65
POS_META = META + ANCHO_BUS

# Función para centrar textos
def centrar(texto):
    print(texto.center(ANCHO_CONSOLA))


# Diseño del bus articulado
def dibujar_bus(nombre):
    return [
        " ______________________________________",
        f"|   _   _   _   |###|  _   _   _   |{nombre:<3}|",
        "|  |_| |_| |_|  |###| |_| |_| |_|  |   |",
        "|---------------|###|-TRANSMILENIO-|___|",
        "|___ (o)(o) ____|###|______ (o)(o) ____|",
    ]


# Calcular ancho real del bus
ANCHO_REAL = max(len(linea) for linea in dibujar_bus("F19"))

# Posición de llegada
LLEGADA = POS_META - ANCHO_REAL


# Dibujar pista y meta
def dibujar_pista(posicion, linea):
    linea = linea.ljust(ANCHO_REAL)
    espacios = max(0, POS_META - posicion - ANCHO_REAL)
    print(" " * posicion + linea + " " * espacios + "##")


# Presentación inicial
print("\n")
print("=" * ANCHO_CONSOLA)
centrar("¡¡¡¡¡¡¡ CARRERA DE BUSES !!!!!!!")
print("=" * ANCHO_CONSOLA)

time.sleep(2)


# Carrera
while pos_f19 < LLEGADA and pos_h15 < LLEGADA:

    os.system("cls" if os.name == "nt" else "clear")

    # Movimiento aleatorio
    pos_f19 += random.randint(3, 4)
    pos_h15 += random.randint(3, 4)

    pos_f19 = min(pos_f19, LLEGADA)
    pos_h15 = min(pos_h15, LLEGADA)

    print("\n")
    print("=" * ANCHO_CONSOLA)
    centrar("¡¡¡¡¡¡¡ CARRERA DE BUSES !!!!!!!")
    print("=" * ANCHO_CONSOLA)

    # BUS F19
    print("\n F19")
    for linea in dibujar_bus("F19"):
        dibujar_pista(pos_f19, linea)

    print()

    # BUS H15
    print("\n H15")
    for linea in dibujar_bus("H15"):
        dibujar_pista(pos_h15, linea)

    time.sleep(0.20)


# Resultado final
print("\n")
print("=" * ANCHO_CONSOLA)

if pos_f19 == pos_h15:
    centrar("EMPATE, LOS DOS SON MUY RÁPIDOS")
elif pos_f19 >= LLEGADA:
    centrar("¡GANÓ EL F19! SOLO BANDERAS LKS")
else:
    centrar("¡GANÓ EL H15! SOLO TUNAL LKS")

print("=" * ANCHO_CONSOLA)
