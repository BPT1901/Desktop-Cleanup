import os
import shutil

import send2trash
from datetime import datetime

desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
cleanup_folder = 'Cleanup'
cleanup_dir = os.path.join(desktop_dir, cleanup_folder)
screen_dir = 'Screenshots'
images_dir = 'Images'
movies_dir = 'Videos'
others_dir = 'Others'
path1 = os.path.join(cleanup_dir, screen_dir)
path2 = os.path.join(cleanup_dir, images_dir)
path3 = os.path.join(cleanup_dir, movies_dir)
path4 = os.path.join(cleanup_dir, others_dir)
now = datetime.now()
current_time = now.strftime('%H:%M:%S')
#Create a folder called 'cleanup' on my desktop
#if cleanup doesn't exist, I need to create it
#create 3 x subfolders in cleanup. 1 for screenshots 1 for images (including pdf, jpg etc), 1 for movie files
def cleanup():
    os.makedirs(cleanup_dir)
    os.makedirs(path1)
    os.makedirs(path2)
    os.makedirs(path3)
    os.makedirs(path4)
    print('Creating Cleanup Folder...')

     #Loop through all files on desktop   
    imgs = ('pdf', 'jpg', 'HEIC')
    movies = ('mp4', 'mov', 'MOV')
    others = ('zip', 'dmg' 'xls')
    files_on_desktop = os.listdir(desktop_dir)
     # if there is a screenshot move it to screenshots folder
    for file in files_on_desktop:
        if file.startswith('Screenshot') or file.startswith('Screen Shot'):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, path1)
            print(f'Moving {file}')
    #if there is an image, move it to the images folder
        elif file.endswith(imgs):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, path2)
            print(f'Moving {file}')
    # if there is a video, move to videos folder
        elif file.endswith(movies):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, path3)
            print(f'Moving {file}')
        elif file.endswith(others):
            file_dir = desktop_dir + '/' + file
            shutil.move(file_dir, path4)
            print(f'Moving {file}')
            
    print(f'Cleanup folder completed at: {current_time}')       
      
#Schedule files in the screenshots folder to be deleted after 7 days
def deletes():
    for folder, subfolders, files in os.walk('/Users/benturner/Desktop/CleanUp/Screenshots'):
        for file in files:
            if file.startswith('Screenshot') or file.startswith('Screen Shot'):
                path = os.path.join(folder, file)
                print(f'{file} has been deleted')
                send2trash.send2trash(path)
                
start = input('Would you like to cleanup your desktop? yes/no:')
if start == 'yes':
    cleanup()    
else: 
    print('Cleanup suspended')            

#Schedule auto run for both deletes and cleanup
#schedule.every(1).monday.at("10:00").do(deletes)
#schedule.every(1).monday.at("10:02").do(cleanup)

#while True:
    #schedule.run_pending()
    #time.sleep(1) 



