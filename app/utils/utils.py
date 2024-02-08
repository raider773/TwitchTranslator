import os
from loguru import logger
from conf.settings import Settings

settings = Settings()

logger.add(settings.logs_file, level="INFO") 

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logger.info(f"Folder '{folder_path}' created")
    else:
        logger.info(f"Folder '{folder_path}' already exists")