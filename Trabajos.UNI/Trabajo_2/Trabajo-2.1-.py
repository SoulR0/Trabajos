def validar_usuario():
    """Solicita un nombre de usuario y lo valida según las reglas establecidas."""
    nombre = input("Ingrese su nombre de usuario: ").strip()

    if len(nombre) > 3 and len(nombre) < 8:
        print(f"👋 ¡Hola, {nombre.upper()}! Bienvenido a la plataforma.")
    else:
        print("❌ Nombre inválido. Debe tener entre 4 y 7 caracteres.")

validar_usuario()