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
                css_directory = ".." + os.sep + utils.remove_prefix(root, directory)
                css_part =  " --css=" + utils.escape_path(css_directory + os.sep + "styles.css")
                convert_command = command + " " + utils.escape_path(file_path) + " " + parameters + " " + utils.escape_path(file_path+suffix) + css_part
                print("Executing: " + convert_command)
                os.system(convert_command)
            