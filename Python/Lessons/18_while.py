guess = 0
tries = 0

while tries != 5 and guess != 6:
    guess = int(input("Adivina el numero: "))
    tries = tries + 1
 
if guess != 6:
    print('Te has quedado sin intentos')
else:
    print('Lo tienes!')
