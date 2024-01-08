from dotenv import load_dotenv
import os
import re
load_dotenv()

DB_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


def is_valid_hex_color(color: str) -> bool:
    # Regular expression for matching hex color codes
    pattern = r'^#(?:[0-9a-fA-F]{3}){1,2}$'
    return re.match(pattern, color) is not None
