# Simple script to test the connection to the SQL Server
# This script is used in the Dockerfile to test the connection to the SQL Server

# DO NOT USE connection_string.txt IN PRODUCTION

import logging
import pyodbc

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Get the root logger and add the file handler to it
log = logging.getLogger()


# MAIN
with open("connection_string.txt", "r") as f:
    connection_string = f.read()

cnxn = pyodbc.connect(connection_string)
cursor = cnxn.cursor()

print(cursor.execute("SELECT @@version;").fetchall())
cursor.close()
