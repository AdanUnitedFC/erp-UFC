# UFC Intrasys

ERP para forwarding. Fullstack en FastAPI + React + SQLite.

## Backend

- FastAPI + JWT Auth
- `/token`: login
- `/upload/importacion`: subir Excel de importaciones
- `/upload/exportacion`: subir Excel de exportaciones
- `/data/importaciones`: obtener lista de importaciones
- `/data/exportaciones`: obtener lista de exportaciones
- `/history/`: ver historial de archivos subidos
- `/history/{id}`: eliminar archivo y registros asociados

## Frontend

 - Interfaz HTML con menú lateral estilo ERP para acceder a los módulos de
   subida de archivos, importaciones, exportaciones y el historial.
 - Las tablas de datos utilizan DataTables con filtros por columna.

## Instalación

1. Crea y activa un entorno virtual:
   ```bash
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```
2. Instala las dependencias del backend:
   ```bash
   pip install -r backend/requirements.txt
   ```

## Scripts

- Levantar backend:
    cd backend && python -m uvicorn app.main:app --reload

- Levantar frontend:
    cd frontend && python -m http.server 8000
  Luego abrir http://localhost:8000 en el navegador
