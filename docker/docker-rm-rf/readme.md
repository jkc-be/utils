# dockerrmrf - Docker Cleanup Script

`dockerrmrf` is a shell script that helps you clean up your Docker environment by stopping and removing all containers, images, volumes, and networks. It's designed to be a simple and convenient way to keep your Docker system clean.

## Usage

1. **Download the Script**
   - You can download the `dockerrmrf` script from [this link](https://github.com/jkc-be/utils/blob/main/docker/docker-rm-rf/dockerrmrf.sh).

2. **Make the Script Executable**
   - Open Terminal.
   - Navigate to the directory where you downloaded the script.
   - Run the following command to make the script executable:
     ```bash
     chmod +x dockerrmrf.sh
     ```

3. **Move the Script to a Directory in Your PATH**
   - You can move it to `/usr/local/bin`, which is typically included in the system's PATH. Use this command (you might need to enter your password):
     ```bash
     sudo mv dockerrmrf.sh /usr/local/bin/dockerrmrf
     ```

4. **Run the Script**
   - To clean up your Docker environment, simply open your terminal and type the following command:
     ```bash
     dockerrmrf
     ```
   - Press Enter, and the script will execute the necessary Docker cleanup commands.

## Caution

- This script will forcefully remove all Docker containers, images, volumes, and networks.
- Make sure to backup any important data before running the script.
- Use it with caution, as the cleanup is irreversible.
