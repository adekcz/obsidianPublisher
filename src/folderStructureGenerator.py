import os
import utils.pathUtils as pathUtils

#takes folder path and generates html file containing all the files in the folder recursively
def generate_html_file(path, file_name):
    html = "<ul>\n"
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file.endswith(".html")):
                file_path = os.path.join(root, file)
                file_path = pathUtils.remove_prefix(file_path, path)
                file_path = file_path.replace("\\", "/")
                css_class = "podcast" if file_path.startswith("Podcasts") else "book" if file_path.startswith("Books") else ""
                html += "<li class=\"" + css_class + "\"><a href=\"./" + file_path + "\">" + file_path + "</a><br/></li>\n"
    html += "</ul>\n"

    #write to file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(html_template().format(content=html))

def html_template():
    return """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<link rel="stylesheet" href="./resources/styles.css">
<title>Michal's Notes</title>
</head>
<body>
{content}
</body>
</html>
"""
