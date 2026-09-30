from core.ai import AI
from memory.database import create_database

create_database()


from tools.tool_manager import ToolManager
from tools.base_tool import BaseTool
from tools.calculator_tool import CalculatorTool


# temporal
from core.tool_decision import ToolDecision


decision = ToolDecision()

#--

nova = AI()

print("=" * 40)
print("      Nova - Compañera Virtual")
print("=" * 40)

while True:

    mensaje = input("\nTú: ")

    if mensaje.lower() in ["salir", "exit"]:
        break

    respuesta = nova.process_user_message(mensaje)

    resultado = decision.decide(mensaje)

    print("\n[DEBUG] Decision:")

    print(resultado)

    print(f"\nNova: {respuesta}")

