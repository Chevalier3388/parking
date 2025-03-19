import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # SQLALCHEMY_TRACK_MODIFICATIONS = False  # Отключаем уведомления о изменениях
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # Используем SQLite по умолчанию
