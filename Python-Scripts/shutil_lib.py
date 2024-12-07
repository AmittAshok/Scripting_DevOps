import shutil
import tempfile

def copy_file():
    # use for copy content from source file to destinantion file
    # If destinantion is not created then it will created by code
    source_file = "/home/amitt-ashok/shell_script/Python-Scripts/demo.txt"
    destination_file = "/home/amitt-ashok/Desktop/test.txt"
    
    shutil.copy(source_file, destination_file)
    print(f" Copy operation successfully completed....")
  
def copy_dir():
    # Copy files and Directory from source folder to destinantion
    # but Destinantion shoud not be created already
    source_dir = "/home/amitt-ashok/shell_script"    
    destination_dir = "/home/amitt-ashok/Test"
    shutil.copytree(source_dir, destination_dir)
    
def move_file_dir():
    # Move files and directory from source to destinantion after move operation files will be not there
    source = "/home/amitt-ashok/shell_script"
    dest = "/home/amitt-ashok/Desktop"
    shutil.move(source, dest)
    print("Move operation succesfully completed....")
    
def delete_dir():
    # delete entire directory and it content
    source = "/home/amitt-ashok/test"
    
    shutil.rmtree(source)
    print(f"{source} removed successfully...")  
          
def archive():
    # here in first need to give path where backup is created, followd by format like tar, gztar etc and
    # whose backup need taken in last
    destinantion = "/home/amitt-ashok/shell_script/backup"
    source = "/home/amitt-ashok/aws"
    shutil.make_archive(destinantion, 'tar', source) 
    print(f"Succesfully completed...") 
    
def usage():
    # Check disk usage
    usage = shutil.disk_usage("/")
    print(f"Total: {usage.total // (1024 ** 3)} GB")
    print(f"Used: {usage.used // (1024 ** 3)} GB")
    print(f"Free: {usage.free // (1024 ** 3)} GB")

def temp_dir_creation():
    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"Temp dir created succesfully {tmpdir}")    
        
def custom_copy_oper():
    # This is same as copy operation but use for bigfile operations
    with open ("source.txt", 'rb') as src, open("dest.txt", 'wb') as dest:
        shutil.copyfileobj(src, dest)
        print("successfully completed..")        
#copy_file()
#copy_dir()   
#move_file_dir() 
#delete_dir()
#archive()
#usage()
#temp_dir_creation()
#custom_copy_oper()