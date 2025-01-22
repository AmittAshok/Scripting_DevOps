#!/bin/bash
#

# check if there is running container

running=$( docker ps -q)

if [ -z "$running" ];then
        echo " no running containers"
else
        echo "removing Containers..."

# Stop all running conatiner
docker stop $(docker ps -aq)      # Stops all running containers
docker rm $(docker ps -aq)        # Removes all containers
echo "Conatiner removed successfully.."
fi

# remove images
echo " Removing docker images"
docker rmi -f $(docker images -q)
docker image prune --all
echo "Images deleted successfully"

