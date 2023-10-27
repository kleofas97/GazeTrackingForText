import logging
import os
from datetime import datetime

filepath = os.path.join(os.getcwd(), "data", "logs.txt")
logging.basicConfig(
    level=logging.INFO,
    format=f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} :: %(name)s :: %(levelname)s :: %(message)s',
    handlers=[
        logging.FileHandler(filepath),
        logging.StreamHandler()
    ]
)
logging.info("Logger has been initialized")