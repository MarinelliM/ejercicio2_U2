class ViajeroF:
    __Numv = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millasa = ""

    def __int__(self, Numv, dni, nombre, apellido, millasa):
        self.__Numv = Numv
        self.__dni = dni
        self.__millasa = millasa
        self.__nombre = nombre
        self.__apellido = apellido

    def Cantidadtm(self):
        print("la cantidad de millas es de {}".format(self.__millasa))

    def acumularmillas(self, millas):
        self.__millasa+millas
        print("La cantidad de millas acumuladas es de {}".format(self.__millasa))


    def canjearmillas(self, canjear):
        if self.__millasa >= canjear:
            self.__millasa-canjear
            print("Se canjearon sus millas, le quedan {} millas acumuladas".format(self.__millasa-canjear))
        else:
            print('No tiene las millas suficientes')

    def Menu(self):
        op=int(input("Ingrese una opcion(1.consultar cantidad de millas| 2.Acumular millas| 3.Canjear millas):"))
        if op==1:
            self.Cantidadtm()
        elif op==2:
            self.acumularmillas(int(input("ingrese la cantidad de millas a acumular:")))
        elif op==3:
            self.canjearmillas(int(input("ingrese las millas a canjear:")))
        else:
            print("la opcion ingresada no es aceptada")
