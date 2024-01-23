# python-mssql18

## Overview
This repo provides a Dockerfile that you can use to:
   - Create a linux container with Python3.11 and pyodbc.
   - Connect to a MSSQL server 18 (change Dockerfile for v17).

## Quickstart
   - Update `src/connection_string.txt` with your MSSQL18 credentials **(DO NOT USE IN PRODUCTION)**.
   - Build and run. This can be easily done using `utils/make_docker.sh` utility script in docker/python-mssql18 directory.
   ```bash
   sh utils/make_docker.sh
   ```

If succesfull you should see something like:
```
[('Microsoft SQL Azure (RTM) - 12.0.2000.8 \n\tNov  2 2023 01:40:17 \n\tCopyright (C) 2022 Microsoft Corporation\n',)]
```

