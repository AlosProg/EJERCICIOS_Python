"""
# Ejercicio 1

print("Antonio Luis Ojeda Soto")
print("Getafe")

# Ejercicio 2: AREA DE UNA HABITACIÓN

longitud = float(input("Introduzca la longitud: "))
ancho = float(input("Introduzca el ancho: "))
area = longitud*ancho
print("El area es: ", area)

# Ejercicio 3: AREA EN ACRES

pies=43560
longitud = float(input("Introduzca la longitud: "))
ancho = float(input("Introduzca el ancho: "))
area_acres = longitud*ancho/pies
print("El area es: ", area_acres, "acres")

# Ejercicio 5: DEPÓSITOS EN BOTELLA

menos_depósito=0.10
mas_depósito=0.25

botellas_menos=int(input("Cuantas botellas de menos de 1l tiene? "))
botellas_mas=int(input("Cuantas botellas de más de 1l tiene? "))

importe_total=botellas_menos*menos_depósito + botellas_mas*mas_depósito
print ("Tu importe total es $%.2f." % importe_total)

# Ejercicio 6: IMPUESTOS Y PROPINAS

propina=1.00
impuesto=0.21

comida=int(input("Cuánto cuesta la comida? "))
comida_total=comida +(comida*impuesto)+propina
print("El total de la comida es: %.2f €" % comida_total)

# Ejercicio 7: SUMA DE LOS PRIMEROS N ENTEREOS POSITIVOS

numero=int(input("Dame un número "))
suma=int(numero*(numero+1)/2)
print("La suma de los", numero, "primeros numeros es", suma)

# Ejercicio 8: WIDGETS Y GIZMOS

peso_widget= 75
peso_gizmo= 112

cantidad_widgets=int(input("Dame la cantidad de widgets que quieres "))
cantidad_gizmos=int(input("Dame la cantidad de gizmos que quieres "))
peso_total= (cantidad_widgets*peso_widget+cantidad_gizmos*peso_gizmo)/1000
print("El peso total del pedido es %.1f" % peso_total, "Kg")

# Ejercicio 9: INTERÉS COMPUESTO

interes=4
ahorros=int(input("Dime tus ahorros "))
total = interes/100*ahorros+ahorros
print("El saldo total del primer año es %.2f" % total, "€")
total = interes/100*total+total
print("El saldo total del segundo año es %.2f" % total, "€")
total = interes/100*total+total
print("El saldo total del segundo año es %.2f" % total, "€")

# Ejercicio 10: ARITMÉTICA
import math

num1=int(input("Dame un número "))
num2=int(input("Dame otro número "))

print("La suma es ", num1+num2)
print("La resta es ", num1-num2)
print("El produco es ", num1*num2)
print("El cociente es ", num1/num2)
print("El resto es ", num1%num2)
print("La potencia es ", num1**num2)
print("El resultado de log10 de",num1,"es", math.log10(num1))

# Ejercicio 11: Eficiencia de combustible (de galones y millas a litros y kilómetros

distanciaUSA=int(input("Dime las millas que recorre tu coche "))
cantidadUSA=int(input("Dime los galones que consume tu coche "))
distanciaCanada=distanciaUSA/1.6
cantidadCanada=cantidadUSA*0.26
print("Lo que consume tu coche en medidas canadienses es ",cantidadCanada, "litros /",distanciaCanada, "Kms" )

# Ejercicio 12: DISTANCIA ENTRE DOS PUNTOS DE LA TIERRA
import math

latitud1=int(input("Dame la latitud del punto 1 "))
longitud1=int(input("Dame la longitud del punto 1 "))
latitud2=int(input("Dame la latitud del punto 2 "))
longitud2=int(input("Dame la longitud del punto 2 "))

distancia = 6371.01 * math.acos(math.sin (latitud1) * math.sin (latitud2) +
                                math.cos (latitud1) * math.cos (latitud2) *
                                math.cos (longitud1 - longitud2))

print("La distancia es %.2f" % distancia, "Kms")

# Ejercicio 13: HACER CAMBIOS

monedas200= 200
monedas100= 100
monedas25= 25
monedas10= 10
monedas5= 5

centimos=int(input("Ingrese el número de céntimos "))

print("Monedas de 200 céntimos:", int(centimos/monedas200))
centimos=centimos%monedas200

print("Monedas de 100 céntimos:", int(centimos/monedas100))
centimos=centimos%monedas100

print("Monedas de 25 céntimos:", int(centimos/monedas25))
centimos=centimos%monedas25

print("Monedas de 10 céntimos:", int(centimos/monedas10))
centimos=centimos%monedas10

print("Monedas de 5 céntimos:", int(centimos/monedas5))
centimos=centimos%monedas5

# Ejercicio 14: UNIDADES DE ALTURA

pies=int(input("Dame tus pies "))
pulgadas=int(input("Dame tus pulgadas "))

centímetros=int((pies*12*2.54)+(pulgadas*2.54))
print("Mides ", centímetros, "cms de altura")

# Ejercicio 15: UNIDADES DE DISTANCIA

pies=int(input("Dime cuantos pies hay de distancia "))

print("Las pulgadas que hay son", int(pies*12*2.54))
print("Las yardas que hay son", int(pies*12*2.54/91))
print("Las millas que hay son", float(pies*12*2.54/100/1600))

# Ejercicio 16: AREA Y VOLUMEN

import math
radio=int(input("Dame el radio "))
area=math.pi*radio**2
volumen=4/3*math.pi*radio**3
print("El área es", area, "y el volumen es", volumen)

# Ejercicio 26: HORA ACTUAL
import time
print(time.asctime())

# Ejercicio 27: INDICE DE MASA CORPORAL

peso=float(input("Dame tu peso en kilogramos "))
altura=float(input("Dame tu peso en metros "))

IMC =peso/altura**altura
print("Tu índice de masa corporal es ", IMC)

# Ejercicio 31: SUMA DE LOS DÍGITOS DE UN ENTERO

numero=int(input("Dame un entero de cuatro cifras "))
suma=0

resto=numero%10
suma=suma+resto
numero=int(numero/10) # se tiene que poner el int para que dé solamente la parte entera de la división

resto=numero%10
suma=suma+resto
numero=int(numero/10)

resto=numero%10
suma=suma+resto
numero=int(numero/10)
suma=suma+numero

print(suma)

# Ejercicio 32: ORDENAR 3 ENTEROS

x=int(input("Dame un entero "))
y=int(input("Dame un entero "))
z=int(input("Dame un entero "))

mini=min(x,y,z)
maxi=max(x,y,z)
med=x+y+z-mini-maxi

print("El orden de colocacion es ", mini,med,maxi)

# SENTENCIAS IF
# Ejercicio 34: ¿PAR O IMPAR?

numero=int(input("Dame un entero "))
if numero%2==0:
    print("El numero",numero,"es par")
else:
    print("El numero",numero,"es impar")

# Ejercicio 35: AÑOS DEL PERRO

años=int(input("Dame los años humanos que tienes "))
if años<=2:
    años=años*10.5
    print("Los años perrunos son", años)
elif años>2:
    años=años-2
    años=años*4+21
    print("Los años perrunos son", años)
elif años<=0:
    print("La edad introducida es errónea")

# Ejercicio 36: vocal o consonante

letra=input("Dame una letra del alfabeto ")
if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print("La letra es una vocal")
elif letra=="y":
    print("A veces será vocal, a veces será consonante")
else:
    print("La letra es una consonante")


# Ejercicio 37: NOMBRA ESA FORMA

lados=int(input("Dame el número de lados de la forma "))
if lados==3:
    print("Es un triángulo")
elif lados==4:
    print("Es un cuadrilátero")
elif lados==5:
    print("Es un pentágono")
elif lados==6:
    print("Es un hexágono")
elif lados==7:
    print("Es un heptágono")
elif lados==8:
    print("Es un octógono")
elif lados==9:
    print("Es un nonágono")
elif lados==10:
    print("Es un decágono")
elif lados<3:
    print("El número de lados es inválido")
elif lados>10:
    print("El número de lados no es soportado por este programa")


# Ejercicio 40: NOMBRE DEL TRIÁNGULO

lado1=int(input("Dame la longitud del primer lado "))
lado2=int(input("Dame la longitud del segundo lado "))
lado3=int(input("Dame la longitud del tercer lado "))

if lado1==lado2 and lado1==lado3:
    print("Es un triángulo equilátero")
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
    print("Es triángulo isósceles")
else:
    print("Es triángulo escaleno")

# Ejercicio 44: FECHA DEL NOMBRE DEL DÍA FESTIVO

mes=input("Dame el nombre del mes ")
día=int(input("Dame el día del mes "))

if mes=="enero" and día==1:
    print("Es año nuevo")
elif mes=="julio" and día==1:
    print("Es el día de Canadá")
elif mes=="diciembre" and día==25:
    print("Es navidades")
else:
    print("No es festivo")


# Ejercicio 45: ¿DE QUÉ COLOR ES ESE CUADRADO DEL TABLERO DE AJEDREZ?

letra=input("Dame una letra de la 'a' a la 'h' ")
numero=int(input("Dame un número del 1 al 8 "))

if (letra=="a" or letra=="c" or letra=="e" or letra=="g") and (numero%2!=0):
    print("La casilla es negra")
elif (letra=="a" or letra=="c" or letra=="e" or letra=="g") and (numero%2==0):
    print("La casilla es blanca")
if (letra=="b" or letra=="d" or letra=="f" or letra=="h") and (numero%2==0):
    print("La casilla es negra")
elif (letra=="b" or letra=="d" or letra=="f" or letra=="h") and (numero%2!=0):
    print("La casilla es blanca")

# Ejercicio 48: ZODÍACO CHINO

año=int(input("Dame un año "))
if año%12==8:
    print("AÑO DEL DRAGÓN")
elif año%12 ==9:
    print("AÑO DE LA SERPIENTE")
elif año%12 ==10:
    print("AÑO DEL CABALLO")
elif año%12 ==11:
    print("AÑO DE LA OVEJA")
elif año%12 ==0:
    print("AÑO DEL MONO")
elif año%12 ==1:
    print("AÑO DEL GALLO")
elif año%12 ==2:
    print("AÑO DEL PERRO")
elif año%12 ==3:
    print("AÑO DEL CERDO")
elif año%12 ==4:
    print("AÑO DE LA RATA")
elif año%12 ==5:
    print("AÑO DEL BUEY")
elif año%12 ==6:
    print("AÑO DEL TIGRE")
elif año%12 ==7:
    print("AÑO DE LA LIEBRE")

# Ejercicio 49: ESCALA DE RICHTER

rango=float(input("Deme el rango de la magnitud del terremoto "))
if rango<2.0:
    print("El terremoto es micro")
elif rango>=2 and rango<3:
    print("El terremoto es muy menor")
elif rango>=3 and rango<4:
    print("El terremoto es menor")
elif rango>=4 and rango<5:
    print("El terremoto es ligero")
elif rango>=5 and rango<6:
    print("El terremoto es moderado")
elif rango>=6 and rango<7:
    print("El terremoto es fuerte")
elif rango>=7 and rango<8:
    print("El terremoto es mayor")
elif rango>=8 and rango<10:
    print("El terremoto es excelente")
elif rango>10:
    print("El terremoto es meteórico")
"""

