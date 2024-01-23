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

### License

MIT License

Copyright (c) 2024 jkc bv

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
