#!/bin/bash
echo "sh util to:\n1.build container\n2.optional:run container\n3.optional:push container to ACR\n4.optional:prune unused local containers\n"

# adjust this to your container registry name
CONTAINER_REGISTRY_NAME="PLACEHOLDER"

# Get the name of the current directory
current_dir=$(basename "$PWD")

# Script can be run from /utils/make_docker.sh or /make_docker.sh
if [ "$current_dir" = "utils" ]; then
    # Navigate up if in 'utils' directory
    cd ../..
# elif [ "$current_dir" != "main" ]; then
#     # If not in 'dofeverhour' or 'utils', exit the script with a message
#     echo "This script should be run from the 'main' (top level git) or 'utils' directory."
#     exit 1
fi

# Function to check if Docker daemon is running
check_docker() {
    docker info > /dev/null 2>&1
}

# Function to start Docker
start_docker() {
    # Using open command to start Docker.app
    open -a Docker
    echo "Starting Docker..."
    # Wait for Docker to start (adjust the timing as necessary)
    for i in {1..60}; do
        if check_docker; then
            echo "Docker is now running."
            return 0
        fi
        sleep 1
    done
    echo "Docker failed to start."
    return 1
}

# Try to connect to Docker daemon
if ! check_docker; then
    start_docker
else
    echo "Docker is already running."
fi

# base image
BASE_IMAGE=${1:-$(read -p "1.Enter image name: " base_image; echo $base_image)}
VERSION=${2:-$(read -p "1.Enter version: " version; echo $version)}
IMAGE_NAME="$BASE_IMAGE:$VERSION"

# Build and tag the image
docker build -t $IMAGE_NAME .

# Update docker-compose.yml
# Replace the image name in docker-compose.yml with the new image name
sed -i '' "s|image: .*|image: $IMAGE_NAME|" compose.yml

echo -e "\n==> Build and update completed for \033[1;34m$IMAGE_NAME\033[0m\n"

# Ask if the user wants to run the container
read -p "2.Do you want to run the container? (y/n): " answer

if [ "$answer" = "y" ]; then
    echo "\n"
    docker-compose up
    echo "\n"
fi

# Ask if the user wants to push to azure
read -p "3.Do you want to push the container to azure container registery? (y/n): " answer

if [ "$answer" = "y" ]; then
    read -p "3.Are you connected with az cli ? (y/n) " azcli
    if [ "$azcli" != "y" ]; then
        echo "\n"
        az login
    fi
    az acr login --name $CONTAINER_REGISTRY_NAME
    docker tag $IMAGE_NAME $CONTAINER_REGISTRY_NAME.azurecr.io/$BASE_IMAGE
    docker push $CONTAINER_REGISTRY_NAME.azurecr.io/$BASE_IMAGE
    echo "\n"
fi

# Ask if the user wants to push to azure
read -p "4.Do you want to prune unused local images (no containers)? (y/n): " answer

if [ "$answer" = "y" ]; then
    echo "\n"
    docker image prune -a
else exit 0
fi