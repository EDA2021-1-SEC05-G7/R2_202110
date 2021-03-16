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
    print("2- Encontrar buenos videos por categoría y país")
    print("3- Encontrar video tendencia por país")
    print("4- Encontrar video tendencia por categoría")
    print("5- Buscar los videos con más Likes")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n(recuerde que antes de escoger cualquier opción tiene que cargar primero la información del catálogo)\n')
    if int(inputs[0]) == 1:
        catalog = controller.initCatalog()
        loadData(catalog)
        print("Cargando información de los archivos... Esto puede tardar un poco.")
        if catalog == None:
            print("No ha seleccionado una opcion valida")
        else:
            print('Videos cargados: ' + str(lt.size(catalog['ListCompleteVidAll'])))
            

    elif int(inputs[0]) == 2:
        print ("Encontrar buenos videos por categoría y país")
        """#size = int(input("¿De que tamaño quiere la lista?: "))
        #name = input("¿De que categoría desea saber los videos?: ")
        #country = input("¿De que pais desea saber los videos?: ")
        #if size > lt.size(catalog['ListCompleteVidAll']):
            print("El numero de muestra seleccionado, excede el tamaño de la cantidad total de elementos que hay")
        else:
            resul = controller.req1(catalog,name,country,size)
            print(resul)"""
        
            
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
    else:
        sys.exit(0)
        
sys.exit(0)

