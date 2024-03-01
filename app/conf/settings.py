

class Settings():

    def __init__(self):


        self.language = 'en'

        #folders
        self.logs_file = "logs/logs.log"
        self.original_folder = "data/images"
        self.cropped_folder = "data/cropped"
        self.box_labels_folder = "data/box"

        #image        
        self.urls = ['https://www.twitch.tv/valorant_americas'] # Streams to use. For now only use EN streams
        self.region = (1325,200,490,1480) # region to take screenshot in selenium browser   
        self.interval = 10 # time between screenshots
        self.duration = 120 # total time taking screenshoots

        #box
        self.box_batch_size = 10 # batch size for getting box labels
