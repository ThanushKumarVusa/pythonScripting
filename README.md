User and Group Management Script

Description

This Python script allows administrators to manage users and groups on a Linux system. It checks if a specified group exists and creates it if necessary. Then, it checks if a user exists and either adds them to the specified group or creates the user and assigns them to the group.

Prerequisites

The script must be run with root or sudo privileges.

Ensure Python 3 is installed on the system.

Installation

No installation is required. Just download the script and run it with Python 3.

Usage

Open a terminal.

Run the script using:

sudo python3 script.py

Enter the required username and group name when prompted.

Features

Checks if the group exists before creating it.

Checks if the user exists before creating or modifying them.

Adds the user to the specified group if they already exist.

Creates a home directory for new users.

Uses subprocess with error handling to ensure safe execution.

Code Breakdown

Uses grp.getgrnam(group_name) to check if a group exists.

Uses pwd.getpwnam(user_name) to check if a user exists.

Uses subprocess.run() to execute system commands safely.

Example Output

Enter username: alice
Enter groupname: developers
Group 'developers' exists, skipping...
User 'alice' doesn't exist, creating and adding to 'developers'...
User 'alice' is now in group 'developers'.

Potential Enhancements

Logging actions to a file.

Adding error handling for failed system commands.

Accepting arguments from the command line instead of user input.

License

This script is open-source. Feel free to modify and use it as needed.
