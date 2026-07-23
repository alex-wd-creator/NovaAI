from core.client import client, MODEL
import json


class MemoryExtractor:

    def extract(self, text: str):

        # preparar mensajes
        SYSTEM_PROMPT = """
        Eres un extractor de memoria para una IA.

        Tu única tarea es analizar el mensaje del usuario y extraer
        únicamente la información útil para recordar a largo plazo.

        Extrae únicamente:

        - Nombre
        - Edad
        - Profesión
        - Estudios
        - Gustos
        - Preferencias
        - Objetivos
        - Proyectos
        - Información personal permanente

        NO extraigas:

        - Saludos
        - Conversación casual
        - Pregunemporales
        - Estados de ántas
        - Emociones timo
        - Clima
        - Hora
        - Información pasajera

        Responde EXCLUSIVAMENTE con un JSON válido.

        Formato:

        [
            {
                "category": "Nombre",
                "value": "Alex"
            }
        ]

        Si no hay información relevante responde exactamente:

        []
        """

        messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    },
    {
        "role": "user",
        "content": text
    }
]

        # llamar a la IA
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        # obtener la respuesta
        result = response.choices[0].message.content


        # convertir con json.loads()
        try:
            result = json.loads(result)
        except json.JSONDecodeError:
            result = []

        # devolver el resultado
        return result