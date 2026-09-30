@echo off
echo ================================
echo Instalando NovaAI...
echo ================================

python -m venv venv

call venv\Scripts\activate

pip install -r requirements.txt

echo.
echo Instalacion completada.
pause