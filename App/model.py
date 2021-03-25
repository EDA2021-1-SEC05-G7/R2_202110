"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mgs

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(num1,num2):
    tipo = ""
    factor = 0
    catalog = {'ListCompleteVidAll': None,
               'categories': None,
               'videos-cat': None}
    if num1 == 1:
        tipo = "PROBING"
        if num2 == 1:
            factor = 0.30
        elif num2 == 2:
            factor = 0.50
        elif num2 == 3:
            factor = 0.80
    elif num1 == 2:
        tipo = "CHAINING"
        if num2 == 1:
            factor = 2.00
        elif num2 == 2:
            factor = 4.00
        elif num2 == 3:
            factor = 6.00
    print("vamos en el tipo: ",tipo, "con factor: ", factor)
    catalog['ListCompleteVidAll'] = lt.newList("ARRAY_LIST")
    catalog['categories'] = mp.newMap(numelements=44,
                                    maptype=tipo,
                                    loadfactor=factor)
    catalog["videos-cat"] = mp.newMap(numelements=500,
                                    maptype="PROBING",
                                    loadfactor=0.5)
    
    return catalog



# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    lt.addLast(catalog['ListCompleteVidAll'], video)
    addCatVid(catalog,video)

def addCat(catalog, cat):
    mp.put(catalog["categories"],cat["name"].strip(), cat["id"].strip())
    



# Funciones para creacion de datos

def newVidCat(ids):
    entry = {'cat': "", "videos": None}
    entry['cat'] = ids
    entry['videos'] = lt.newList('ARRAY_LIST')
    return entry

def addCatVid(catalog,video):
    cats = catalog["videos-cat"]
    category = video["category_id"]
    existcat = mp.contains(cats,category)
    if existcat:
        entry = mp.get(cats,category)
        cat = me.getValue(entry)
    else:
        cat = newVidCat(category)
        mp.put(cats,category,cat)
    lt.addLast(cat["videos"],video)

def ReqLab(catalog, name, size):
    idee = mp.get(catalog["categories"], name)
    #print(catalog["categories"])
    ideev = me.getValue(idee)
    
    valor = mp.get(catalog["videos-cat"],ideev)
    lista = me.getValue(valor)["videos"]
    nuevaLista = sortVideos(lista, size, cmpVideosByLikes)
    return nuevaLista

    """
    print(catalog["videos-cat"])"""

# Funciones de consulta


# Funciones utilizadas para comparar elementos dentro de una lista

def compareId(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def cmpVideosByLikes(video1,video2):
    return (float(video1['likes']) > float(video2['likes']))


# Funciones de ordenamiento

def sortVideos(lst,size,cmp):
    copia_lista = lst.copy()
    list_orden = mgs.sort(copia_lista, cmp)
    resul = lt.subList(list_orden, 1, size)
    return resul
