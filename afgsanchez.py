# Declaración de variables.

# variables tipo integer (enteros)
entero = 5
entero1 = 6

# variable tipo float (flotantes, numeros con decimal)
flotante = 3.14
flotante1 = 1.26

# variable tipo string (cadenas de texto)
texto = "Me llamo Toni."
texto2 = "Encantado de conoceros"

# variable tipo booleano (True o False)
boleano = True

# variables tipo listas (Almacenan un serie de elementos)
lista_enteros = [1, 2, 3, 4]
lista_texto = ['uno', 'dos', 'tres', 'cuatro']

# variables tipo tupla (son listas inmutables, que
# no se puede cambiar el contenido)
tupla = (1, 2, 3, 4)

# variables tipo diccionario (listas que almacenan
# pares)
diccionario = {"Nombre": "Toni", "Localidad": "Baleares"}

# variables tipo set (almacenan colecciones de datos
# no ordenados y no repetidos)
variable_set = {"rojo", "azul", "amarillo", "verde"}

#------------------------------#
# Ejercicios con las variables #
#------------------------------#

# Concatena variables de tipo texto.
print(texto, texto2)
print()

# Haz las diferentes operaciones con variable numéricas (Suma, Resta, Multiplicación, División, Residuo, Potenciación).
# Suma enteros
print(entero + entero1, " - Suma de integer")
# Suma entero + flotante
f = entero + flotante1
print(f, " - Suma de integer + float")
# Resta
print(entero - entero1, " - Resta de integer")
# Multiplicación
print(entero * flotante, " - Multiplicacion entre enteros y flotantes")
# Division
print(entero / flotante, " - División entre entero y flotante")
#Residuo
print(entero1 % entero, " - Residuo de dividir entero1 entre entero")
# Potenciación
print(entero ** entero1, " - ejemplo de potenciación, en este caso entero elevado a entero1")
print()

# Cambia el valor de una variable booleana.
print("El valor de la variable boleano es: ", boleano)
respuesta = input("Quieres cambiar el valor? yes/no: ")
if respuesta == "yes":
    boleano = False
elif respuesta == "no":
    print("No cambio en valor")
else:
    print("Debes elegir yes/no")
    exit()
print("El valor de la variable boleano es: ", boleano)
print()

# Suma una variable de texto con una variable numérica.
variable_numerica = 4
variable_texto = "2"
# convierto la variable_texto a una variable numerica
variable_texto = int(variable_texto)
# Hago la suma
suma = variable_numerica + variable_texto
print(suma)









