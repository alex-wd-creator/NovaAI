import json

texto = """
[
    {
        "category":"Nombre",
        "value":"Alex"
    },
    {
        "category":"Juego favorito",
        "value":"Roblox"
    }
]
"""

datos = json.loads(texto)

print(type(datos))
print(type(datos[0]))
print(datos)
print(datos[0]["category"])
print(datos[1]["value"])