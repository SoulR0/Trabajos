import math
#########Luis Miguel Barros Rodriguez
# Lista para almacenar los préstamos
prestamos = []

def calcular_cuota(monto, tasa_anual, plazo):
    """Calcula la cuota mensual de un préstamo usando la fórmula del préstamo."""
    tasa_mensual = (tasa_anual / 100) / 12  # Convertimos tasa a decimal mensual
    if tasa_mensual == 0:
        return round(monto / plazo, 2)  # Evita división por 0 en préstamos sin interés
    cuota = (monto * tasa_mensual) / (1 - (1 + tasa_mensual) ** -plazo)
    return round(cuota, 2)

def solicitar_float(mensaje):
    """Solicita un número flotante válido al usuario."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor <= 0:
                print(" El valor debe ser mayor a 0. Inténtelo de nuevo.")
                continue
            return valor
        except ValueError:
            print(" Entrada no válida. Ingrese un número.")

def solicitar_entero(mensaje):
    """Solicita un número entero válido al usuario."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print(" El valor debe ser mayor a 0. Inténtelo de nuevo.")
                continue
            return valor
        except ValueError:
            print(" Entrada no válida. Ingrese un número entero.")

def registrar_prestamo():
    monto = solicitar_float("Ingrese el monto del préstamo: ")
    tasa = solicitar_float("Ingrese la tasa de interés anual (%): ")
    plazo = solicitar_entero("Ingrese el plazo en meses: ")
    
    cuota = calcular_cuota(monto, tasa, plazo)
    
    prestamo = {
        "Monto solicitado": monto,
        "Tasa de interés": tasa,
        "Plazo en meses": plazo,
        "Cuota mensual": cuota
    }
    
    prestamos.append(prestamo)
    print("\n Préstamo registrado correctamente.")
    print(f"Cuota mensual: ${cuota}\n")

def mostrar_prestamos():
    if not prestamos:
        print(" No hay préstamos registrados aún.")
        return
    print("\n Lista de préstamos:")
    for i, prestamo in enumerate(prestamos, 1):
        print(f"{i}. Monto: ${prestamo['Monto solicitado']}, Tasa: {prestamo['Tasa de interés']}%, Plazo: {prestamo['Plazo en meses']} meses, Cuota: ${prestamo['Cuota mensual']}")

# Menú interactivo
while True:
    print("\n Calculadora de Préstamos ")
    print("1. Registrar nuevo préstamo")
    print("2. Mostrar préstamos registrados")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_prestamo()
    elif opcion == "2":
        mostrar_prestamos()
    elif opcion == "3":
        print(" Saliendo del programa...")
        break
    else:
        print(" Opción no válida, intente de nuevo.")
