def mcd_extendido(a, b):
    if a == 0:
        return b, 0, 1
    mcd, x1, y1 = mcd_extendido(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return mcd, x, y


while True:
    a = int(input("Introduce el numero: "))
    m = int(input("Introduce el modulo: "))

    g, x, y = mcd_extendido(a, m)

    if g != 1:
        print("Error: No existe el inverso (MCD != 1).")
    else:
        inverso = (x % m + m) % m
        print(f"El inverso de {a} mod {m} es: {inverso}")

    opcion = input("\n¿Quieres realizar otra operacion? (s/n): ")
    if opcion.lower() != 's':
        break
