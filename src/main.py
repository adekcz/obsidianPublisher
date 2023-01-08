# -*- coding: utf-8 -*-
import os
import fileStructureGenerator


if __name__ == "__main__":
    path = "D:\\temp\\obsidian test"
    #run_command_on_files(path, "pandoc", "-t html -o", ".html")
    path_index = path+ os.sep +"index.html"
    #fileStructureGenerator.generate_html_file(path, path_index)
    ftp.upload_file(path_index)


