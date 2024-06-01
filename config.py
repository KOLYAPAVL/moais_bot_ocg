from __future__ import annotations

import os

from dotenv import load_dotenv


load_dotenv()

# Токен бота
API_TOKEN: str = os.getenv('BOT_API_TOKEN')

# Авторы
AUTHORS: list[str] = str(os.getenv('AUTHORS', '')).split(",")

# Изображение
INFO_IMAGE: str = os.getenv('INFO_IMAGE', '')
