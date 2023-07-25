import random


input("tu pregunta: ")

num = random.randint(1,9)


if num == 1:
    print("Magic 8 Ball: Si - definitivamente")
elif num == 2:
    print("Magic 8 Ball: Creo que si")
elif num == 3:
    print("Magic 8 Ball: Sin duda ninguna")
elif num == 4:
    print("Magic 8 Ball: No lo sé, prueba de nuevo")
elif num == 5:
    print("Magic 8 Ball: Pregunta otra vez despues")
elif num == 6:
    print("Magic 8 Ball: Mejor no te lo digo ahora")
elif num == 7:
    print("Magic 8 Ball: Mis fuentes me dicen que no")
elif num == 8:
    print ("Magic 8 Ball: Definitivamente no")
else:
    print("Magic 8 Ball: lo dudo mucho")


#============================================
#Solution: 

import random

question = input()

random_number = random.randint(1, 9)

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4:
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'Ask again later'
elif random_number == 6:
  answer = 'Better not tell you now'
elif random_number == 7:
  answer = 'My sources say no'
elif random_number == 8:
  answer = 'Outlook not so good'
elif random_number == 9:
  answer = 'Very doubtful'
else:
  answer = 'Error'
  
print('Question:      ' + question) 
print('Magic 8 Ball:  ' + answer)