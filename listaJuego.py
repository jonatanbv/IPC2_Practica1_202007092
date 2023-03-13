from Juego import Juego

class ListaJuego:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, codigo, nombre, plataforma):
        juego = Juego(codigo, nombre, plataforma)

        if self.primero is None:
            self.primero = juego
            self.ultimo = juego
        else:
            juego.anterior = self.ultimo
            self.ultimo.siguiente = juego
            self.ultimo = juego

    def mostrar(self):
        if self.primero is None:
            print('lista Vacia')
        else:
            aux = self.primero
            while aux is not None:
                print(f'Codigo: {aux.codigo} -- Nombre: {aux.nombre} -- plataforma: {aux.plataforma}')
                aux = aux.siguiente
            
    def ordenCodigoJuego(self):
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

                    temp = aux.plataforma
                    aux.plataforma = aux2.plataforma
                    aux2.plataforma = temp

                aux2 = aux2.siguiente
            aux = aux.siguiente

    def ordenCodigoPlataforma(self):
        aux = self.primero
        while aux is not None:
            aux2 = aux.siguiente
            while aux2 is not None:
                if int(aux.plataforma) > int(aux2.plataforma):
                    temp = aux.codigo
                    aux.codigo = aux2.codigo
                    aux2.codigo = temp

                    temp = aux.nombre
                    aux.nombre = aux2.nombre
                    aux2.nombre = temp

                    temp = aux.plataforma
                    aux.plataforma = aux2.plataforma
                    aux2.plataforma = temp

                aux2 = aux2.siguiente
            aux = aux.siguiente

    def crearXMLJuegos(self):
        if self.primero is None:
            print('la lista esta vacia')
        else:
            stringin = ''
            stringin = stringin+'<ListaJuegos>\n'

            aux = self.primero
            while aux is not None:

                stringin=stringin+'\t<Juego>\n'
                stringin=stringin+f'\t\t<codigo>{aux.codigo}</codigo>\n'
                stringin=stringin+f'\t\t<nombre>{aux.nombre}</nombre>\n'
                stringin=stringin+'\t\t<Plataforma>\n'
                stringin=stringin+f'\t\t\t<codigo>{aux.plataforma}</codigo>\n'
                stringin=stringin+'\t\t</Plataforma>\n'
                stringin=stringin+'\t</Juego>\n'

                aux = aux.siguiente

            stringin=stringin+'</ListaJuegos>'
            return stringin



