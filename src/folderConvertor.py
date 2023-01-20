import utils
import os
import re
import utils.pathUtils as pathUtils

#recursively go through all the files in the directory
# and run external command on each file
# and save the output to a file

def run_command_on_files(directory, command, parameters, suffix):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if(file.endswith(".md")):
                file_path = os.path.join(root, file)
                css_directory = pathUtils.remove_prefix(root , directory +  os.sep)
                css_directory_final = "/".join([".." for x in css_directory.split("\\")]) + "/resources/"
                css_part =  " --css=" + pathUtils.escape_path(css_directory_final + "styles.css")
                convert_command = command + " " + pathUtils.escape_path(file_path) + " " + parameters + " " + pathUtils.escape_path(file_path+suffix) + css_part
                print("Executing: " + convert_command)
                os.system(convert_command)