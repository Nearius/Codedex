#Quiz de preguntas sobre las casas de harry potter

#puntuaciones de inicio:

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0


print('Bienvenido al QUIZ mas atrevido sobre Harry Potter, te atreves a descubrir a que casa perteneces?')


#lanzamos la primera pregunta:
print('Q1) Do you like Dawn or Dusk?')
print('    1) Dawn')
print('    2) Dusk')

#recogemos la respuesta del usuario:
q1answer = int(input('Escribe 1 o 2 para elegir tu respuesta: '))


#Obtenemos la respuesta del usuario y sumamos puntos a la casa elegida:
if q1answer == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif q1answer == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:
    print('Respuesta no valida, no contara para el recuento de puntos')

#print de comprobacion de puntos:
#print(Gryffindor)
#print(Ravenclaw)
#print(Hufflepuff)
#print(Slytherin)

#confirmacion de respuesta elegida
print('Respuesta recibida 😉 continuemos con la siguiente pregunta:')

#Pregunta numero 2:
print('Q2) When I’m dead, I want people to remember me as:')
print('    1) The Good')
print('    2) The Great')
print('    3) The Wise')
print('    4) The Bold')

q2answer = int(input('Escribe 1, 2, 3 o 4 para elegir tu respuesta: '))

if q2answer == 1:
    Hufflepuff = Hufflepuff + 2
elif q2answer == 2:
    Slytherin = Slytherin + 2
elif q2answer == 3:
    Ravenclaw = Ravenclaw + 2
elif q2answer == 4:
    Gryffindor = Gryffindor + 2
else:
    print('Respuesta no valida, no contara para el recuento de puntos')

#confirmacion de respuesta elegida
print('Respuesta recibida 😉 continuemos con la siguiente pregunta:')


#Pregunta numero 3:
print('Q3) Which kind of instrument most pleases your ear?:')
print('    1) The violin')
print('    2) The trumpet')
print('    3) The piano')
print('    4) The drum')

q3answer = int(input('Escribe 1, 2, 3 o 4 para elegir tu respuesta: '))

if q3answer == 1:
    Slytherin = Slytherin + 4
elif q3answer == 2:
    Hufflepuff = Hufflepuff + 4
elif q3answer == 3:
    Ravenclaw = Ravenclaw + 3
elif q3answer == 4:
    Gryffindor = Gryffindor + 4
else:
    print('Respuesta no valida, no contara para el recuento de puntos')

#confirmacion de respuesta elegida
print('Respuesta recibida 😉 continuemos con la siguiente pregunta:')

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and  Gryffindor > Slytherin:
    print('Eres un miembro orgulloso de 🦁 Gryffindor con una puntuacion de', Gryffindor)
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print('Eres mercedor de la casa 🦅 Ravenclaw con una puntuacion de', Ravenclaw)
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print('Eres un miembro apto para la casa 🦡 Hufflepuff con una puntuacion de', Hufflepuff)
elif Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw:
    print('Eres un intrpido mago, pues perteneces a la casa 🐍 Slytherin con una puntuacion de', Slytherin)
else:
    print('ha habido un empate! vuelve a repetir el quiz')

print('Muchas gracias por participar en este QUIZ de codedex 😁')