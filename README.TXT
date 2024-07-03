# Instrucciones para configurar y ejecutar el proyecto

## Configuración inicial

1. **Abrir el entorno virtual:**

   Abre tu terminal y navega hasta el directorio donde tienes configurado tu entorno virtual.

   
   # Windows
   .\venv\Scripts\activate

2.Actualizar pip:

    Asegúrate de tener la última versión de pip para instalar las dependencias correctamente.

   
    
    python -m pip install --upgrade pip

3.Instalar las dependencias del proyecto:

    Utiliza el archivo requirements.txt para instalar todas las bibliotecas necesarias.


    pip install -r requirements.txt

    (SI TIENE PROBLEMAS PUEDE INSTALAR DJANGO 4.1.2 Y LA ULTIMA VERSION DE PILLOW POR SEPARADO)

4.Ejecutar el servidor local:

    Una vez instaladas las dependencias, puedes iniciar el servidor de desarrollo.

    
    python manage.py runserver