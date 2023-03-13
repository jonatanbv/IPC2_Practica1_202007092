from elemento import Elemento
from listaDoble import ListaDoble
import xml.etree.ElementTree as ET
from xml.dom import minidom
from listaJuego import ListaJuego
from tkinter import filedialog

if __name__ == '__main__':
    def leerXML():
        print('hola')
            
    
    def crearXMLFind(listaPlataformas, listaJuegos):
        archivo = open('datos.xml', 'w')
        archivo.write('<JuegosViejos>\n')
        archivo.write(listaPlataformas)
        archivo.write(listaJuegos)
        archivo.write('\n</JuegosViejos>')
        archivo.close()
    
    flag = True
    ruta = ''


    while flag:
        print('1. Ingresar XML')
        print('2. Ordenar Plataformas')
        print('3. Crear xml')
        print('4. Salir')

        option = input('Ingrese una opcion: ')

        if int(option) == 1:
            ruta = filedialog.askopenfilename(title='Abrir')
                                              
        elif int(option) == 2:
            tree = ET.parse(ruta)
            root = tree.getroot()
            #listaPlataforma = root.getroot('ListaPlataformas') 


            lista = ListaDoble()
            for elemento in root.iter('ListaPlataformas'):
                for el in elemento.findall('Plataforma'):
                        
                    codigo = el.find('codigo').text
                    nombre = el.find('nombre').text

                    lista.insertarFinal(codigo, nombre)


            listGame = ListaJuego()
            for elemento in root.iter('ListadoJuegos'):
                for el in elemento.findall('Juego'):
                    codigo = el.find('codigo').text
                    nombre = el.find('nombre').text
                    for e in el.iter('Plataforma'):
                        plataforma = e.find('codigo').text

                    listGame.insertar(codigo, nombre, plataforma)

            fl = True
            while fl:
                print('1. Ordenar Plataformas[Menor-Mayor]')
                print('2. Ordenar Juegos[Menor-Mayor]')
                print('3. Ordenar Juegos por Plataforma[Menor-Mayor]')
                print('4. Salir')

                op = input('Ingresa una opcion: ')
                
                if int(op) == 1:
                    lista.orden()
                    print('\n------------- LISTA ORDENADA ---------------')
                    lista.mostrar()
                    print('Se ordeno correctamente\n')
                elif int(op)==2:

                    listGame.ordenCodigoJuego()
                    print('\n--------- LISTA ORDENADA DE JUEVOS ---------')
                    listGame.mostrar()
                    print('Se ordeno Correctamente la lista de juegos\n')

                elif int(op) == 3:
                    listGame.ordenCodigoPlataforma()
                    print("\n-- LISTA DE JUEGOS ORDENADA POR PLATAFORMA--")
                    print('Se ordeno correctamente la lista de juegos por plataformas\n')
                elif int(op)==4:
                    fl = False
                else:
                    print('Ingresa una opcion valida')


        elif int(option) == 3:
            platafor = lista.escribirXML()
            juegos = listGame.crearXMLJuegos()

            crearXMLFind(platafor, juegos)

        elif int(option) == 4:
            flag = False
            print('finalizo')
        else:
            print('ingrese una opcion valida')
        

    """print('-------------Plataforma Ordenando----------')
    lista.orden()
    lista.mostrar()
    print('----------------Juegos Ordenados---------------')
    listGame.ordenCodigoJuego()
    listGame.mostrar()

    strlista = lista.escribirXML()
    print(strlista)
    strJuego = listGame.crearXMLJuegos()
    print(strJuego)

    crearXMLFind(str(strlista), str(strJuego))"""


    