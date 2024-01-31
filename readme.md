# Purpose

This repository serves as a publicly available collection of various utility code snippets, designed to aid in a range of development tasks.

Most shell scripts are designed to be run on macOS with arm64 (apple sillicon)

## Modules

### 1. Docker
This module contains utility scripts and Dockerfile configurations to streamline Docker-related operations.

- **build-run-push**:  
  A utility shell script designed to simplify the process of running, building, and pushing Docker containers to Azure Container Registry (CR).

- **python-mssql18**:  
  A Dockerfile that sets up a Linux environment equipped with Python and `pyodbc`, enabling connections to MSSQL18 databases.

- **docker-rm-rf**:

  Clean up everything docker related; use with some caution!

### 2. rsa-aes
This module contains a python script to generate RSA 4096 pem keypair and uses the public key to encrypt a generated AES key
