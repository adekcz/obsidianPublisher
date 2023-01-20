import os
import utils.fileUtils as fileUtils
import utils.pathUtils as pathUtils

#create file structure
def create_file_structure(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

#copy file
def copy_file(source, destination):
    with open(source, "rb") as file:
        data = file.read()
    with open(destination, "wb") as file:
        file.write(data)

def copy_resources(source, destination, suffixes):
    create_file_structure(destination)
    for root, dirs, files in os.walk(source):
        for file in files:
            if any(file.endswith(suffix) for suffix in suffixes):
                file_path = os.path.join(root, file)
                file_name = pathUtils.get_file_name(file_path)
                destination_path = destination + os.sep + file_name
                copy_file(file_path, destination_path)

# delete all the files in the directory ending with suffix
def delete_files(directory, suffixes):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(suffix) for suffix in suffixes):
                file_path = os.path.join(root, file)
                print("Deleting: " + file_path)
                os.remove(file_path)