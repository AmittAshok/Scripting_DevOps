import os
import shutil
from datetime import datetime

def create_backup(source_dir, backup_dir):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    # /home/amitt-ashok/Desktop/Backups/backup1_time
    backup_file = os.path.join(backup_dir, f"BackUp_{timestamp}")
    
    try:
        if not os.path.isdir(backup_dir): 
            os.makedirs(backup_dir)
        else:
            print(f"{backup_dir} is already exist")   
    except Exception as e:
        print(f"Error in creating dir {e}")
        return
    
    try:
        shutil.copyfile(source_dir,backup_file ) 
        
        print(f"Backup successfully complted in {backup_file}")
    except Exception as e:
        print(f" Error while copying {e}")

    try:
        if shutil.make_archive(backup_file, 'zip'):
            print("Zip successfully done")
            os.remove(backup_file)   
    except Exception as e:
        print("Error while archieve")

    
source_dir = "/home/amitt-ashok/test.txt"
backup_dir = "/home/amitt-ashok/Desktop/Backups1"
create_backup(source_dir, backup_dir)
               