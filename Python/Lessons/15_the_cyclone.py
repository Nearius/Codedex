#Obtengo información del ususario, tanto su altura (height) como sus creditos:

height  = int(input('Introduce tu altura actual: '))
creditos = int(input('Cuantos creditos tienes: '))

#Establezco la altura minima y los creditos minimos para poder participar:

minHeight = 137
mincredits = 10

if height >= minHeight and creditos >= mincredits:
    print('disfruta la vuelta')
elif height < minHeight and creditos > mincredits:
    print('No eres lo suficientemente alto')
elif height > minHeight and creditos < mincredits:
    print('no tienes suficientes creditos')
else: 
    print('No eres lo suficientemente alto ni tienes creditos.')




