import utils
import os
import re
import utils.pathUtils as pathUtils
import subprocess

#recursively go through all the files in the directory
# and run external command on each file
# and save the output to a file

def run_command_on_files(directory, suffix):
    command = "pandoc", 
    parameters = " ",
    for root, dirs, files in os.walk(directory):
        for file in files:
            if(file.endswith(".md")):
                file_path = os.path.join(root, file)
                temp_file = pathUtils.escape_path(root + os.sep +"content.tmp")
                #replace dataview query with pandoc template variable, and output to temp file
                convert_command = "(Get-Content -path "+ pathUtils.escape_path(file_path) +") -Replace \"``= this.(\w+)``\", '$$$1$$' | Out-File  -Encoding \"UTF8\" " + temp_file  + ";"
                css_directory = pathUtils.remove_prefix(root , directory +  os.sep)
                css_directory_final = "/".join([".." for x in css_directory.split("\\")]) + "/resources/"
                css_part =  " --css=" + pathUtils.escape_path(css_directory_final + "styles.css")
                #pandoc file --template temp_file to apply template
                #pandoc -s -t .... to convert to html
                convert_command += " pandoc " +  pathUtils.escape_path(file_path)  + " --template" + " " +temp_file + " | pandoc -s -t html --metadata title=\"" + file.split(".")[0] + "\" -o " + pathUtils.escape_path(file_path+suffix) + css_part
                print("Executing: " + convert_command)
                run(convert_command)

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed