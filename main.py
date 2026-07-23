from core.ai import AI
from memory.database import create_database

create_database()



nova = AI()

print("=" * 40)
print("      Nova - Compañera Virtual")
print("=" * 40)

while True:

    mensaje = input("\nTú: ")

    if mensaje.lower() in ["salir", "exit"]:
        break

    respuesta = nova.process_user_message(mensaje)

    print(f"\nNova: {respuesta}")

