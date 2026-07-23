# 🤖 NovaAI

NovaAI es una compañera virtual desarrollada completamente en Python que se ejecuta de forma local utilizando modelos de lenguaje (LLMs) a través de LM Studio.

El objetivo del proyecto es crear una IA capaz de conversar de forma natural, recordar información importante del usuario y evolucionar progresivamente hasta convertirse en una verdadera compañera virtual para el día a día y los videojuegos.

---

# ✨ Características actuales (v0.1.0)

- 💬 Conversación local mediante LM Studio.
- 🧠 Memoria persistente utilizando SQLite.
- 📌 Extracción automática de información relevante mediante IA.
- 🗂️ Gestión inteligente de recuerdos mediante categorías.
- 🔄 Categorías únicas (se reemplazan automáticamente).
- ➕ Categorías múltiples (se agregan nuevos recuerdos).
- 🏗️ Arquitectura modular y fácil de ampliar.

---

# 📂 Estructura del proyecto

```
NovaAI/
│
├── core/
│   ├── ai.py
│   ├── client.py
│   └── memory_extractor.py
│
├── memory/
│   ├── database.py
│   ├── memory.py
│   └── rules.py
│
├── data/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

---

# 🚀 Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/NovaAI.git

cd NovaAI
```

---

## 2. Crear un entorno virtual

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Configurar LM Studio

Inicia LM Studio y:

- Carga un modelo compatible.
- Activa el servidor local (OpenAI Compatible API).

---

## 5. Crear el archivo `.env`

Copia el archivo `.env.example` y renómbralo como:

```
.env
```

Ejemplo:

```env
BASE_URL=http://localhost:1234/v1
API_KEY=lm-studio
MODEL=qwen3-vl-8b-instruct
```

---

## 6. Ejecutar Nova

```bash
python main.py
```

---

# 🧠 Sistema de memoria

Nova utiliza una memoria persistente basada en SQLite.

La IA analiza automáticamente los mensajes del usuario y extrae únicamente la información útil para recordar a largo plazo.

Ejemplo:

```
Usuario:
Me llamo Alex.

↓

Nombre = Alex
```

La siguiente vez que Nova se inicie seguirá recordando esa información.

---

# 📚 Categorías de memoria

Actualmente Nova distingue entre categorías únicas y múltiples.

## Categorías únicas

Solo puede existir un valor.

Ejemplos:

- Nombre
- Edad
- Profesión
- Estudios

Si el usuario cambia alguno de estos datos, Nova reemplaza automáticamente el valor anterior.

---

## Categorías múltiples

Permiten almacenar varios recuerdos.

Ejemplos:

- Gustos
- Preferencias
- Proyectos
- Objetivos

---

# 🛠️ Tecnologías utilizadas

- Python 3.13
- SQLite
- OpenAI Python SDK
- LM Studio
- Modelos de lenguaje locales (Qwen3-VL)
- python-dotenv
- Git
- GitHub

---

# 📅 Roadmap

## v0.1.0

- ✅ Chat local
- ✅ Memoria persistente
- ✅ Extracción automática de recuerdos
- ✅ Reglas de memoria

## v0.2.0

- 🔄 Evitar recuerdos duplicados
- 🔍 Búsqueda inteligente de recuerdos
- 🧠 Mejoras en el contexto de memoria

## v0.3.0

- 😊 Personalidad configurable
- ❤️ Sistema de emociones
- 🗣️ Estilo de conversación personalizable

## v0.4.0

- 🎤 Reconocimiento de voz
- 🔊 Síntesis de voz

## v0.5.0

- 🎮 Asistente para videojuegos
- 💡 Consejos durante las partidas
- 📊 Memoria específica para juegos

---

# 🤝 Contribuciones

Actualmente este proyecto está en desarrollo y aún no acepta contribuciones externas.

Sin embargo, cualquier sugerencia o reporte de errores es bienvenido.

---

# 📄 Licencia

Este proyecto está distribuido bajo la licencia MIT.

Consulta el archivo LICENSE para más información.

---

# ❤️ Autor

Desarrollado por Alex Abou.

Proyecto iniciado en 2026 con el objetivo de construir una compañera virtual completamente local utilizando modelos de inteligencia artificial.

---

# 🤖 Herramientas de desarrollo

Durante el desarrollo de NovaAI se utilizaron herramientas de inteligencia artificial como apoyo al aprendizaje, diseño de arquitectura y resolución de problemas.

## ChatGPT (OpenAI)

ChatGPT fue utilizado como asistente de desarrollo para:

- Diseñar la arquitectura general del proyecto.
- Explicar conceptos de Python y programación orientada a objetos.
- Resolver errores y realizar tareas de depuración.
- Proponer mejoras de diseño y buenas prácticas.
- Documentar el proyecto.
- Revisar y optimizar fragmentos de código.
- Ayudar en el aprendizaje durante el desarrollo.

Todas las decisiones finales, integración del código y evolución del proyecto fueron realizadas por el autor.

---

## LM Studio

LM Studio permite ejecutar modelos de lenguaje completamente de forma local.

NovaAI utiliza LM Studio como servidor compatible con la API de OpenAI para comunicarse con modelos LLM sin necesidad de enviar información a servicios externos.

Modelo utilizado actualmente:

- Qwen3-VL-8B-Instruct-GGUF (Q4_K_M)

El modelo puede cambiarse fácilmente modificando el archivo `.env`.

# 🎯 Filosofía del proyecto

NovaAI nació como un proyecto personal con un doble objetivo:

- Aprender desarrollo de software e inteligencia artificial desde cero.
- Construir una compañera virtual completamente local, modular y escalable.

El proyecto prioriza una arquitectura limpia, código mantenible y un desarrollo progresivo, documentando cada nueva versión para facilitar el aprendizaje y la evolución del sistema.