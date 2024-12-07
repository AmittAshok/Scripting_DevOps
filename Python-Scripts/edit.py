import os

file_name = "demo.txt"

with open(file_name, 'w') as f:
    f.write('I am living awsome Life')

os.chmod(file_name, 0o777)    
print(f"Permission chnaged {file_name}")