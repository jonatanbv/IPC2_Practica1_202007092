from elemento import Elemento
from listaDoble import ListaDoble
import xml.etree.ElementTree as ET
from xml.dom import minidom

if __name__ == '__main__':
    tree = ET.parse('inf.xml')
    root = tree.getroot()
    #listaPlataforma = root.getroot('ListaPlataformas') 
    lista = ListaDoble()


    for elemento in root.iter('ListaPlataformas'):
        for el in elemento.findall('Plataforma'):
                
            codigo = el.find('codigo').text
            nombre = el.find('nombre').text

            lista.insertarFinal(codigo, nombre)

    lista.mostrar()
    lista.orden()
    print('-------------Ordenando----------')
    lista.mostrar()



    