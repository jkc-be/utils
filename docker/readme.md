# Docker Utility Script

## Overview
This Bash script provides a convenient utility for Docker operations. It automates the following tasks:
1. Building a Docker container.
2. (Optionally) running the container. Make sure to add compose.yml in Docker directory
3. (Optionally) pushing the container to Azure Container Registry (ACR).
4. (Optionally) pruning unused local containers.

This repo contains code sourced from: https://github.com/crccheck/docker-hello-world to start and run a simple hello-world webapp

## Prerequisites
- Docker installed and running on your machine.
- (Optionally) Access to an Azure account and Azure CLI installed for ACR operations.

## Usage
- This script should be run from the 'main' directory of your project.
- Alternatively you can run it from utils/ (one level below 'main')

### Configuration
Before using the script, you need to set your container registry name in the script:
```bash
CONTAINER_REGISTRY_NAME="YourContainerRegistryName"
```
