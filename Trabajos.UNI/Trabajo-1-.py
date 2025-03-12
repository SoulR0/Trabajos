# Diccionario para almacenar la biblioteca
biblioteca = {}

# Funciones de validación
def validar_isbn(isbn):
    """Verifica si el ISBN tiene 10 o 13 dígitos numéricos."""
    return len(isbn) in [10, 13] and isbn.isdigit()

def validar_calificacion(calificacion):
    """Verifica que la calificación sea un número entre 0 y 10."""
    try:
        calificacion = float(calificacion)
        return 0 <= calificacion <= 10
    except ValueError:
        return False

# Función para agregar un libro
def agregar_libro():
    """Permite al usuario agregar un libro con validaciones."""
    isbn = input("Ingrese el ISBN del libro (10 o 13 dígitos): ").strip()
    
    if not validar_isbn(isbn):
        print("❌ ISBN inválido. Debe tener 10 o 13 dígitos numéricos.")
        return

    if isbn in biblioteca:
        print("⚠️ El libro con este ISBN ya está en la biblioteca.")
        return

    titulo = input("Ingrese el título del libro: ").strip()
    autor = input("Ingrese el autor del libro: ").strip()
    anio = input("Ingrese el año de publicación: ").strip()
    genero = input("Ingrese el género del libro: ").strip()

    calificacion = input("Ingrese la calificación (0-10): ").strip()
    if not validar_calificacion(calificacion):
        print("❌ Calificación inválida. Debe ser un número entre 0 y 10.")
        return

    leido = input("¿Lo has leído? (s/n): ").strip().lower() == 's'

    biblioteca[isbn] = {
        "Título": titulo,
        "Autor": autor,
        "Año": anio,
        "Género": genero,
        "Calificación": float(calificacion),
        "Leído": leido
    }
    
    print(f"✅ Libro '{titulo}' agregado correctamente.")

# Función para mostrar todos los libros
def mostrar_libros():
    """Muestra todos los libros almacenados en la biblioteca de forma ordenada."""
    if not biblioteca:
        print("📚 La biblioteca está vacía. Agrega libros primero.")
        return

    print("\n📖 Lista de libros en la biblioteca:")
    print("=" * 50)
    for isbn, datos in biblioteca.items():
        print(f"📌 ISBN: {isbn}")
        print(f"   📕 Título: {datos['Título']}")
        print(f"   ✍️ Autor: {datos['Autor']}")
        print(f"   📅 Año: {datos['Año']}")
        print(f"   📚 Género: {datos['Género']}")
        print(f"   ⭐ Calificación: {datos['Calificación']}/10")
        print(f"   ✅ Leído: {'Sí' if datos['Leído'] else 'No'}")
        print("-" * 50)

# Función para buscar libros
def buscar_libro():
    """Permite buscar un libro por título, autor o ISBN."""
    if not biblioteca:
        print("📚 La biblioteca está vacía. Agrega libros primero.")
        return

    print("\n🔍 Buscar libro por:")
    print("1️⃣ Título")
    print("2️⃣ Autor")
    print("3️⃣ ISBN")
    opcion = input("Elige una opción (1-3): ").strip()

    if opcion == "1":
        criterio = "Título"
    elif opcion == "2":
        criterio = "Autor"
    elif opcion == "3":
        criterio = "ISBN"
    else:
        print("❌ Opción inválida.")
        return

    valor_busqueda = input(f"Ingrese el {criterio} del libro: ").strip().lower()
    encontrados = []

    for isbn, datos in biblioteca.items():
        if (criterio == "ISBN" and isbn == valor_busqueda) or (criterio in datos and valor_busqueda in datos[criterio].lower()):
            encontrados.append((isbn, datos))

    if encontrados:
        print("\n📚 Libros encontrados:")
        print("=" * 50)
        for isbn, datos in encontrados:
            print(f"📌 ISBN: {isbn}")
            print(f"   📕 Título: {datos['Título']}")
            print(f"   ✍️ Autor: {datos['Autor']}")
            print(f"   📅 Año: {datos['Año']}")
            print(f"   📚 Género: {datos['Género']}")
            print(f"   ⭐ Calificación: {datos['Calificación']}/10")
            print(f"   ✅ Leído: {'Sí' if datos['Leído'] else 'No'}")
            print("-" * 50)
    else:
        print("❌ No se encontraron libros con ese criterio.")

# Función para modificar un libro
def modificar_libro():
    """Permite modificar la información de un libro, excepto el ISBN."""
    if not biblioteca:
        print("📚 La biblioteca está vacía. Agrega libros primero.")
        return

    isbn = input("Ingrese el ISBN del libro que desea modificar: ").strip()

    if isbn not in biblioteca:
        print("❌ No se encontró un libro con ese ISBN.")
        return

    print("\n🔄 ¿Qué desea modificar?")
    print("1️⃣ Título")
    print("2️⃣ Autor")
    print("3️⃣ Año de publicación")
    print("4️⃣ Género")
    print("5️⃣ Calificación")
    print("6️⃣ Estado de lectura (Leído/No leído)")
    opcion = input("Elige una opción (1-6): ").strip()

    if opcion == "1":
        biblioteca[isbn]["Título"] = input("Nuevo título: ").strip()
    elif opcion == "2":
        biblioteca[isbn]["Autor"] = input("Nuevo autor: ").strip()
    elif opcion == "3":
        biblioteca[isbn]["Año"] = input("Nuevo año de publicación: ").strip()
    elif opcion == "4":
        biblioteca[isbn]["Género"] = input("Nuevo género: ").strip()
    elif opcion == "5":
        nueva_calificacion = input("Nueva calificación (0-10): ").strip()
        if validar_calificacion(nueva_calificacion):
            biblioteca[isbn]["Calificación"] = float(nueva_calificacion)
        else:
            print("❌ Calificación inválida. No se realizaron cambios.")
            return
    elif opcion == "6":
        leido = input("¿Lo has leído? (s/n): ").strip().lower()
        biblioteca[isbn]["Leído"] = leido == 's'
    else:
        print("❌ Opción inválida.")
        return

    print("✅ Libro modificado exitosamente.")

# Función para eliminar un libro
def eliminar_libro():
    """Permite eliminar un libro de la biblioteca por su ISBN."""
    if not biblioteca:
        print("📚 La biblioteca está vacía. Agrega libros primero.")
        return

    isbn = input("Ingrese el ISBN del libro que desea eliminar: ").strip()

    if isbn not in biblioteca:
        print("❌ No se encontró un libro con ese ISBN.")
        return

    del biblioteca[isbn]
    print("✅ Libro eliminado exitosamente.")

# Menú interactivo
while True:
    print("\n📚 Menú Biblioteca")
    print("1️⃣ Agregar libro")
    print("2️⃣ Mostrar libros")
    print("3️⃣ Buscar libro")
    print("4️⃣ Modificar libro")
    print("5️⃣ Eliminar libro")
    print("6️⃣ Salir")
    
    opcion = input("Elige una opción: ").strip()
    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        mostrar_libros()
    elif opcion == "3":
        buscar_libro()
    elif opcion == "4":
        modificar_libro()
    elif opcion == "5":
        eliminar_libro()
    elif opcion == "6":
        print("👋 ¡Hasta luego!")
        break
    else:
        print("❌ Opción inválida.")
