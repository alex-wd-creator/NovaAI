import json

from core.client import client, MODEL


class ToolDecision:

    SYSTEM_PROMPT = """
Eres el sistema de decisión de herramientas de Nova.

Tu tarea es determinar si el mensaje del usuario requiere utilizar
una herramienta disponible.

Herramientas disponibles:

- calculator: realiza operaciones matemáticas.

Si necesitas una herramienta, responde EXCLUSIVAMENTE con JSON válido:

{
    "use_tool": true,
    "tool": "nombre_de_la_herramienta",
    "arguments": {
        "argumento": "valor"
    }
}

Si NO necesitas una herramienta, responde exactamente:

{
    "use_tool": false
}

No escribas explicaciones.
No escribas Markdown.
No escribas texto fuera del JSON.
"""

    def decide(self, message: str):

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": self.SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        result = response.choices[0].message.content.strip()

        try:
            return json.loads(result)

        except json.JSONDecodeError:
            return {
                "use_tool": False
            }