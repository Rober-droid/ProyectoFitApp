# ProyectoFitApp- Sistema de registro de Gimnasios
Proyecto básico para practicar operaciones CRUD
Proyecto CRUD desarrollado con **Python (Flask)** para gestionar clientes de un gimnasio: registrar, editar, eliminar y visualizar información.

#### Funcionalidades principales

- Registrar nuevos clientes
- Editar datos existentes
- Eliminar registros
- Visualizar lista de clientes

#### Funcionalidad extra

-Analisis Sonarcloud para el analisis de codigo

Tecnologías utilizadas

- Python
- Tkinter
- Flask
- MySQL
- mysql.connector 
- HTML + CSS 
- Postman (para pruebas)
- GitHub Actions + SonarCloud (análisis de código)

   1.-Clona el repositorio:
   ```bash
   git clone https://github.com/Rober-droid/ProyectoFitApp.git
   cd fitapp

   2.- Crea un entorno virtual y actívalo
   python -m venv venv
   source venv/bin/activate

   3.-Instala las dependencias
   pip install -r requirements.txt

   4.-Crea la base de datos con el script de database.sql y luego configura la conexion en conexion.py

   5.- Ejecuta la aplicación. Existen 3 opciones
   zona_fit_app.py con solo lenguaje python
   zona_fit_gui.py utilizando la libreria tkinter
   appFlask.py utilizando Flask

   En la carpeta de pruebas se presentan imagenes con las pruebas realizadas en postman
   Los archivos AnalisisSonar.propeties y analisisSonar.yml sirven para el analisis de codigo el codigo sirve para ejecutar un analisis en la cuenta de Sonar Cloud vinculada a la cuenta     de github cada vez que se hace un commit
