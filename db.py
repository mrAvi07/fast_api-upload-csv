import os
import databases, sqlalchemy
from config.settings import settings


DATABASE_URL = settings.DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

students = sqlalchemy.Table(
    "students",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name" , sqlalchemy.String),
    sqlalchemy.Column("mark"      , sqlalchemy.Float),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)

metadata.create_all(engine)