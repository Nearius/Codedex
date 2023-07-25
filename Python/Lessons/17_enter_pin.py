print('Banco Nealand')

pin = int(input('Introduce tu PIN: '))

while pin != 1234:
    pin = int(input('Pin incorrecto. Introduce tu PIN de nuevo: '))

if pin == 1234:
    print('PIN aceptado!')