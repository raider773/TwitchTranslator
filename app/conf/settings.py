

class Settings():

    def __init__(self):

        #folders
        self.logs_file = "logs/logs.log"
        self.original_folder = "data/images"
        self.cropped_folder = "data/cropped"

        #image        
        self.urls = ['https://www.twitch.tv/rush', 'https://www.twitch.tv/jinnytty']
        self.region = (1325,200,490,1480)
        self.url = 'https://www.twitch.tv/rivers_gg'
        self.interval = 5
        self.duration = 60
