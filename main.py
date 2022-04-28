import csv
from clase import ViajeroF

if __name__ == "main":
    archivo = open('viajero.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        Numv = int(fila[0])
        dni = int(fila[1])
        nombre = str(fila[2])
        apellido = str(fila[3])
        millasa = int(fila[4])
        viajero = ViajeroF(Numv, dni, nombre, apellido, millasa)
        viajero.Menu()
        lvf = []
        lvf.append(viajero)
        print(lvf)
    archivo.close()
