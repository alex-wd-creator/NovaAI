from tools.base_tool import BaseTool


class CalculatorTool(BaseTool):

    name = "calculator"

    description = (
        "Realiza operaciones matemáticas básicas."
    )

    def execute(self, expression: str):

        try:
            result = eval(expression, {"__builtins__": {}}, {})
            return str(result)

        except Exception:
            return "No pude realizar esa operación."