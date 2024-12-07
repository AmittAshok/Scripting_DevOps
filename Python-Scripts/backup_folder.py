import os
import shutil
from datetime import datetime

def create_backup(source_dir, backup_dir):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    # /home/amitt-ashok/Desktop/Backups/backup1_time
    backup_folder = os.path.join(backup_dir, f"backup1_{timestamp}")
    
    try:
        if not os.path.isdir(backup_dir): 
            os.makedirs(backup_dir)
        else:
            print("No needed to create")   
    except Exception as e:
        print(f"Error in creating dir {e}")
        return
    
    try:
        shutil.copyfile(source_dir,backup_folder ) 
        print(f"Backup successfully complted in {backup_folder}")
    except Exception as e:
        print(f" Error while copying {e}")
    
source_dir = "/home/amitt-ashok/test.txt"
backup_dir = "/home/amitt-ashok/Desktop/Backups1"
create_backup(source_dir, backup_dir)
               