contacto=(

"nombre: Juan",
"apellido: Perez",
"telefono: 123456789",
"edad: 30",
"ciudad: Buenos Aires",

)
print(contacto)
print(contacto[0])  # nombre: Juan
print(contacto[-1]) # ciudad: Buenos Aires 
x,y=contacto[0],contacto[-1]
print(x,y) # nombre: Juan ciudad: Buenos Aires


print(contacto.get("nombre","clave no validad"))
contacto["telefono"]="987654321"


print(contacto)


del contacto["edad"]
contacto.pop("ciudad")
print(contacto)