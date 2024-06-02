#Vamos a limpiar los datos de los archivos del directorio prueba5-7


import os

#primero queremos normalizar cada archivo, para después sumarlos y 
#hacer el promedio de cada longitud de onda, para finalmente guardar
#los datos en un diccionario para cada uno de los archivos de texto

#En la primer columna se encuentra la longitud de onda y en la segunda
#la intensidad de la luz, por lo que nuestro diccionario tendrá como
#llave la longitud de onda y como valor la intensidad de la luz

#definimos una función que transfiere los datos de un archivo a un diccionario

def archivo_diccionario(archivo):
    diccionario = {}
    with open(archivo, 'r') as file:
        #Empecamos por la linea que contiene datos, que es la 14

        for linea in file.readlines()[14:]:
            linea = linea.strip()
            datos = linea.split()
            diccionario[float(datos[0])] = float(datos[1])
    return diccionario

#print(archivo_diccionario('prueba5-17\sinsal\sinsal_HRC06701__0__61.txt'))

#Ahora queremos normalizar los datos de cada archivo, para esto
#vamos a restarle a cada valor de la intensidad de la luz el valor
#mínimo de la intensidad de la luz y después dividirlo entre la diferencia
#entre el valor máximo y el valor mínimo de la intensidad de la luz

def normalizar(diccionario):
    valores = diccionario.values()
    minimo = min(valores)
    maximo = max(valores)
    for lamda in diccionario:
        diccionario[lamda] = (diccionario[lamda] - minimo)/(maximo - minimo)
    return diccionario

#print(normalizar(archivo_diccionario('prueba5-17\sinsal\sinsal_HRC06701__0__61.txt')))

#Ahora queremos sumar los diccionarios de los archivos de texto
#para después dividir cada valor entre el número de archivos
#para obtener el promedio de cada longitud de onda

def promedio_diccionarios(diccionarios):
    promedio = {}
    for diccionario in diccionarios:
        for lamda in diccionario:
            if lamda not in promedio:
                promedio[lamda] = diccionario[lamda]
            else:
                promedio[lamda] += diccionario[lamda]
    for lamda in promedio:
        promedio[lamda] = promedio[lamda]/len(diccionarios)
    return promedio

#Ahora queremos guardar los datos en un archivo csv que creamos nombrandolo 
#como f'promedio_{directorio}.csv' donde directorio es el directorio donde
#se encuentran los archivos de texto

def diccionario_csv(diccionario, archivo):
    with open(archivo, 'w') as file:
        file.write('Longitud de onda, Intensidad de la luz\n')
        for lamda in diccionario:
            file.write(f'{lamda}, {diccionario[lamda]}\n')


#Ahora queremos limpiar los archivos de un directorio, para esto
#vamos a hacer uso de las funciones anteriores

def limpiar_directorio(directorio):
    archivos = os.listdir(directorio)
    diccionarios = []
    for archivo in archivos:
        diccionarios.append(normalizar(archivo_diccionario(f'{directorio}/{archivo}')))
    promedio = promedio_diccionarios(diccionarios)
    diccionario_csv(promedio, 'promedio.csv')
    os.rename('promedio.csv', f'{directorio}_promedio.csv')

#ahora vamos a limpiar todos los directorios de prueba5-7

for directorio in os.listdir('prueba5-17'):
    limpiar_directorio(f'prueba5-17/{directorio}')