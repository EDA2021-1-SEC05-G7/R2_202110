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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'ListCompleteVidAll': None,
               'categories': None}

    catalog['ListCompleteVidAll'] = lt.newList("ARRAY_LIST")
    catalog['categories'] = mp.newMap(numelements=44,
                                    maptype="CHAINING",
                                    loadfactor=4.0)
    catalog["videos-cat"] = mp.newMap(numelements=50000,
                                    maptype="PROBING",
                                    loadfactor=0.5)
    
    return catalog



# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    lt.addLast(catalog['ListCompleteVidAll'], video)
    addCatVid(catalog,video)

def addCat(catalog, cat):
    mp.put(catalog["categories"],cat["name"],cat["id"])
    



# Funciones para creacion de datos

def newVidCat(ids):
    entry = {'cat': "", "videos": None}
    entry['cat'] = ids
    entry['videos'] = lt.newList('SINGLE_LINKED')
    return entry
def addCatVid(catalog,video):
    cats = catalog["videos-cat"]
    category = video["category_id"]
    existcat = mp.contains(cats,category)
    contadorif = 0
    contadorelse = 0
    if existcat:
        contadorif += 1
        print("if",contadorif)
        entry = mp.get(cats,category)
        cat = me.getValue(entry)
    else:
        contadorelse
        print("else",contadorelse)
        cat = newVidCat(category)
        mp.put(cats,category,cat)
    lt.addLast(cat["videos"],video)


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def compareId(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

# Funciones de ordenamiento
