while True:
    
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    
    mayor = num1
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3

   
    print(f"El numero mayor es: {mayor}")

    
    continuar = input("¿Quieres intentar con otros números? (s/n): ").strip().lower()
    if continuar != "si":
        print("adios")
        break
