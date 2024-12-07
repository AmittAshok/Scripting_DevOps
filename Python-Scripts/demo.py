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
#current_working_dir()
#new_dir = "raja"
#create_new()

#change_dir = "/home/amitt-ashok/Desktop"
#change()    
#list_dir()
#create_dir()
#new_file()
#remove_file()
#put_env()