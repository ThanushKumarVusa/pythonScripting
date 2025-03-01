#!/usr/bin/python3

import os
import pwd
import grp
import subprocess

user_name = input("Enter username: ")
group_name = input("Enter groupname: ")

try:
	grp.getgrnam(group_name)
	print(f"group {group_name} exists, skipping....")
except KeyError:
	print(f"Group {group_name} doesn't exist, so creating it..... ")
	try:
		subprocess.run(["groupadd",group_name],check=True)
	except subprocess.CalledProcessError:
		print(f" Failed to create Group {group_name}, Exiting...")
	exit(1)


try:
	pwd.getpwnam(user_name)
	print(f"user {user_name} exists, skipping....")
except ErrorKey:
	print(f" {user_name} doesn't exist, so creating user and adding to {group_name}..... ")
	try:
		 subprocess.run(["useradd", "-m", "-G", group_name, user_name], check=True)
	except subrprocess.CalledProcessError:
		print(f"Failed to add {user_name} to the {group_name} exiting...")
	exit(1)

try:
	subprocess.run(["usermod","-aG",group_name,user_name], check=True)
	print(f"User '{user_name}' has been added to group '{group_name}'.")
except subprocess.CalledProcessError:
    print(f"Error: Could not add user '{user_name}' to group '{group_name}'.")


