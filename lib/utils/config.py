import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path(os.getenv('DATA_DIR'))
RAW_FILE = Path(os.getenv('RAW_FILE'))
OUTPUT_FILE = Path(os.getenv('OUTPUT_FILE'))
