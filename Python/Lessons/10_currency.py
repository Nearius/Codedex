co = int(input("Cuantos pesos tienes? "))
pe = int(input("Cuantos soles tienes? "))
br = int(input("cuantos reais tienes? "))

co_to_USD = co * 0.00025 / 1
pe_to_USD = pe * 0.28 / 1
br_to_USD = br * 0.21 / 1


print(co_to_USD + pe_to_USD + br_to_USD)

