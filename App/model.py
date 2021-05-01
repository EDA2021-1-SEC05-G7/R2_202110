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
from DISClib.DataStructures import arraylistiterator as it

from pprint import pprint

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """tipo = ""
    factor = 0"""
    catalog = {'ListCompleteVidAll': None,
               'categories': None,
               'videos-cat': None}
    """if num1 == 1:
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
            factor = 6.00"""
    catalog['ListCompleteVidAll'] = lt.newList("ARRAY_LIST")
    catalog['categories'] = mp.newMap(numelements=44,
                                    maptype="PROBING",
                                    loadfactor=0.5)
    catalog["videos-cat"] = mp.newMap(numelements=500,
                                    maptype="CHAINING",
                                    loadfactor=4.0)
    catalog["videos-pais"] = mp.newMap(numelements=500,
                                    maptype="CHAINING",
                                    loadfactor=4.0)
    
    return catalog



# Funciones para agregar informacion al catalogo


def addVideo(catalog, video):
    lt.addLast(catalog['ListCompleteVidAll'], video)
    #addCatVid(catalog,video)


def addCat(catalog, cat):
    mp.put(catalog["categories"],cat["name"].strip(), cat["id"].strip())
    



# Funciones para creacion de datos

def newVidCat(ids):
    entry = {'cat': "", "videos": None}
    entry['cat'] = ids
    entry['videos'] = lt.newList('ARRAY_LIST')
    return entry


def newVidPais(pais):
    toxic = {"pais": "", "videos": None}
    toxic["pais"] = pais
    toxic["videos"] = lt.newList('ARRAY_LIST')
    return toxic


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



def addPaisVid(catalog, video):
    paiss = catalog["videos-pais"]     #"paiss" guarda el map dentro del catalogo que tiene la información de los videos ordenada por paises
    pai = video["country"]             #"pai" guarda el pais del video que le toxic por parametro
    existpai = mp.contains(paiss, pai) #revisa si el map "paiss" contiene la llave "pai" (el pais) y retorna true o false
    if existpai:                       #el "if" inicia si "existpai" es true
        toxic = mp.get(paiss, pai)     #"toxic" guarda la pareja (llave,valor) de la llave "pai" (el pais)
        pais = me.getValue(toxic)      #retorna el Valor de la pareja llave,valor que retorna "toxic"
    else:                              #si el map "paiss" no tiene la llave "pai" entonces se ejecuta este "else"
        pais = newVidPais(pai)         #"pais" guarda el diccionario que retorna la funcion "newVidPais()" con "pai" como valor del key "pais"
        mp.put(paiss, pai, pais)       #pone en el map "paiss", en la llave "pai" el dict "pais"
    lt.addLast(pais["videos"], video)  #añade un nuevo a la lista que esta dentro de la llave "videos" en el dict "pais"


# Funciones de consulta

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


def ReqUno(catalog, name, size, country):
    idee = mp.get(catalog["categories"], name)
    ideev = me.getValue(idee)
    valor = mp.get(catalog["videos-cat"],ideev)
    lista = me.getValue(valor)["videos"]
    nuevl = lt.newList(datastructure="ARRAY_LIST")
    iterator = it.newIterator(lista)
    while it.hasNext(iterator):
        aire = it.next(iterator)
        if aire["country"].lower() == country.lower():
            newdict = {"trending_date": aire['trending_date'],
            'title': aire['title'],
            "channel_title": aire['channel_title'],
            "publish_time": aire["publish_time"],
            'views': aire['views'],
            "likes": aire['likes'], 
            "dislikes": aire['dislikes']}
            lt.addLast(nuevl,newdict)


    nuevaLista = sortVideos(nuevl, size, cmpVideosByViews)

    return nuevaLista


