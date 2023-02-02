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
<div>I write these notes after I finish listening to/watching some
content. I do not attempt to properly summarize the content but only to
write my thoughts. E.g. what I found interesting or what I didn’t knew. Which is
all heavily subjective and probably not valuable for anyone else. Yet,
one of the reasons why I do this publicly is that I feel bit more
pressure to spend some time on this.</div>
<div>These notes do represent me and my writing somewhat, but I do not
optimize for quality or readability for others.</div>
<div>This exists for several purposes. 
<ol>
<li><strong>Tool exploration:</strong> Automation for generating and uploading html files
from my obsidian notes is written using github copilot. Potentially
important tool to familiarize oneself with. </li>
<li> <strong>Retention:</strong> I do consume a lot of content. Seems like
retention is low. This is yet another attempt to increase information
retention and squeeze more value out of content consumption. 
</li>
<li> <strong>Metrics:</strong> I keep simple metrics that I want to use to
evaluate which podcast should I (maybe) listen less, stop listening
altogether etc. This would be easily done in simple google sheet. But it
is small additional motivation to keep honing my notes. 
</li>
<li> <strong>Writing upskilling:</strong> My believe is that to get good at
writing and summarizing you need to write and summarize a lot. I am
currently looking for new career opportunities which might possibly
involve a lot of that. This is my practice ground.</div> 
</li>
</ol>
<div>My experience when I don’t take intentional notes is that I am often
not able to recall any insights or facts from podcast I listened to more
than week ago. Which would suggest listening to nonfiction podcast might
not be very valuable. Is it worth it? This page should help.</div>


{content}
</body>
</html>
"""
