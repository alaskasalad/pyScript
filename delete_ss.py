import os, shutil
from dotenv import load_dotenv

load_dotenv()
# get path to saved pictures 
path = os.getenv('SCREENSHOT_PATH')

def removePics():
    for pics in os.listdir(path):
        os.remove(os.path.join(path, pics))

removePics()