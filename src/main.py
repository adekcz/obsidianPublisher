# -*- coding: utf-8 -*-
import os
import folderStructureGenerator
import folderConvertor
import ftp
import utils.fileUtils as fileUtils
import utils.pathUtils as pathUtils
from entities.credentials import Credentials

if __name__ == "__main__":
    credentials = Credentials()
    path = credentials.root_directory
    folderConvertor.run_command_on_files(path, "pandoc", "-s -t html -o ", ".html")
    path_index = path+ os.sep +"index.html"
    fileUtils.copy_resources(pathUtils.get_runtime_script_path() + os.sep + "resources", path + os.sep + "resources", [".css", ".png"])
    folderStructureGenerator.generate_html_file(path, path_index)
    ftp.upload_files(path, [".html", ".css", ".png"])
    fileUtils.delete_files(path, [".html", ".css", ".png"])