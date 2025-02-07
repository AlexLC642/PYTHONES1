    def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculadora():
    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '5':
            print("Saliendo de la calculadora...")
            break
        
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                if opcion == '1':
                    print(f"Resultado: {sumar(num1, num2)}")
                elif opcion == '2':
                    print(f"Resultado: {restar(num1, num2)}")
                elif opcion == '3':
                    print(f"Resultado: {multiplicar(num1, num2)}")
                elif opcion == '4':
                    print(f"Resultado: {dividir(num1, num2)}")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    calculadora()
