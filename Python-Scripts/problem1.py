# You are managing multiple servers, and your task is to automate the process of checking 
# if any services like Apache or Nginx have stopped. If they are stopped, 
# the script should attempt to restart the service and log the event with a timestamp.

import os
import shutil
import psutil
import subprocess

services = ['nginx', 'jenkins']
def check_nginx_status(service_name):
    try:
        
        result = subprocess.run(['systemctl', 'is-active', 'jenkins'], stdout= subprocess.PIPE, stderr= subprocess.PIPE, text=True)
        
        if result.stdout.strip() == 'active':
            print("service is running")
        else:
            print("Not running..")
    except FileNotFoundError:
        print("Command not avilable")
    except Exception as e:
        print(f"An erroe occouer {e}")

def multiple_service_check(services):
    for service in services:
        check_nginx_status(service)
                           
def restart_services():
    for service in services:
        restart = subprocess.run(['systemctl', 'restart', service])
        print("restart successfully..")       
                            
if __name__ == "__main__":
    services_to_check = ['nginx', 'jenkins']
    multiple_service_check(services_to_check)
    restart_services()  
                  