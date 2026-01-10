# Transport API Backend

API backend desarrollada con **FastAPI** para exponer información básica de rutas y alertas de transporte urbano.

Este proyecto es la base de una plataforma que busca ofrecer información de transporte **actualizada y confiable**, pensada para escalar con datos reales y servicios inteligentes.

## Tecnologías
- Python
- FastAPI
- Uvicorn

## Instalación y ejecución

1. Crear y activar entorno virtual
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
3. Ejecutar el servidor:
uvicorn app.main:app --reload
GET /health
Verifica que la API esté funcionando correctamente.

{
  "status": "ok"
}
