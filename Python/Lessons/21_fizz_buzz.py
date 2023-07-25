for x in range(100):
    if x % 3 == 0 and  x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("fizz")
    else:
        print(x)