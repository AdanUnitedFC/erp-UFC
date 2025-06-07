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

## Scripts

- Levantar backend:
    cd backend && uvicorn app.main:app --reload

- Levantar frontend:
    cd frontend && python3 -m http.server 8000
  Luego abrir http://localhost:8000 en el navegador
