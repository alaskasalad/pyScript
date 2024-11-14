import os, shutil, schedule, time
from dotenv import load_dotenv

load_dotenv()
# get path to saved pictures 
path = os.getenv("PICTURES_PATH")

# list out all the directories in this path 
file_name = os.listdir(path)
folder_names = ['jpeg files', 'pdf files', 'png files', 'web files']

# create files if needed 
def create_folders():
    for loop in range(len(folder_names)):
        if not os.path.exists(os.path.join(path + folder_names[loop])):
            os.makedirs(os.path.join(path + folder_names[loop]))

# move all the pictures that are not in folders 
def move_pictures():
    for file in file_name:
        if ".png" in file and not os.path.exists(path + "png files\\" + file):
            shutil.move(path + file, path + "png files\\" + file)
        elif ".jpeg" in file and not os.path.exists(path + "jpeg files\\" + file):
            shutil.move(path + file, path + "jpeg files\\" + file)
        elif ".pdf" in file and not os.path.exists(path + "pdf files\\" + file):
            shutil.move(path + file, path + "pdf files\\" + file)
        elif ".webp" in file and not os.path.exists(path + "web files\\" + file):
            shutil.move(path + file, path + "web files\\" + file)

# main body 
def script(): 
    create_folders()
    move_pictures()

# runs script every monday @ 9am
def job():
    script()
    schedule.every().monday.at("9:00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
