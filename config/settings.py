import os
from dotenv import load_dotenv

load_dotenv()

class Settings():

    POSTGRES_USER       =   os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD   =   os.getenv('POSTGRES_PASSWORD')
    DATABASE_PORT       =   os.getenv('DATABASE_PORT')
    DATABASE_NAME       =   os.getenv('DATABASE_NAME')
    DATABASE_SERVER     =   os.getenv('DATABASE_SERVER')


    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DATABASE_SERVER}/{DATABASE_NAME}"





settings = Settings()