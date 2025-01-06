#The logs in your application server are growing rapidly. 
# You are required to create a shell script that checks the size of log files in a 
# specified directory every day. If the log file exceeds 1GB, the script should archive the 
# logs and delete the original file. The archive should be timestamped and stored in a separate 
# backup folder.

import os
import shutil
from datetime import datetime

import os
import shutil
from datetime import datetime

log_dir = "/home/amitt-ashok/logfile"
backup_dir = "/home/amitt-ashok/Desktop/Backup"
MAX_LOG_SIZE_GB = 1024

def check_and_archive_logs():
    # Ensure the backup directory exists
    os.makedirs(backup_dir, exist_ok=True)

    # Iterate over all files in the log directory
    for log_file in os.listdir(log_dir):
        log_path = os.path.join(log_dir, log_file)

        # Skip non-files
        if not os.path.isfile(log_path):
            continue

        # Get the file size in GB
        file_size_gb = os.path.getsize(log_path) / (1024 ** 1)

        # Archive if the file size exceeds the limit
        if file_size_gb > MAX_LOG_SIZE_GB:
            # Generate a timestamped archive name
            timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            archive_name = f"{log_file}_{timestamp}.tar.gz"
            archive_path = os.path.join(backup_dir, archive_name)

            try:
                # Create the archive
                shutil.make_archive(archive_path.replace('.tar.gz', ''), 'gztar', log_dir, log_file)
                print(f"Archived {log_file} to {archive_path}")

                # Delete the original file
                os.remove(log_path)
                print(f"Deleted original file: {log_path}")
            except Exception as e:
                print(f"Error archiving {log_file}: {e}")

if __name__ == "__main__":
    check_and_archive_logs()
