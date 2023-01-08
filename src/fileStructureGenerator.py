import os
import utils

#takes folder path and generates html file containing all the files in the folder recursively
def generate_html_file(path, file_name):
    html = ""
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file.endswith(".html")):
                file_path = os.path.join(root, file)
                file_path = utils.remove_prefix(file_path, path)
                file_path = file_path.replace("\\", "/")
                html += "<a href=\"./" + file_path + "\">" + file_path + "</a><br/>"

    #write to file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html)