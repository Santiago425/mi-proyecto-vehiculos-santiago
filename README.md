# Proyecto Django – Gestión de Vehículos

Este proyecto fue realizado en Django como parte de la actividad del curso.  
El objetivo principal es crear una aplicación que permita gestionar vehículos,  
donde se puedan registrar, editar, eliminar y visualizar los datos.

---

## 🚗 Funcionalidades principales

La aplicación permite:

- Crear un vehículo
- Editar un vehículo
- Eliminar un vehículo
- Ver la lista de vehículos registrados

Estas funciones se manejan con formularios, modelos y vistas en Django.

---

## 📁 Estructura del proyecto

El proyecto está dividido en:

### 🟦 Carpeta **Vehículos/**
Contiene la configuración principal del proyecto:
- `settings.py`
- `urls.py`
- `wsgi.py`
- `asgi.py`

### 🟩 Carpeta **Aplicaciones Vehicles/**
Aquí se encuentra la aplicación desarrollada:
- `models.py` → modelo del vehículo  
- `forms.py` → formulario del vehículo  
- `views.py` → vistas para crear, editar, eliminar y listar  
- `urls.py` → rutas de la aplicación  
- carpeta `templates/` → páginas HTML  
- carpeta `migrations/` → migraciones de la base de datos  

### Otros archivos
- `manage.py`
- `requirements.txt`

---

¿Cómo ejecutar el proyecto?
pip install -r requirements.txt

2. Ejecutar el servidor:
python manage.py runserver

3. Abrir en el navegador:
http://127.0.0.1:8000/


---

## 🧑‍💻 Autor

Santiago Alejandro Campoverde Obando

Proyecto desarrollado siguiendo las instrucciones del docente  
y subido correctamente al repositorio sin archivos comprimidos.


1. Instalar las dependencias:
