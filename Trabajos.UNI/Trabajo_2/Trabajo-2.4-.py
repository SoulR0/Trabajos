def validar_codigo_producto():
    """Verifica si un código de producto es válido (debe comenzar con 'PRO')."""
    codigo = input("Ingrese el código del producto: ").strip().upper()  # Convertimos a mayúsculas

    if codigo.startswith("PRO"):
        print("✅ Código válido.")
    else:
        print("❌ Código inválido. Debe comenzar con 'PRO'.")

# Prueba la función
validar_codigo_producto()
