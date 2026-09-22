import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    Origins = os.getenv("ORIGINS")
    SECREAT_KEY= os.getenv("SECREAT_KEY")
    DB_URL= os.getenv("DB_URL")

settings = Settings()
