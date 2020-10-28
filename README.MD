# Subasta Backend
## paso 1 ##

## Instalar python en ubuntu
``` bash
sudo apt update
sudo apt install python3.7 python3-dev python3-pip
``` 

## paso 2 
   - Crear entorno virtual en ubuntu  dentro de la carpeta proveedor desde la linea de comandos en la carpeta del proyecto
    ```bash
      python3 -m venv venv
    ```

   - crear entorno virtual en Windows dentro de la carpeta proveedor  desde la linea de comandos en la carpeta del proyecto
    ```bash
        python -m venv venv
    ```

## paso 3 

   - Ejecutar entorno virtual en ubuntu dentro de la carpeta proveedor  desde la linea de comandos en la carpeta del proyecto
      ```bash
        source venv/bin/activate
        ```

   - ejecutar entorno virtual en Windows dentro de la carpeta proveedor  desde la linea de comandos en la carpeta del proyecto
       ```bash
       venv\Scripts\activate
       ```

## paso 4 
   - Instalar requerimientos 
     ```bash
        pip install -r requirements.txt
        ```

## paso 5 
   - agregar las credenciales para conectar a mysql en la carpeta subasta en el archivo settings.py 
   ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': 'DB_NAME',
            'USER': 'DB_USER',
            'PASSWORD': 'admin',
            'HOST': 'localhost',   # o  una direccion  IP donde esta la base de datos
            'PORT': '3306',
        }
    }
   ```

## paso 6 
   - crear migraciones
    python manage.py makemigrations
    
## aplicar migraciones
        python manage.py migrate  

## paso 7 
   - correr el servidor
    python manage.py runserver

    