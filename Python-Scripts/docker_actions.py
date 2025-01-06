import docker
import docker.errors

#client = docker.from_env()
#client.containers.run("ubuntu","echo Hello world")
   
client = docker.from_env()

running_Conatiner = client.containers.list(all=False)
for container in running_Conatiner:
    print(f"Container id {container.id}")
    print(f"container name {container.name}")
    print(f"container status : {container.status}")
    #print("-" * 40)

def create_conatiner(image_name, container_name, command=None, ports=None):
    
    try:
        client = docker.from_env()
        
        print(f" Pulling images...")
        #client.images.pull()
        client.images.pull(image_name)
        
        print(f"Creating and staring conatiner: {container_name}")
        container = client.containers.run(
            image=image_name,
            name=container_name,
            command=command,
            ports=ports,
            detach=True
        )
        print(f"container {container_name} is running")
        return container
    except docker.errors.DockerException as e:
        print(f"Error while creaing {e}")
        
if __name__ == "__main__":
    image_name = "nginx"
    container_name = "my_nginx_container"
    ports = {"80": "80"}
    create_conatiner(image_name, container_name, ports=ports)                            