def ReqDos(catalog, country):
    videitos = mp.get(catalog["videos-pais"], country)
    #print(mp.valueSet(catalog["videos-pais"]))
    #print(videitos)
    videillos = me.getValue(videitos)["videos"]
    ceteras = mp.newMap(numelements=500,
                    maptype="CHAINING",
                    loadfactor=4.0)
    dickss = mp.newMap(numelements=500,
                    maptype="CHAINING",
                    loadfactor=4.0)
    iterator = it.newIterator(videillos)
    while it.hasNext(iterator):
        tierra = it.next(iterator)
        if mp.contains(ceteras,tierra['title']):
            pareja = mp.get(ceteras,tierra['title'])
            valor = me.getValue(pareja) + 1
            mp.put(ceteras,tierra["title"],valor)
        else:
            mp.put(ceteras,tierra["title"],1)
            mp.put(dickss,tierra["title"],tierra)
    k = None
    mx = -1
    varx = mp.keySet(ceteras)
    itr = varx["first"]
    if itr == None:
        return None
    while itr:
        element = itr["info"]
        cnt = mp.get(ceteras, element)
        cnts = me.getValue(cnt)
        if cnts > mx:
            mx = cnts
            k = element
        itr = itr["next"] 
    zzz = mp.get(dickss,k)
    b = me.getValue(zzz)
    result = {'Title': b["title"], 'Channel_title': b['channel_title'], 'Country': country, 'Número de días': mx}
    return result
    
def ReqTres(catalog, name):
    idee = mp.get(catalog["categories"], name)
    #print(catalog["categories"])
    ideev = me.getValue(idee)
    valor = mp.get(catalog["videos-cat"],ideev)
    #print(valor)
    lista = me.getValue(valor)["videos"]
    catss = mp.newMap(numelements=500,
                    maptype="CHAINING",
                    loadfactor=4.0)
    dickss = mp.newMap(numelements=500,
                    maptype="CHAINING",
                    loadfactor=4.0)
    iterator = it.newIterator(lista)
    while it.hasNext(iterator):
        tierra = it.next(iterator)
        if mp.contains(catss,tierra['title']):
            #cats[tierra["title"]] += 1
            pareja = mp.get(catss,tierra['title'])
            valor = me.getValue(pareja) + 1
            mp.put(catss,tierra["title"],valor)
            
        else:
            mp.put(catss,tierra["title"],1)
            mp.put(dickss,tierra["title"],tierra)
    #(a, b) = max((catss[key], key) for key in catss)

    k = None
    mx = -1
    varx = mp.keySet(catss)
    itr = varx["first"]
    if itr == None:
        return None
    while itr:
        element = itr["info"]
        cnt = mp.get(catss, element)
        cnts = me.getValue(cnt)
        if cnts > mx:
            mx = cnts
            k = element
        itr = itr["next"] 
    zzz = mp.get(dickss,k)
    b = me.getValue(zzz)
    result = {'title': b["title"], 'channel_title': b['channel_title'], 'category_id': b["category_id"], 'número de días': mx}
    return result

    #return 
def ReqCuatro(catalog, tag, country, size):
    videitos = mp.get(catalog["videos-pais"], country)
    videillos = me.getValue(videitos)["videos"]
    elqueitera = it.newIterator(videillos)
    tagslist = lt.newList(datastructure="ARRAY_LIST")
    while it.hasNext(elqueitera):
        fuego = it.next(elqueitera)
        etiquetas = fuego["tags"].split("|")
        for j in etiquetas:
            if tag.lower() in j.lower():
                """dictiquetas = mp.newMap()
                mp.put(dictiquetas, "title",fuego['title'])
                mp.put(dictiquetas, "channel_title",fuego['channel_title'])
                mp.put(dictiquetas, "publish_time",fuego['publish_time'])
                mp.put(dictiquetas, "views",fuego['views'])
                mp.put(dictiquetas, "likes",fuego['likes'])
                mp.put(dictiquetas, "dislikes",fuego['dislikes'])
                mp.put(dictiquetas, "tags",fuego['tags'])"""
                lt.addLast(tagslist, fuego)

    if size > lt.size(tagslist):
        ordenation = 0
    else:
        ordenation = sortVideos(tagslist,size,cmpVideosByLikes)
    return ordenation




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


def cmpVideosByViews(video1, video2): 
    return (float(video1['views']) > float(video2['views']))

# Funciones de ordenamiento


def sortVideos(lst,size,cmp):
    copia_lista = lst.copy()
    list_orden = mgs.sort(copia_lista, cmp)
    resul = lt.subList(list_orden, 1, size)
    return resul
