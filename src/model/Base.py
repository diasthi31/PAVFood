from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/pavFood', echo=True)
Base = declarative_base()
db = SQLAlchemy()