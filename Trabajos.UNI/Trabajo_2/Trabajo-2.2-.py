def analizar_comentario():
    """Analiza un comentario de cliente, eliminando espacios y contando la palabra 'excelente'."""
    comentario = input("Ingrese el comentario del cliente: ").strip()  # Elimina espacios extra
    comentario = comentario.lower()  # Convierte a minúsculas
    cantidad = comentario.count("excelente")  # Cuenta las ocurrencias de "excelente"

    print(f"📝 Comentario limpio: {comentario}")
    print(f"🔍 La palabra 'excelente' aparece {cantidad} veces.")

analizar_comentario()