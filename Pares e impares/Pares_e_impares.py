Impares = 0
Pares = 0
for i in range(5):
    x = int(input("Digite un número: "))
    if x % 2 == 0:
        Pares = Pares + 1
    else:
        Impares = Impares + 1

# Output
print("\nCantidad de números pares: "+str(Pares))
print("Cantidad de números impares: "+str(Impares))
print(" ")
