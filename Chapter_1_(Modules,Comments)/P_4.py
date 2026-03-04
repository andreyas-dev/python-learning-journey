import os

# Specify the directory path (use '.' for the current folder)
path = "/Semester 6" 

try:
    # Get the list of all files and directories
    dir_list = os.listdir(path)
    
    print(f"Files and directories in '{path}':")
    for item in dir_list:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")