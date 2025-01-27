import os

def current_working_dir():
    # Current working directories as getcwd
    dir = os.getcwd()
    # in Print statment f is used to insert dyanmically result or variable
    print(f"Current Working directories: {dir}")

def create_new():
    #new_dir = "Demo"
    # Directory name should always be in ' '
    os.makedirs('new')
    print("Successfully created Directories....")
   
def change():
    path = "/home/amitt-ashok/"
    os.chdir(path)
    print(f"Current working dir is {os.getcwd()}")
    os.removedirs('raja')
    #os.makedirs('raja')
   
def list_dir():
    path = "/home/amitt-ashok/Downloads"
    os.chdir(path)
    current = os.getcwd()
    file_and_dir = os.listdir()
    for item in file_and_dir:
        print(f"Directories and Files are: {item}")
  
# Create Directories inside Directory
def create_dir():
    os.makedirs('raja/rani', exist_ok=True)
    print("Created succesfully")     
    
def new_file():
    with open('sample.txt', 'w') as f:
        f.write('Hello')       

def remove_file():
    os.remove('sample.txt')
    print("file removed successfully..")   
    
def put_env():
    os.putenv('name', 'amitt')
    print("name:", os.getenv('name'))  
    os.putenv('MY_VAR', '1234')
    print("MY_VAR:", os.getenv('MY_VAR'))      
    
    
os.chmod("/home/amitt-ashok/shell_script/log.txt", 0o777)   


# Path Manipulation
def path_editor():
    working_dir = os.getcwd()
    print("Current working dir :", working_dir)
    file_name = "demo.txt"
    # here file_name will add with working directory path 
    file_path = os.path.join(working_dir, file_name )
    print("Full file path is :", file_path)
    if not os.path.isfile(file_path):
        with open (file_path, 'w') as f:
            f.write('Hello, World')
    print(f"File exsist: {os.path.isfile(file_path)}")   
    # Result is True
    print(f"Dir Exsist: {os.path.isdir(file_path)}")          
    # result is False
    
def system_editor():
    # use for system related informations
    os.system('echo "Hello From Amitt Ashok"') 
    print(f"Process ID {os.getpid()}")
    print(f"Get Login in user {os.getlogin()}")

def permission_file():
    file_name = "demo.txt"
    with open(file_name, 'w') as f:
        f.write('I am living awsome Life')
    os.chmod(file_name, 0o777)    
    print(f"Permission chnaged {file_name}")
    
current_working_dir()
#new_dir = "raja"
#create_new()

#change_dir = "/home/amitt-ashok/Desktop"
#change()    
#list_dir()
#create_dir()
#new_file()
#remove_file()
#put_env()
#path_editor()
#permission_file()
#system_editor()
