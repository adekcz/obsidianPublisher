# -*- coding: utf-8 -*-
import ftp
import os
import utils
import fileStructureGenerator

#recursively go through all the files in the directory
# and run external command on each file
# and save the output to a file
def run_command_on_files(directory, command, parameters, suffix):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if(file.endswith(".md")):
                file_path = os.path.join(root, file)
                css_directory = ".." + os.sep + utils.remove_prefix(root, directory)
                css_part =  " --css=" + escape_path(css_directory + os.sep + "styles.css")
                convert_command = command + " " + escape_path(file_path) + " " + parameters + " " + escape_path(file_path+suffix) + css_part
                print("Executing: " + convert_command)
                os.system(convert_command)
            



#get path path of running script
def get_script_path():
    return os.path.dirname(os.path.realpath(__file__))

def escape_path(file_path):
    file_path = "\"" + file_path + "\""
    return file_path
            




if __name__ == "__main__":
    path = "D:\\temp\\obsidian test"
    #run_command_on_files(path, "pandoc", "-t html -o", ".html")
    path_index = path+ os.sep +"index.html"
    #fileStructureGenerator.generate_html_file(path, path_index)
    ftp.upload_file(path_index)


