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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()

    return catalog

def loadData(catalog):
    # Videos:
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)
        model.addCatVid(catalog,video)
    # Categorias: 
    catfile = cf.data_dir + 'category-id.csv'
    input_cat_file = csv.DictReader(open(catfile, encoding="utf-8"),  delimiter='\t')
    for cat in input_cat_file:
        model.addCat(catalog, cat)

# Funciones para la carga de datos

# Funciones de ordenamiento

def reqLab(catalog, name, size):

    return model.ReqLab(catalog, name, size)


# Funciones de consulta sobre el catálogo

# pruebas
"""catalog = initCatalog()
loadData(catalog)
print(model.prueba(catalog,"28"))"""

