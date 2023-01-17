import utils
import os

#recursively go through all the files in the directory
# and run external command on each file
# and save the output to a file

def run_command_on_files(directory, command, parameters, suffix):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if(file.endswith(".md")):
                file_path = os.path.join(root, file)
                css_directory = "/notes/"
                css_part =  " --css=" + utils.escape_path(css_directory + "styles.css")
                convert_command = command + " " + utils.escape_path(file_path) + " " + parameters + " " + utils.escape_path(file_path+suffix) + css_part
                print("Executing: " + convert_command)
                os.system(convert_command)


# delete all the files in the directory ending with suffix
def delete_files(directory, suffixes):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(suffix) for suffix in suffixes):
                file_path = os.path.join(root, file)
                print("Deleting: " + file_path)
                os.remove(file_path)