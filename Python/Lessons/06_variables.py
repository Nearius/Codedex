#En el paso 6 he aprendido los tipos de variables diferentes:


# Int o Integer son los numeros enteros Ejemplo:   Año = 2023  / Edad = 30    Las variables Año y Edad están almacenando numeros enteros.
# Float serían los numeros decimales.  Ejemplo   Fiebre = 38.9      La variable Fiebre me indica un numero con decimales.
# String son textos,   Ejemplo:   Mensaje = "Buenas noches"  usuario = "nea.es"  Variable Mensaje y Usuario almacenan textos, incluidos espacios.
# Bolean, respuestas de Verdadero o Falso,  True - False   Sexy = False      Borracho = True

#Operadores: 

score = 0           # score is 0
score = 4 + 3       # score is now 7
score = 4 - 3       # score is now 1
score = 4 * 3       # score is now 12
score = 4 / 3       # score is now 1.3333
score = 4 % 3       # score is now 1

print(score)        # Output: 1   ///  Recordatorio, se usa el ultimo variable declarado, en este caso  score = 4 % 3


#Ejercicio basico, Calculadora total

pizza = 20.00
iva = 0.10

totalpizza = pizza * iva + pizza

print('Total Pizza Iva incluido:')
print( pizza * iva + pizza)
print(totalpizza)


# Exponents
# Python can also perform exponentiation such as 2³ or 10².

# In written math, we might see an exponent as a superscript number (like above), but typing superscript numbers isn't always easy on modern keyboards. Since exponentiation is super similar to multiplication, Python uses the notation **.

score = 2 ** 2      # score is 4
score = 2 ** 3      # score is now 8
score = 2 ** 4      # score is now 16
score = 2 ** 5      # score is now 32

print(score)        # Output: 32



# Relational Operators
#A lot of the times inside conditions, we are comparing two values. To do so, we need to use a different type of operators called relational operators that compares values:

#== equal to
#!= not equal to
#> greater than
#< less than
#>= greater than or equal to
#<= less than or equal to