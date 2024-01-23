# Dockerfile for building a Python image with SQL Server ODBC Driver 18 for Linux
# Alternatively can be used for SQL Server 17 replacing msodbcsql18 -> msodbcsql17

# Use a smaller, more efficient base image
FROM --platform=linux/amd64 python:3.11-slim

# Install dependencies required for MS ODBC Driver
RUN apt-get update && apt-get install -y --no-install-recommends \
    # general linux packages
    gnupg \
    curl \
    openssl \ 
    ca-certificates \
    apt-transport-https \
    # odbc packages
    unixodbc \
    libodbc1 \
    # (Optional) C and C++ packages
    libc6 \
    libstdc++6 \ 
    && rm -rf /var/lib/apt/lists/*

# Update CA certificates
RUN update-ca-certificates

# Add SQL Server ODBC Driver 18 for debian
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy only the requirements.txt first to leverage Docker cache
COPY requirements.txt /app/

# Install Python dependencies
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy only the necessary files
COPY ./src /app

# Run app.py when the container launches
CMD ["python", "./testSQL.py"]
