from os import listdir
from loguru import logger
import pickle
import easyocr
from utils.utils import create_folder_if_not_exists
from conf.settings import Settings

settings = Settings()
logger.add(settings.logs_file, level="INFO") 

def save_streamer_labels(streamer,batch_size,reader,folder):
    images = listdir(f"{settings.cropped_folder}/{streamer}")    
    logger.info(f"Images of streamer {streamer}: {images}")
    if '.ipynb_checkpoints' in images:
        images.remove('.ipynb_checkpoints')    
    images_folder = [f"{settings.cropped_folder}/{streamer}/{image}" for image in images]

    logger.info(f"Using batch size of {batch_size}")
    batches = [images_folder[i:i+batch_size] for i in range(0, len(images_folder), batch_size)]
    logger.info(f"Amount of batches: {len(batches)}")
    
    streamer_result = {}
    for batch in batches:  
        logger.info(f"Streamer: {streamer}, Batch: {batch}")
        batch_result = reader.readtext_batched(batch)   
        logger.info(f"Saving Batch")

        for image_index in range(len(batch)):
            logger.info(f"Saving {batch[image_index]}")
            with open(f"{folder}/{batch[image_index].split('/')[-1].strip('.png')}.pkl", "wb") as box_dictionary_labels:   
                pickle.dump(batch_result[image_index], box_dictionary_labels)
        logger.info(f"Batch successfully saved")
    return streamer_result


def get_box_labels():
    reader = easyocr.Reader([settings.language],cudnn_benchmark=True)
    logger.info(f"Created OCR")    
    streams = listdir(settings.cropped_folder)
    logger.info(f"Streams: {streams}")    
    for streamer in streams:  
        logger.info(f"Getting labels of {streamer}")    
        folder = f"{settings.box_labels_folder}/{streamer}"
        create_folder_if_not_exists(folder)   
        result = save_streamer_labels(streamer,settings.box_batch_size,reader,folder)        
        logger.info(f"Successfully written results to {folder}/labels")    