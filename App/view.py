"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

default_limit = 1000 
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def loadData(catalog):
    controller.loadData(catalog)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("6- Encontrar buenos videos por categoría")
    print("2- Encontrar buenos videos por categoría y país")
    print("3- Encontrar video tendencia por país")
    print("4- Encontrar video tendencia por categoría")
    print("5- Buscar los videos con más Likes")
    print("0- Salir")

catalog = None

def fullfunck(num1,num2):
    """catalog = controller.initCatalog(num1,num2)
    (a,b) = controller.loadData(catalog)
    print("Cargando información de los archivos... Esto puede tardar un poco.")
    if catalog == None:
        print("No ha seleccionado una opcion valida")
    else:
        print('Videos cargados: ' + str(lt.size(catalog['ListCompleteVidAll'])))
        print('Categorías cargados: ' + str(lt.size(catalog['categories'])))
        print("Tiempo [ms]: ", f"{a:.3f}", "  ||  ", "Memoria [kB]: ", f"{b:.3f}")"""
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n(recuerde que antes de escoger cualquier opción tiene que cargar primero la información del catálogo)\n')
    if int(inputs[0]) == 1:
        """opc = [1,2]
        opc1 = [1,2,3]
        for i in opc:
            for j in opc1:
                fullfunck(i,j)"""
        catalog = controller.initCatalog()
        (a,b) = controller.loadData(catalog)
        print("Cargando información de los archivos... Esto puede tardar un poco.")
        if catalog == None:
            print("No ha seleccionado una opcion valida")
        else:
            print('Videos cargados: ' + str(lt.size(catalog['ListCompleteVidAll'])))
            print('Categorías cargados: ' + str(lt.size(catalog['categories'])))
            print("Tiempo [ms]: ", f"{a:.3f}", "  ||  ", "Memoria [kB]: ", f"{b:.3f}") 


    elif int(inputs[0]) == 2:
        print ("Encontrar buenos videos por categoría y país")
        size = int(input("¿De que tamaño quiere la lista?: "))
        name = input("¿De que categoría desea saber los videos?: ")
        country = input("¿De que pais desea saber los videos?: ")
        resul = controller.reqUno(catalog,name,size,country)
        print(resul)
        
            
    elif int(inputs[0]) == 3:
        print ("Encontrar video tendencia por país")
        """country = input("Ingrese el nombre del país del cual quiere saber el video que más fue tendencia: ")
        print(controller.req2(catalog, country))"""
        

    elif int(inputs[0]) == 4:
        print('Encontrar videos tendencias por categoría')
        """category = input("Ingrese la categoria de la cual quiera saber el video que más fue tendencia: ")
        print(controller.req3(catalog,category))"""


    elif int(inputs[0]) == 5:
        print('Buscar los videos con mas likes de un pais y con un tag determinados')
        """country = input("Ingrese el pais del cual  quiera conocer los videos con mas likes: ")
        tag = input("Ingrese el tag del cual quiera saber los videos: ")
        size = int(input("Ingrese la cantidad de videos que quiera conocer: "))
        result = controller.req4(catalog,tag,country,size)
        if result == 0:
            print("El numero de muestra seleccionado, excede el tamaño de la cantidad total de elementos que hay")
        else:
            print(result)"""

    elif int(inputs[0]) == 6:
        print('Buscar los videos con mas likes de una categoría')
        name = input("Escriba el nombre de la categoría de la cual quiere conocer los videos: ")
        size = int(input("Escriba cuantos videos quiere conocer: "))
        print(controller.reqLab(catalog, name, size))
        
    
    else:
        sys.exit(0)
        
sys.exit(0)

