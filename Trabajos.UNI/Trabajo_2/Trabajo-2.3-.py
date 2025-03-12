def corregir_articulo():
    #Corrige un artículo reemplazando una frase y dividiéndolo en oraciones.
    articulo = input("Ingrese el artículo a corregir: ").strip().lower()  # Elimina espacios extra y convierte a minúsculas

    articulo = articulo.replace("tecnología antigua", "tecnología de punta") 
    oraciones = articulo.split(".")  # Divide el artículo

    print("📝 Artículo corregido:")
    for oracion in oraciones:
        if oracion.strip():  # Evitar imprimir líneas vacías
            print(f"➡️ {oracion.strip()}.")

corregir_articulo()