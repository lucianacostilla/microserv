import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Leer detalles de conexión desde variables de entorno
db_user = os.getenv("DATABASE_USER", "root")
db_password = os.getenv("DATABASE_PASSWORD", "taeminkai10")
db_host = os.getenv("DATABASE_HOST", "mysql")  # Nombre del servicio MySQL en Docker Compose
db_name = os.getenv("DATABASE_NAME", "practica")

# Crear URL de conexión a MySQL
DATABASE_URL = f"mysql://{db_user}:{db_password}@{db_host}/{db_name}"

# Configurar SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




##from sqlalchemy import create_engine
# sqlalchemy biblioteca de pythoin para usar con mysql. 
# create_engine establece conexion con bdd
##from sqlalchemy.ext.declarative import declarative_base
# declarative_base hereda clases modelos base que se puede usar. plantilla
##from sqlalchemy.orm import sessionmaker
# crea sesiones

##DATABASE_URL = "mysql://root:taeminkai10@localhost:9190/practica"

##engine = create_engine(DATABASE_URL)
# create_engine establece conexion con la bdd que tiene como valor DATABASE_URL
##SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal almacena el valor de que se crea una sesion con esas caracteristicas usando session
##Base = declarative_base()
# crea una base desde la cual construir estos modelos