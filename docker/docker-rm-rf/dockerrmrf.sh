#!/bin/bash

# Stop all running containers
docker stop $(docker ps -q) 2>/dev/null

# Remove all containers
docker rm -f $(docker ps -a -q) 2>/dev/null

# Remove all images
docker rmi -f $(docker images -q) 2>/dev/null

# Remove all volumes
docker volume rm $(docker volume ls -q) 2>/dev/null

# Remove all networks (except default networks)
docker network rm $(docker network ls -q) 2>/dev/null

echo "Docker cleanup complete."
