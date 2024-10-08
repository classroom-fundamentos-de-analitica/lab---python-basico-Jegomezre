"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv

def pregunta_01(): 
    suma = 0

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            suma += int(fila[1])

    return suma


def pregunta_02():
    letras = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            letras.append(fila[0])
    
    salida = []
    
    for letra in sorted(set(letras)):
        salida.append((letra, letras.count(letra)))

    return salida


def pregunta_03():
    letras = []
    conteo = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            if not fila[0] in letras:
                letras.append(fila[0])
                conteo.append(int(fila[1]))
            else:
                conteo[letras.index(fila[0])] += int(fila[1])

    salida = []
    
    for letra in sorted(letras):
        salida.append((letra, conteo[letras.index(letra)]))

    return salida

def pregunta_04():
    meses = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            mes = fila[2].split('-')[1]
            meses.append(mes)

    salida = []

    for mes in sorted(set(meses)):
        salida.append((mes, meses.count(mes)))

    return salida
    
def pregunta_05():
    letras = []
    conteo = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            if not fila[0] in letras:
                letras.append(fila[0])
                conteo.append([int(fila[1])])
            else:
                conteo[letras.index(fila[0])].append(int(fila[1]))

    salida = []

    for letra in sorted(set(letras)):
        salida.append((letra, max(conteo[letras.index(letra)]), min(conteo[letras.index(letra)])))
    
    return salida

def pregunta_06():
    cadenas = []
    valores = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            diccionario = fila[4].split(',')

            for elemento in diccionario: 
                cadena = elemento.split(':')[0]
                valor = elemento.split(':')[1]

                if cadena not in cadenas:
                    cadenas.append(cadena)
                    valores.append([int(valor)])
                else:
                    valores[cadenas.index(cadena)].append(int(valor))

    salida = []

    for cadena in sorted(cadenas):
        salida.append((cadena, min(valores[cadenas.index(cadena)]), max(valores[cadenas.index(cadena)])))

    return salida

def pregunta_07():
    numeros = []
    letras = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            if int(fila[1]) not in numeros:
                numeros.append(int(fila[1]))
                letras.append([fila[0]])
            else:
                letras[numeros.index(int(fila[1]))].append(fila[0])

    salida = []

    for numero in sorted(numeros):
        salida.append((numero, letras[numeros.index(numero)]))

    return salida

def pregunta_08():
    numeros = []
    letras = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            if int(fila[1]) not in numeros:
                numeros.append(int(fila[1]))
                letras.append({fila[0]})
            else:
                letras[numeros.index(int(fila[1]))].add(fila[0])

    salida = []

    for numero in sorted(numeros):
        salida.append((numero, list(sorted(letras[numeros.index(numero)]))))

    return salida

def pregunta_09():
    salida = {}

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            diccionario = fila[4].split(',')

            for elemento in diccionario: 
                cadena = elemento.split(':')[0]

                if cadena not in salida.keys():
                    salida[cadena] = 1
                else:
                    salida[cadena] += 1

    return dict(sorted(salida.items()))

def pregunta_10():
    salida = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            col4 = len(fila[3].split(','))
            col5 = len(fila[4].split(','))
            salida.append((fila[0], col4, col5))
    
    return salida

def pregunta_11():
    letras = {}

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            for letra in fila[3].split(','):
                if not letra in letras.keys():
                    letras[letra] = int(fila[1])
                else:
                    letras[letra] += int(fila[1])

    return dict(sorted(letras.items()))


def pregunta_12():
    letras = {}

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            letra = fila[0]
            
            for elemento in fila[4].split(','):
                numero = int(elemento.split(':')[1])

                if not letra in letras.keys():
                    letras[letra] = numero
                else:
                    letras[letra] += numero

    return dict(sorted(letras.items()))
