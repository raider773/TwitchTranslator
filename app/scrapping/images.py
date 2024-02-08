from loguru import logger
from selenium import webdriver
from PIL import Image
import time
from conf.settings import Settings
from utils.utils import create_folder_if_not_exists

import threading

settings = Settings()
logger.add(settings.logs_file, level="INFO") 

def get_screenshots(url,region,original_folder,cropped_folder,interval,duration):   

    cropped_url = url.split("//")[1].split("/")[1]
    original_destination_folder = f"{original_folder}/{cropped_url}" 
    cropped_destination_folder =  f"{cropped_folder}/{cropped_url}"
    create_folder_if_not_exists(original_destination_folder)
    create_folder_if_not_exists(cropped_destination_folder)
    
    driver = webdriver.Chrome()
    driver.get(url)
    logger.info(f"Connected to url:{url}")    
    time.sleep(20)
    
    for i in range(duration//interval):      
    
        driver.save_screenshot(f"{original_destination_folder}/original_image_{i}.png")
        logger.info(f"Saved original image {cropped_url}/original_image_{i}.png")    
        
        x = region[0]
        y = region[1]
        w = region[2]
        h = region[3]        
        width = x + w
        height = y + h      
        
        im = Image.open(f"{original_destination_folder}/original_image_{i}.png")
        im = im.crop((x, y, width, height))
        im.save(f'{cropped_destination_folder}/cropped_image_{i}.png')
        logger.info(f"Saved cropped image {cropped_url}/cropped_image_{i}.png")
        
        time.sleep(interval)   
        
    driver.quit()



def get_images():

    threads = []
    for url in settings.urls:
        thread = threading.Thread(target=get_screenshots, args=(url,settings.region,settings.original_folder,settings.cropped_folder,settings.interval,settings.duration))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()