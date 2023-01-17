# -*- coding: utf-8 -*-
import os
import fileStructureGenerator
import folderConvertor
import ftp


if __name__ == "__main__":
    path = "D:\\Dropbox\\Apps\\Obsidian\\Public\\www"
    folderConvertor.run_command_on_files(path, "pandoc", "-s -t html -o ", ".html")
    path_index = path+ os.sep +"index.html"
    fileStructureGenerator.generate_html_file(path, path_index)
    ftp.upload_files(path)
    folderConvertor.delete_files(path, ".html")