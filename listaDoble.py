from elemento import Elemento

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertarFinal(self, codigo, nombre):
        elemento = Elemento(codigo, nombre)

        if self.primero is None:
            self.primero = elemento
            self.ultimo = elemento
        else:
            elemento.anterior = self.ultimo
            self.ultimo.siguiente = elemento
            self.ultimo = elemento

    def mostrar(self):
        if self.primero is None:
            print('Lista Vacia')
        else:
            aux = self.primero
            while aux is not None:
                print(f'Codigo: {aux.codigo} ---- Nombre: {aux.nombre}')
                aux = aux.siguiente

    def orden(self):
        aux = self.primero
        while aux is not None:
            aux2 = aux.siguiente
            while aux2 is not None:
                if int(aux.codigo) > int(aux2.codigo):
                    temp = aux.codigo
                    aux.codigo = aux2.codigo
                    aux2.codigo = temp

                    temp = aux.nombre
                    aux.nombre = aux2.nombre
                    aux2.nombre = temp
                aux2 = aux2.siguiente
            aux = aux.siguiente
