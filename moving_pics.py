import os, shutil, schedule, time
from dotenv import load_dotenv

load_dotenv()
# get path to saved pictures 
path = os.getenv('PICTURES_PATH')

'''
check if getenv worked  
print('PICTURES_PATH' in os.environ)
print(path)
'''

# list out all the directories in this path 
file_name = os.listdir(path)
folder_names = ['jpeg files', 'pdf files', 'png files', 'web files']

# create files if needed 
def create_folders():
    for loop in range(len(folder_names)):
        if not os.path.exists(path + folder_names[loop]):
            os.makedirs(path + folder_names[loop])

# check if picture is in path and not in the correct folder 
def check(file, string1, string2):
    if string1 in file and not os.path.exists(path + string2 + file):
            shutil.move(path + file, path + string2 + file)

# move all the pictures that are not in folders 
def move_pictures():
    for file in file_name:
        check(file, ".png", "png files\\")
        check(file, ".jpeg", "jpeg files\\")
        check(file, ".pdf", "pdf files\\")
        check(file, ".webp", "web files\\")

# main body 
def script(): 
    create_folders()
    move_pictures()

script()