ECOMERCE - PROYECTO GRUPAL CICLO 3

Por:
    Juan Camilo Parra
    Laura Carrillo
    Laura Pinzón
    Mauricio Martínez
    Natalia Morales Ruiz

Tecnologías:
    La aplicación WEB se desarrolla con Flask
    La conexión con la base de datos se realiza a partir de SQLAlquemy y sus migraciones con Flask-Migrate

Lo que queremos:
    Se quiere crear una página web de E-comerce de productos de confitería en la que habrá tres tipos de usuarios
    con los siguientes permisos:
        CLIENTE:    Puede hacer login,
                    visualizar productos, 
                    agregarlos al carrito, 
                    hacer una lista de deseos 
                    y realizar comentarios a los productos
        ADMIN:      Puede hacer login,
                    gestionar los productos, agregando, editando o eliminando
                    gestionar los clienteS, agregando, editando o eliminando
        SUPERADMIN: Comparte todo lo que puede hacer CLIENTE y ADMIN

Lo que hemos logrado:
    - Visualizar la página de inicio
    - Registrarse en en la página WEB
    - Hacer login
    - Visualizar cada producto
    - Agregar productos al carrito
    - Se inició la creación de la vista para el ADMIN http://127.0.0.1:5000/admin

Contenido de esta carpeta:
    - "main.py"             archivo principal para ejecutar la app
    - "populate.py"         archivo para inicializar la base de datos
    - "requirements.txt"    archivo para instación de paquetes necesarios
    - "migrations"          carpeta generada automaticamente a partir de Flask-Migrate
    - "website"             carpeta que contiene los archivos.py y templates de archivos.html así como archivos estáticos

Para usar la app:
    - Crear un ambiente de desarrollo dentro de la carpeta llamada "minticFlaskWebsite"
    En una terminal:
        - Preparar el ambiente instalando los requerimientos con $ pip install -r requirements.txt
        - Crear la variables de entorno:
            En una terminal de unix:    $ export FLASK=main
                                        $ export FLASK_ENV
            En una terminal de windows: $ set FLASK=main
                                        $ set FLASK_ENV
        - Implementar las migraciones para la base de datos
            $ flask db upgrade
        - Correr el script populate.py para inicializar la base de datos $ python populate.py
        - Correr la app $ python populate.py
        - Copiar el link http que arroja la terminal en un navegador de preferencia
    En el navegador:
        - Puede ver la página de inicio donde podrá visualizar los productos
        - Puede registrarse en el sistema y agregar productos a la base de datos
        - Para visualizar el perfil del administrador debe usar la ruta:  http://127.0.0.1:5000/admin
