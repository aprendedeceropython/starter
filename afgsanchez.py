# Crea una función que sume dos números y devuelva el resultado.
def suma(a, b):
    c = a + b
    return c

a = int(input("Escribe un numero: "))
b = int(input("Escribe otro numero: "))

print("El resultado de la suma es: ", suma(a, b))
print()

# Crea una función que reste dos números y devuelva el resultado.
def resta(d, e):
    f = d - e
    return f

d = int(input("Escribe un numero: "))
e = int(input("Escribe otro numero: "))

print("El resultado de la resta es: ", resta(d, e))
print()

# Crea una función que multiplique dos números y devuelva el resultado.
def multiplicacion(g, h):
    i = g * h
    return i

g = int(input("Escribe un numero: "))
h = int(input("Escribe otro numero: "))

print("El resultado de la multiplicación es: ", multiplicacion(g, h))
print()

# Crea una función que divida dos números y devuelva el resultado.
def division(j, k):
    l = j / k
    return l
j= int(input("Escribe un numero: "))
k = int(input("Escribe otro numero: "))

print("El resultado de la división es: ", division(j, k))
print()

# Crea una función que concatene dos textos y devuelva el resultado.
def concatenar_textos(texto1, texto2):
    texto_c = texto1 + " " + texto2
    return texto_c
texto1 = "hola"
texto2 = "radiola"
print("Texto concatenado: ", concatenar_textos(texto1, texto2))
print()

# Crea una función a tu criterio que no devuelva nada.
def mensaje():
    print("Hello World!")
mensaje()
print()

#  Crea una función que devuelva el módulo de una división de dos números enteros y devuelva el resultado.
# Esto es calcular el residuo de una division.
# Usaremos la misma funcion para calcular el entero que es el siguiente ejercicio.
def division_entero_modulo(numero1, numero2):
    entero = numero1 // numero2
    modulo = numero1 % numero2
    return entero, modulo

num1 = 10
num2 = 3
resultado_entero = division_entero_modulo(num1, num2)[0]
resultado_modulo = division_entero_modulo(num1, num2)[1]
print("El entero de la división de", num1, "entre", num2, "es:", resultado_entero)
print("El módulo de la división de", num1, "entre", num2, "es:", resultado_modulo)
print()

# Crea una función que devuelva el resultado de la potencia de dos de un número y devuelva el resultado.
def potenciacion(numero, potencia):
    result = numero ** potencia
    return result
numero = 5
potencia = 2

num_pot = potenciacion(numero, potencia)
print("El resultado de la potencia de dos de ", numero, "es: ", num_pot)

    


