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