# EJERCICIOS DE BUCLES (While o For, o ambos, depende del problema)
"""
# Exercise 61: PROMEDIO
contador=0
resultado=0.0

numero=float(input("Dame un número "))

if numero == 0:
    print("Error, no se puede hacer promedio de 0")
while numero>0:
    resultado = resultado + numero
    contador = contador + 1
    numero=float(input("Dame un número "))

resultado=resultado/contador
print("El promedio de la nota es",round(resultado,1))

# Exercise 62: Tabla de descuento de una unidad de un producto.

cantidad=int(input("Dime los productos que quieres--> "))
precioP=float(input("Dime el producto que quieres--> "))

while precioP==4.95 or precioP==9.95 or precioP==14.95 or precioP==19.95 or precioP==24.95:
    total = 0
    precioD = precioP * 0.40 # como queremos un descuento del 60% del producto lo multiplicamos por 0,40 para que dé el total
    total = cantidad * precioD # round: para redondear a dos decimales
    print (" El precio original es", precioP, "\n",
           "El descuento de cada unidad es un 40%\n",
           "El valor de los productos con el descuento es %.2f\n" % total) # %.2f es para dos decimales
    precioP = float(input("Dime el producto que quieres---> "))

print("El precio del producto no tiene descuento")


# Exercise 65: CALCULAR EL PERÍMETRO DE UN POLÍGONO

import math

perímetro = 0

primerax=int(input("Dime la coordenada de x: "))
primeray=int(input("Dime la coordenada de y: "))

xprevia = primerax
yprevia = primeray

linea=input("Pulsa cualquier tecla menos Enter para seguir: ")
while(linea!=""):
    x = int(input("Dime la coordenada de x: "))
    y = int(input("Dime la coordenada de y: "))
    totalx = xprevia - x
    totaly = yprevia - y
    lado = math.sqrt((totalx ** 2) + (totaly ** 2)) # teorema de Pitágoras
    perímetro = perímetro + lado
    xprevia = x
    yprevia = y
    linea = input("Si quieres seguir pulsa una tecla, sino pulsa enter: ")

print ("El perímetro total es %.2f" % perímetro)

# Exercise 67: PRECIO DE ADMISIÓN

precioGrupo = 0

edadPersona =int(input("Dame la edad de la persona "))

while(edadPersona != 0):
    if edadPersona <=2:
        precioGrupo = precioGrupo  + 0
    elif edadPersona >=3 and edadPersona <=12:
        precioGrupo = precioGrupo + 14
    elif edadPersona >= 65:
        precioGrupo = precioGrupo + 18
    else:
        precioGrupo = precioGrupo + 23

    edadPersona=int(input("Dame la edad de la persona "))

print ("El precio total del grupo es " , precioGrupo)


# NOTA: esto sirve para contar las veces que se repite una caracter de una cadena de texto
linea = input("Introduce cadena de 8 bits ")
unos = linea.count("1")
print(unos)


# Exercise 69: APROXIMATE PI

a = 2.0
b = 3.0
c = 4.0
Num_pi = 3.0

for i in range(14):
    Num_pi = Num_pi + (4 / (a * b * c))
    a += 2
    b += 2
    c += 2
    Num_pi = Num_pi - (4 / (a * b * c))
    a += 2
    b += 2
    c += 2

print(Num_pi)


# Exercise 70: CIFRADO CESAR

abecedario = "abcdefghijklmnñopqrstuvwxyz" # posiciones de 0 a 26
pos = abecedario.find("z")
print(pos)
mensaje = input ("Dame un mensaje a cifrar o descifrar: ")
rotacion = int(input ("Dame una rotacion: "))

mensaje = mensaje.lower()

def cifrar (mensaje,rotacion):
    cifrado = ""
    for i in mensaje:
        if (i=="." or i=="," or i==" " or i=="?" or i=="!"):
            cifrado = cifrado + "#"
        else:
            posicion = (abecedario.find(i) + rotacion) % 27 # Integer que nos devuelve la posición de la letra x posiciones más avanzada de la original
            cifrado = cifrado + abecedario[posicion] # String de la palabra cifrada según la posición del abecedario
    return print(cifrado)

def descifrar (mensaje,rotacion):
    descifrado = ""
    for i in mensaje:
        if (i=="#"):
            descifrado = descifrado + " "
        else:
            posicion = (abecedario.find(i) - rotacion) % 27
            descifrado = descifrado + str(abecedario[posicion])
    return print(descifrado)

cifrar(mensaje,rotacion)
#descifrar(mensaje,rotacion)

# Exercise 72: Palíndromo
# Función que mira si una palabra es palíndromo

palabra = input("Dame una palabra: ")

def palíndromo (palabra):
    inversa = ""
    for i in palabra:
        inversa = i + inversa
    if (palabra == inversa):
        print("La palabra",palabra,"SI es un palíndromo")
    else:
        print("La palabra",palabra,"NO es un palíndromo")

palíndromo(palabra)


# Exercise 73: Palíndromos de múltiples palabras.
# Función que mira si una frase es palíndroma

import re
def palíndromo (palabra):
    inversa = ""
    for i in palabra:
        inversa = i + inversa
    if (palabra == inversa):
        print("La frase: ",frase," ,SI es un palíndromo.")
    else:
        print("La frase: ",frase," ,NO es un palíndromo.")

frase = input("Dame una frase: ")
frase2 = frase.lower() # Ponemos todas las palabras en minusculas
resul_frase = re.sub(r'[^\w\s]','',frase2) # Quitamos todos los signos de puntuación
resul_frase = resul_frase.replace(' ', '') # Reemplazamos los espacios por nada, o sea unimos todas las palabras
print(resul_frase)
palíndromo(resul_frase) # Llamamos a la función para ver si esa palabra es palíndromo.

# Exercise 75: El máximo común divisor de dos números.
# Para ello utilizaremos el algoritmo de Euclides.
import math
n1 = int(input("Dame un numero entero: "))
n2 = int(input("Dame otro numero entero: "))
lista =[]

if n1 > n2:
    resto1 = n1 % n2
    if (resto1 == 0): # Si el resto da 0 de primeras entonces n2 será el MCD
        print("El MCD de es:", n2)
    else:
        while (resto1 != 0): # Mientras el resto no sea 0...
            lista.append(resto1) # Se van añadiendo los restos a la lista
            n1 = n2 # Traspaso de variables: el divisor pasa a ser el dividendo
            n2 = resto1 # Traspaso de variables: el resto pasa a ser el divisor
            resto1 = n1 % n2 # Se calcula
            print(lista) # Se imprime la lista para ir viendo los resultados
        resultado = min(lista) # Si el resto es 0, se sale del bucle aquí y nos quedamos con el menor de los restos
        print("El MCD de es:", resultado)
else:
    resto2 = n2 % n1 # Igual que el anterior solo que se viene aquí cuando el segundo número es mayor que el prinmero
    if (resto2 == 0):
        print("El MCD es:", n1)
    else:
        while (resto2 != 0):
            lista.append(resto2)
            n1 = n2
            n2 = resto2
            resto2 = n1 % n2
            print(lista)
        resultado2 = min(lista)
        print("El MCD es:", resultado2)


# Exercise 76: Factorización

n = int(input("Dame un número mayor o igual a 2: "))
lista_factores = []
factor = 2

while (factor <= n): # Mientras el factor sea menor que el número pasado por consola...
    if (n % factor == 0): # Si el módulo del número con el factor es 0..
        n = n / factor # ... dividimos y el número va a ser la división del número entre el factor
        print(n)
        lista_factores.append(factor)
    else: # Si no aumentamos el factor en una unidad.
        factor+=1 # factor = factor + 1.
print(lista_factores)

# Exercise 77: De binario a decimal

binario = input("Dame un número en binario: ")
lista = []
decimal = 0

# NOTA: EN PYTHON NO SE PUEDE RECORRER UN NUMERO ENTERO (NO ES ITERABLE), UNA CADENA O UNA LISTA SI SON ITERABLES
for i in reversed (binario): # Ponemos el número al revés en la lista ya que para pasar a decimal se empieza mirando por la izquierda
    lista.append(int(i)) # Vamos añadiendo cada char en la lista y casteando a entero

for i in range(len(lista)): # recorremos la lista y si es 1 elevamos 2 al índice de ése elemento.
                            # donde si pusiésemos solo: for i in lista--> i sería el valor de cada elemento
                            # con: for i in range(len(lista))--> i es el índice de cada elemento
    if (lista[i]==1):# lista[i] es el valor
        decimal = decimal + (2 ** i) # i es el índice// también valdría pow(Base,Exponente)--> pow(2,i)
    else:
        decimal = decimal + 0

print("La conversión a decimal de",binario, "es:",decimal)


# Exercise 78: De decimal a binario

decimal = int(input("Dame un número en decimal: "))
binario = ""
aux = decimal

while (aux >= 2): # mientras el resto sea mayor o igual a 2...
    resto = aux % 2 # ...vamos obteniendo los restos y ...
    binario = str(resto) + binario # ... los vamos metiendo en la variable binario por el principio y casteando a string
    aux = aux // 2 # actualizamos aux quedándonos con la parte entera del cociente(con dos barras //) para la siguiente división
    # print(aux)

binario = str(aux) + binario # aquí tenemos que incorporar el último cociente al resultado binario
print("El numero", decimal,"en binario es:", binario)


# Exercise 79: Máximo entero

import random
maximo = 0
contador = 0

for i in range (100): # i es 0,1,2,3,4,5,6,7,8...
    #print(i)
    aleatorio = random.randrange(1, 100, 1)
    if (aleatorio > maximo):
        maximo = aleatorio
        print(aleatorio,"<== modificado")
        contador +=1
    else:
        print(aleatorio)

print ("El máximo valor encontrado fué: ",maximo)
print ("El máximo valor fué modificado", contador, "veces")


# Exercise 80: Simulación de tiradas de moneda

from random import choice

aux = 0 # nos dirá el total de todas las tiradas de los 10 ciclos para luego calcular el promedio

for i in range (10):
    lista = []
    contador = 0 # contador de tiradas
    for i in range(3): # hacemos tres tiradas eligiendo o "H" o "T"
        tirada = choice(["H", "T"])
        lista.append(tirada)
        contador += 1

    while (lista[-1]!=lista[-2] or lista[-1]!=lista[-3] or lista[-2]!=lista[-3]):
        tirada = choice(["H", "T"])
        lista.append(tirada)
        contador += 1
    aux = aux + contador
    print(lista, "(",contador,"tiradas )")

promedio = aux / 10
print ("El promedio de tiradas fué: ", promedio)




# EJERCICIOS DE FUNCIONES

# Exercise 81: Computar la hipotenusa
import math

def hipotenusa (num1,num2):
    resultado = (math.sqrt((num1**2) + (num2**2)))
    return print("La hipotenusa de",num1,"y",num2,"es",resultado)

# Exercise 82: Tarifa de taxi (solo pasar como parámetro la distancia en kilómetros)

TARIFA_VARIABLE = 0.25
TARIFA_BASE = 4

def tarifataxi (dist):
    dist = (dist * 1000) # pasamos a metros
    subtotal = round(((dist / 140) * TARIFA_VARIABLE),2) # obtenemos el dinero según los metros recorridos con 2 decimales
    total = subtotal + TARIFA_BASE # obtenemos el total sumándole a los metros recorridos la tarifa base
    return print("La tarifa a pagar por la distancia de", dist, "metros es", total)

# Exercise 83: Calculadora de envío
# Función que te devuelve la cantidad del primer elemento pedido (10.95) más la cantidad de los siguientes (2.95)
def pedido (cantidad):
    if (cantidad > 1):
        cantidad = cantidad - 1
        total = round(((cantidad * 2.95) + 10.95),2) # La cantidad del primer elemento (10.95) más los elementos restantes
    else:
        total = 10.95
    return print("El total de su pedido es:",total)

# Exercise 84: Mediana de tres valores
def mediana (num1,num2,num3):
    lista = []
    lista.extend([num1,num2,num3]) # añade los tres números del argumento a la lista de golpe
    lista.sort() # ordena los valores en órden ascendente
    resultado = lista[1] # coge el segundo valor de la lista
    return print("La mediana de los tres números es: ", resultado)

# Exercise 85: Convertir un entero en su número ordinal
def ordinal (num):
    ord =""
    if (num>1 and num<12):
        if (num==1):
            ord = "Primero"
        elif (num==2):
            ord = "Segundo"
        elif (num==3):
            ord = "Tercero"
        elif (num==4):
            ord = "Cuarto"
        elif (num==5):
            ord = "Quinto"
        elif (num==6):
            ord = "Sexto"
        elif (num==7):
            ord = "Séptimo"
        elif (num==8):
            ord = "Octavo"
        elif (num==9):
            ord = "Noveno"
        elif (num==10):
            ord = "Décimo"
        elif (num==11):
            ord = "Undécimo"
        elif (num==12):
            ord = "Duodécimo"
    if (num>12):
        ord = "ERROR, tiene que introducir un número del 1 al 12"
    return print("El ordinal es: ", ord)

# Ejercicio 87: Centrar una cadena en la terminal
# Función que centra

ancho = 158 # el ancho de mi terminal lo que se vé sin scroll

def centrar (cadena, ancho):
    if ancho < len(cadena):
        return cadena
    espacios = (ancho - len(cadena)) // 2 # devuelve el númnero de caracteres que hay a cada lado con un número entero //
    resultado = " " * espacios + cadena # pone los espacios requeridos delante de la cadena para centrarla

    return resultado

# Ejercicio 88: ¿Es un triángulo válido?
# Función que dadas la longitudes de tres lados mira si se puede formar un triángulo
def es_triangulo (num1,num2,num3):
    if (num1>num2 and num1>num3): # Se mira el número más grande
        if (num1>num2+num3): # Si el número más grande es mayor que la suma de los otros dos...
            return False # ...NO se podrá formar el triángulo
        else:
            return True  # ... si no hay un lado más grande que la suma de los otros dos SI se podrá formar el triángulo
    elif (num2>num1 and num2>num3):
        if (num2>num1+num3):
            return False
        else:
            return True
    elif (num3>num1 and num3>num2):
        if (num3>num1+num2):
            return False
        else:
            return True

# Ejercicio 89: Pasar a mayúscula
# Función que pasa de minúscula a mayúscula
# una letra si está precedida de un espacio, y un punto o signos de interr. o admiración

def a_mayusculas(frase):
    frase = frase.capitalize() # pone la primera letra de la frase en mayúscula
    pos = 0
    while pos < len(frase) :
        if (frase[pos] == "." or frase[pos] == "!" or frase[pos] == "?"):
            pos = pos + 2
            if (pos < len(frase)):
                frase = frase [0 : pos] + frase[pos].upper() + frase [pos + 1 : len(frase)] #
                    #replace(frase[pos],frase[pos].upper()) # esto reemplaza todos las letras
        pos = pos + 1 # se sale del while aquí
    return print(frase)

# Ejercicio 90: ¿Representa una cadena un número entero?
def es_Entero(cadena):
    cadena = cadena.strip() #borra los caracteres vacíos de principio y final
    if (cadena[0]=="+" or cadena[0]=="-") and cadena[1].isdigit():
        return True
    if cadena.isdigit():
        return True
    return False

# Ejercicio 92: Es un número primo?

def esPrimo (num):
    for i in range(2,num): # tenemos un rango de 2 hasta el número anterior al introducido
        if (num % i == 0): # si en todo el rango hay un módulo que sea igual a 0...
            return False # ... no será primo
    return True # ... si no hay ningún módulo igual a 0 será Primo

# Ejercicio 93: Próximo primo
# Le pasamos por parámetro un número entero y nos dirá el siguiente número primo al pasado por parámetro

def proxPrimo (num):
    x = num + 1 # aumentamos el valor pasado como argumento en uno con nueva variable
    i = 2 # iniciamos variable i a 2 ya que será el divisor
    while (i < num): # mientras el divisor sea menor que el número pasado como argumento...
        resul = x % i # metemos en una variable el resultado de los módulos
        if (resul == 0): # si el módulo es igual a 0 significará que el número no es primo y ...
            x = x + 1 # probaremos con el siguiente número
            i = 2 # el divisor lo reiniciamos a 2
        if (resul != 0): # si el módulo no es igual a 0, puede que sea un número primo y ...
            i = i + 1 # probaremos con otro divisor más grande en una unidad hasta llegar a la cantidad del argumento - 1
    return x

# Ejercicio 94: Contraseña aleatoria
# Función que genera una contraseña aleatoria sin ningún argumento de entrada
import random # si ponemos "from random import randint" no haría falta poner random las veces que se utilice randint

def generaPass():
    x = random.randint(7,10) # Elige la longitud de la contraseña aleatoriamente
    contraseña = "" # Incializamos la contraseña
    #print(x) # Vemos la longitud de la contraseña
    for i in range(x): # Vamos cogiendo un carácter ASCII las veces de la longitud de la cadena
        y = random.randint(33,126) # incializamos la variable "y" que será el índice de un elemento aleatorio de la tabla ASCII
        contraseña = contraseña + chr(y) # vamos metiendo en la contraseña cada elemento ASCII acorde al índice anterior
        # chr --> mira el número pasado como argumento en tabla ASCII
    return contraseña

# Ejercicio 95: Placas de matrícula aleatorias
# Esta función genera números de matrículas de coche de forma aleatoria. Tres números y tres letras o cuatro números y tres letras.

def generaMatricula():
    matrícula = ""
    x = random.randint(6,7) # Elige matrícula al azar de 6 dígitos o 7
    if (x == 6): # Va generar matrícula de 6 dígitos, 3 números y 3 letras
        for i in range(3):
            y = random.randint(48,57) # Va a elegir tres números
            matrícula = matrícula + chr(y)
        matrícula = matrícula + "-"
        for j in range(3):
            z = random.randint(65,90) # va a elegir tres letras
            matrícula = matrícula + chr(z)
    elif (x == 7): # Va a generar matrícula de 7 dígitos, 4 números y 3 letras
        for i in range(4):
            y = random.randint(48,57) # Va a elegir cuatro números
            matrícula = matrícula + chr(y)
        matrícula = matrícula + "-"
        for j in range(3):
            z = random.randint(65,90) # va a elegir tres letras
            matrícula = matrícula + chr(z)
    return print(matrícula)

# Ejercicio 96: Comprobar una contraseña

def chequeoPass(contraseña):
    if ((len(contraseña)==8) # Si la longitud de la contraseña es 8...
            and (any(chr.isdigit() for chr in contraseña)) # ... y contiene al menos un dígito...
            and (any(chr.isupper() for chr in contraseña)) # ...contiene al menos una letra mayúscula...
            and (any(chr.islower() for chr in contraseña))): # ...y contiene al menos una letra minúscula entonces...
        return True # ...la contraseña será válida
    else: # si no...
        return False # ...la contraseña NO será válida

# Ejercicio 97: Contraseña buena aleatoria
# Elegir aleatoriamente una contraseña hasta que sea buena (al menos una minúscula, una mayúscula, un número y de ocho dígitos)
# y después mostrar los intentos hasta haberla conseguido
def buenaPass():
    contraseña = generaPass()
    contador = 0
    while (chequeoPass(contraseña) != True):
        contraseña = generaPass()
        print(contraseña)
        contador += 1
    return print("La contraseña es:", contraseña, "y los intentos han sido:", contador)

# Ejercicio 98: Dígitos hexadecimales y decimales
def int2hex(num): # de decimal a hexadecimal
    resultado = ""
    cociente = num
    while (cociente > 16):
        modulo = cociente % 16
        cociente = cociente // 16
        if (modulo == 10):
            resultado = "A" + resultado
        elif (modulo == 11):
            resultado = "B" + resultado
        elif (modulo == 12):
            resultado = "C" + resultado
        elif (modulo == 13):
            resultado = "D" + resultado
        elif (modulo == 14):
            resultado = "E" + resultado
        elif (modulo == 15):
            resultado = "F" + resultado
        else:
            resultado = str(modulo) + resultado
    if (cociente == 10):
        resultado = "A" + resultado
    elif (cociente == 11):
        resultado = "B" + resultado
    elif (cociente == 12):
        resultado = "C" + resultado
    elif (cociente == 13):
        resultado = "D" + resultado
    elif (cociente== 14):
        resultado = "E" + resultado
    elif (cociente == 15):
        resultado = "F" + resultado
    else:
        resultado = str(cociente) + resultado
    return print(resultado)

def hex2int(cadena): # de hexadecimal a decimal
    reverso = ""
    resultado = 0
    for i in cadena: # le damos la vuelta a la cadena
        reverso = i + reverso
    for i in range(len(reverso)): # obtenemos los indices de la longitud de la cadena dada la vuelta
        char = reverso[i] # obtenemos cada caracter de la cadena dada la vuelta
        if (char == "A" or char == "a"):
            resultado = resultado + (10 * (16**i)) # 10 * (16 elevado al indice i de ese elemento char)
        elif (char == "B" or char == "b"):
            resultado = resultado + (11 * (16**i))
        elif (char == "C" or char == "c"):
            resultado = resultado + (12 * (16**i))
        elif (char == "D" or char == "d"):
            resultado = resultado + (13 * (16**i))
        elif (char == "E" or char== "e"):
            resultado = resultado + (14 * (16**i))
        elif (char == "F" or char =="f"):
            resultado = resultado + (15 * (16**i))
        elif (char.isdigit()):
            resultado = resultado + (int(char) * (16**i))
        else:
            return print ("ERROR, NO HA METIDO UN NÚMERO HEXADECIMAL CORRECTO")
    return print(resultado)

# Ejercicio 99: Conversiones base arbitrarias
# igual que ejercicio 77 y 78 pero en lugar de trabajr con el 2 de binario se trabaja con el número que se pase por argumento

# Ejercicio 100: Días en un mes

def diasEnMes(mes,año):
    resultado = 0
    if (mes in range(1,13) and año in range(1900,2101)): # hay que poner un número más en los rangos
        # ya que no coge el segundo argumento
        if ((año % 4 != 0) or (año % 4 == 0 and año % 100 == 0 and año % 400 != 0)):
            # no divisible entre 4 será año normal de 365 días
            # o divisible entre 4 y 100 y no entre 400 también será año normal
            if (mes==1 or mes==3 or mes==5 or mes==7 or mes==9 or mes==11):
                resultado = 31
            elif(mes==2):
                resultado = 28
            else:
                resultado = 30
            return print("Los días del mes del año NO bisiesto",año,"serán", resultado)

        if ((año % 4 == 0 and año % 100 != 0) or (año % 4 == 0 and año % 100 == 0 and año % 400 == 0)):
            # divisible entre 4 y no entre 100
            # o divisible entre 4, 100 y 400
            if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 9 or mes == 11):
                resultado = 31
            elif (mes == 2):
                resultado = 29
            else:
                resultado = 30
            return print("Los días del mes del año bisiesto", año, "serán", resultado)

    else:
        return print("Hay un error en la fecha que introduciste")

# Ejercicio 102: Reducir medidas
# 1 taza equivale a 16 cucharadas
# 1 cucharada equivale a 3 cucharaditas
# el argumento medida solo recibirá cucharadas o cucharaditas

def reducMedida(num,medida):
    taza = 0
    cucharada = 0
    cucharadita = 0
    medida = medida.lower() # paso el argumento a minúsculas en el caso de que se haya puesto en mayúsculas
    if (medida == "cucharadas"):
        taza = num // 16
        cucharada = num % 16
        return print(taza,"taza/s",cucharada, "cucharada/s")
    elif (medida == "cucharaditas"): # si es cucharadita
        taza = num // 16
        aux = num % 16
        cucharada = aux // 3
        cucharadita = aux % 3
        return print(taza,"taza/s",cucharada, "cucharada/s", cucharadita, "cucharadita/s")

# Ejercicio 103: Fechas mágicas
# Una fecha es mágica si el día por el número de mes introducido es igual a los dos últimos dígitos del año

def fechaMagica(dia, mes, año):
    aux = 0
    mes = mes.lower()
    if(año in range(1900,2000)):
        if(mes=="enero"):
            aux = 1
        elif(mes=="febrero"):
            aux = 2
        elif (mes == "marzo"):
            aux = 3
        elif (mes == "abril"):
            aux = 4
        elif (mes == "mayo"):
            aux = 5
        elif (mes == "junio"):
            aux = 6
        elif (mes == "julio"):
            aux = 7
        elif (mes == "agosto"):
            aux = 8
        elif (mes == "septiembre"):
            aux = 9
        elif (mes == "octubre"):
            aux = 10
        elif (mes == "noviembre"):
            aux = 11
        elif (mes == "diciembre"):
            aux = 12
        año = año - 1900
        if (dia*aux==año):
            return print("La fecha introducida es MÁGICA")
        else:
            return print("La fecha introducida No es mágica")
    else:
        return print("Ha metido mal el año, solo se admiten años del siglo XX")


# EJERCICIOS DE LISTAS
# Ejercicio 104: Orden clasificado (de menor a mayor)

lista = []
num = int(input("Dame un entero "))

while (num!=0):
    lista.append(num)
    num = int(input("Dame un entero "))
lista.sort() # pone la lista de menor a mayor
print(lista)



# Ejercicio 105: Orden inverso (de mayor a menor)

lista = []
num = int(input("Dame un entero "))

while (num!=0):
    lista.append(num)
    num = int(input("Dame un entero "))
lista.sort(reverse=True) # pone la lista de mayor a menor
print(lista)


# NOTA: FUNCION LAMBDA PARA AHORRAR ESCRIBIR(sin "return" y sin "def") SI LA FUNCION SOLO TIENE UNA LINEA
# también puede llamar a otras funciones
mult_div = lambda x, y, z : (x * y) / z
print(mult_div(7,8,4))


# Ejercicio 106: eliminar valores atípicos

lista = []
eliminados = []

for i in range (4): # nos aseguramos de que pida al menos cuatro números
    num = int(input("Dame un entero "))
    lista.append(num)

num = int(input("Dame un entero "))# este es el quinto número

while (num!=0):
        lista.append(num)
        num = int(input("Dame un entero "))

lista.sort() # pone la lista de mayor a menor
print("La lista de numeros introducida y ordenada: ", lista)
# meteremos en la lista "eliminados" los dos primeros y dos últimos de "lista"
eliminados.append(lista.pop(0))# añadimos y eliminamos a la vez
eliminados.append(lista.pop(0))
eliminados.append(lista.pop())
eliminados.append(lista.pop())

print("La lista de numeros sin los dos primeros y los dos últimos es: ",lista)
print("La lista de numeros eliminados son: ", eliminados)



# Ejercicio 107: Evitar duplicados

lista = []
palabra =input ("Dame una palabra: ")
lista.append(palabra)
while (palabra !=""):
    if palabra not in lista: # mira si una palabra esta en la lista o no (CON NOT IN)
        lista.append(palabra) # si no está la añadimos

    palabra = input("Dame una palabra: ")

print(lista)

# EJERCICIOs DE CODE WARS 
# Ejercicio que pide un número por parámetro y lo devuelve al revés y en una lista 
def digitize(n):
    cadena = str(n)
    resultado = []
    for i in cadena:
        y = int(i)
        resultado.insert(0, y)
    return print(resultado)

#digitize(678)


# Ejercicio que dado un array desordenado devuelva la suma de los dos números más bajos
#numbers = [3,7,1,7,9,4,2]
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    resultado = numbers[0]+numbers[1]
    return print(resultado)

sum_two_smallest_numbers([323,7,867,7,9,49,20])

# Ejercicio 108: (INVENTADO) Ingresar unos números, incluídos negativos, y dar la lista colocada
def ordenar_numeros():
    lista = []
    numero = input("Dame un número (puede ser positivo o negativo): ")
    while (numero !=""):
        lista.append(int(numero))
        #print(lista)
        numero = input("Dame un número (puede ser positivo o negativo): ")
    lista.sort()
    return lista

print(ordenar_numeros())


# Ejercicio 108: (VERDADERO QUE PIDE EL LIBRO) NEGATIVOS, ZEROS Y POSITIVOS

def agrupar_nums ():
    negativos = []
    ceros = []
    positivos = []
    numero = input("Dame un número (puede ser positivo, negativo o el cero): ")
    while (numero != ""):
        num = int(numero) # IMPORTANTE: se hace casting porque el while trabaja con strings y para comparar y añadir con enteros
        if (num < 0):
            negativos.append(num)
        elif (num == 0):
            ceros.append(num)
        elif (num > 0):
            positivos.append(num)
        numero = input("Dame un número (puede ser positivo, negativo o el cero): ")
    resultado = negativos + ceros + positivos
    print(resultado)


# Ejercicio 109: Lista de Divisores Propios

def listaDivisores(numero):
    lista = []
    for i in range(1, numero):
        if(numero%i == 0):
            lista.append(i)
    return lista

print (listaDivisores(8))


# Ejercicio 110 (A): Números perfectos->cuando, la suma de la lista (del caso anterior) de los divisores enteros es igual al número solicitado
# NOTA: podría haber llamado a la función anterior, pero lo quiser hacer así
def perfectNumbers(numero):
    resultado = 0
    for i in range(1, numero):
        if (numero % i == 0):
            resultado = resultado + i
    #print(numero)
    #print (resultado)

    if(resultado==numero):
        return True
    else:
        return False

print(perfectNumbers(8128))

# Ejercicio 110 (B): Números perfectos-> igual que el anterior pero que muestre los que están en los primeros 10000 números
# El resultado es [6, 28, 496, 8128]

def perfectNumbers2():
    lista_perfectos = []
    for i in range(1,10000):
        if(perfectNumbers(i)==True):
            lista_perfectos.append(i)
    return lista_perfectos

print(perfectNumbers2())


# Ejercicio 111: Sólo lasPalabras -> con librerías
import string
#import re
def soloPalabras(texto):
    # lista_palabras = re.sub(r'[^\w\s]', '', texto) # quitamos los signos de puntuación -> otra forma de hacerlo con import re
    lista_palabras = texto.translate(str.maketrans("", "", string.punctuation)) # quitamos los signos de puntuación
    return lista_palabras.split() # metemos en una lista las palabras de la frase
print(soloPalabras("Buenos dias!!!, cómo está usted?"))



# Ejercicio 111: Sólo lasPalabras -> sin librerías
def soloPalabras(frase):
    # se inicializa la lista vacía
    palabras = []
    palabra = ""
    # se recorre cada caracter de la frase
    for caracter in frase:
        # si el caracter es un espacio en blanco o un signo de puntuación
        if caracter == " " or caracter in ".,!?¿¡": # también se puede poner-> if caracter in [' ', '.', ',' , ';' , ':' , '!' , '?' , '-' , '¿', '!']:
            # se une la palabra formada hasta ahora a la lista
            palabras.append(palabra)
            if palabra =="":
                palabras.pop()
            # se reinicia la variable palabra
            palabra = ""
        else:
            # si el caracter no es un espacio o signo de puntuación se añade la letra a la palabra
            palabra += caracter
    return palabras
    # se imprime la lista de palabras
print(soloPalabras("Hola, ¿cómo estás? Estoy bien, ¡gracias!"))


# Ejercicio 112: Por encima y por debajo del promedio

def menos_Promedio_mas():
    suma = 0
    lista = []
    menores = []
    mayores = []
    num = input("Dame un entero: ")
    while (num != ""):
        lista.append(int(num))
        numero = int(num)
        suma +=numero
        num = input("Dame un entero: ")
    promedio = suma / len(lista)
    for i in lista:
        if i<promedio:
            menores.append(i)
        else:
            mayores.append(i)
    print("El promedio es: ", promedio)
    print("Los menores al promedio son: ", sorted(menores))
    print("Los mayores al promedio son: ", sorted(mayores))


menos_Promedio_mas()



# Ejercicio 113: Dar formato a una lista

def formatoLista():
    frutas = []
    fruta = input("Dame una fruta: ")
    while (fruta!= ""):
        frutas.append(fruta)
        fruta = input("Dame una fruta: ")
    resultado = ""
    for i in range(len(frutas)):
        resultado += frutas[i]
        if i < len(frutas) - 1 and len(frutas) - 1 - i != 1: # si el índice es menos que la longitud de la lista y además no es el penúltimo elemento...
            resultado += ", "
        if i < len(frutas) - 1 and len(frutas) - 1 - i == 1: # también len(frutas) - i == 2
            resultado += " and "
    print (resultado)

formatoLista()

# Ejercicio 114: Números de lotería aleatorios

import random

def loteriaAleatoria():
    numeros = []
    while len(numeros) != 6:
        numero = random.randint(1,49)
        print(numero)
        if numero not in numeros:
            numeros.append(numero)
    print (sorted(numeros))

loteriaAleatoria()

# Ejercicio 114 de chatGPT

import random

def random_numbers():
    numbers = random.sample(range(1, 50), 6)
    return sorted(numbers)

print(random_numbers())


# Ejercicio 115: Pig Latin

def pigLatin(palabra):
    for i in range(len(palabra)):
        if i == 0 and palabra[i] in "aeiouAEIOU":
            print(palabra + "way")
            break # también sirve return para salir del bucle
        if i != 0 and palabra[i] in "aeiouAEIOU":
            print(palabra[i:] + palabra[:i] + "ay") # palabra a partir de la vocal incluída + lo anterior a la vocal + ay
            break # también sirve return para salir del bucle

pigLatin("Ice")


# Ejercicio 117: Línea de Mejor Ajuste

def ecuacionRecta():
    puntos = []
    sumatorio_xy = 0
    sumatorio_x = 0
    sumatorio_y = 0
    x_cuadrado_sumatorio = 0
    sumatorio_x_cuadrado = 0
    promedio_x = 0
    promedio_y = 0
    while True:
        x = input("Introduce la coordenada x: ")
        if x == "":
            break
        else:
            x = float(x)
        y = float(input("Introduce la coordenada y: "))
        punto = (x,y)
        puntos.append(punto)
    n = len(puntos)
    print (n)
    for x,y in puntos:
        sumatorio_xy += x*y
        sumatorio_x += x
        sumatorio_y += y
        x_cuadrado_sumatorio += x**2
        sumatorio_x_cuadrado = (sumatorio_x)**2
        promedio_x = sumatorio_x / n
        promedio_y = sumatorio_y / n

    m = (sumatorio_xy - (((sumatorio_x)*(sumatorio_y))/n)) / (x_cuadrado_sumatorio - ((sumatorio_x_cuadrado)/n))
    b = (promedio_y - (m*promedio_x))
    return print ("El resultado es: "+"y = " +str(round(m,2))+"x + "+str(round(b,2)))

ecuacionRecta()


# Ejercicio 120: ¿Está una lista ordenada?

def lista_ordenada_si_o_no():
    lista = []
    numero = input("Deme un número: ")
    i = 0
    while (numero != ""):
        lista.append(int(numero))
        numero = input("Deme un número: ")
    print (lista)
    if len(lista) == 0:
        return False
    elif len(lista) == 1:
        return True
    else:
        if lista[i] <= lista[i + 1]:
            i += 1
            while i != len(lista) - 1:
                if (lista[i] <= lista[i + 1]):
                    i += 1
                else:
                    return False
            return True
        if (lista[i] >= lista[i + 1]):
            i += 1
            while i != len(lista) - 1:
                if (lista[i] >= lista[i + 1]):
                    i += 1
                else:
                    return False
            return True

print(lista_ordenada_si_o_no())


# Ejercicio 122: tokenización de una cadena. (ES EL MÍO: DA FALLO: "rango del string fuera de índice", PERO FUNCIONA)

def tokenizarFormula(cadena):
    #cadena = cadena.split(" ")
    lista = []
    i = 0
    numero = ""
    print(len(cadena))
    while i < len(cadena): # 0 <= í < len(cadena):
        if i >= len(cadena):
            break
        if cadena[i] == " ":
            i += 1
        if cadena[i] in "()*/":
            lista.append(cadena[i])
            i += 1
        if cadena[i] in "+-":
            numero = cadena[i]
            i += 1
            if cadena[i] == " ":
                i -= 1
                lista.append(cadena[i])
                i += 1
                numero = ""
            if cadena[i] in "123456789":
                numero += cadena[i]
                i += 1
            if cadena[i] in "()*/":
                i -= 1
                lista.append(cadena[i])
                i += 1
                numero = ""
        if cadena[i] in "123456789":
            numero += cadena[i]
            i += 1
            while cadena[i] != " " and cadena[i] not in "+-/*()":
                numero += cadena[i]
                i += 1
            lista.append(numero)
            numero = ""
    return lista

print(tokenizarFormula("6 - 867 * ( 740 + 562 )"))



# Ejercicio 122: tokenización de una cadena. POR ChatGPT, funciona y sin fallo mejorando el mío anterior por los "break" introducidos

def tokenizarFormula2(cadena):
    lista = []
    i = 0
    numero = ""
    while i < len(cadena):
        if i >= len(cadena):
            break
        if cadena[i] == " ":
            i += 1
        if i >= len(cadena):
            break
        if cadena[i] in "()*/":
            lista.append(cadena[i])
            i += 1
        if i >= len(cadena):
            break
        if cadena[i] in "+-":
            numero = cadena[i]
            i += 1
            if i >= len(cadena):
                break
            if cadena[i] == " ":
                i -= 1
                lista.append(cadena[i])
                i += 1
                numero = ""
            if i >= len(cadena):
                break
            if cadena[i] in "123456789":
                numero += cadena[i]
                i += 1
            if i >= len(cadena):
                break
            if cadena[i] in "()*/":
                i -= 1
                lista.append(cadena[i])
                i += 1
                numero = ""
        if i >= len(cadena):
            break
        if cadena[i] in "123456789":
            numero += cadena[i]
            i += 1
            while i < len(cadena) and cadena[i] != " " and cadena[i] not in "+-/*()":
                numero += cadena[i]
                i += 1
            lista.append(numero)
            numero = ""
    return lista

print(tokenizarFormula2("6 - 867 * ( 740 +562 )"))


# Ejercicio 125: ¿Contiene una Lista una Sublista?

def is_sublist(list1, list2):
    for i in range(len(list2) - len(list1) + 1): # range habla de elementos
        print((len(list2) - len(list1) + 1))
        if list1 == list2[i:i+len(list1)]:  # list2[indice x : al elemento de la lista x + i]
            print(list2[i:i+len(list1)])
            return True
        print(list2[i:i + len(list1)])
    return False

list1 = [5, 6, 8]
list2 = [1, 2, 4, 5, 6, 8, 7]
if is_sublist(list1, list2):
    print("La lista 1 es una sublista de la lista 2")
else:
    print("La lista 1 no es una sublista de la lista 2")


"""

# Ejercicio 127: Criba de Eratóstenes. (Es mejor que algoritmo cuadrático pero tacha un número varias veces).
def eratostenes_criba(n):
    primes = [True] * (n+1)
    p = 2
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n+1, p): # 3 argumentos en el for: (desde índice, hasta el n + 1, de p en p)
                primes[i] = False
                print(i)
                print(primes)
        p += 1

    result = []
    for p in range(2, n+1):
        if primes[p]:
            result.append(p)
        else:
            result.append(0)
    return result

n = 20
print("Los números primos y los que no son primos menores que", n, "son:")
print(eratostenes_criba(n))
"""
# Ejercicio 127: Criba de Aristótenes.
# Este algoritmo es sacado de Youtube: Rubén Hidalgo Carrillo
def cribaEratostenes(n):
    lista = [True] * n # range habla de cantidad de elementos
    p = 2
    while p < len(lista):
        if lista[p] == True:
            print(p, " ", end="")
            j = p * 2
            while j < len(lista):
                lista[j] = False
                j += p
        p += 1
cribaEratostenes(40)
"""



















































































































