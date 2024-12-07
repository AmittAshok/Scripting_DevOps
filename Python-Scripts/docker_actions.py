import docker

client = docker.from_env()
#client.containers.run("ubuntu","echo Hello world")

running_container = client.containers.list(all=True)
for container in running_container:
    print(f"Container id {container.id}")
    print(f"Container Name: {container.name}")
    print(f"Status: {container.status}")
    print("-" * 40)