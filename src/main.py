# -*- coding: utf-8 -*-
import os
import fileStructureGenerator
import folderConvertor
import ftp
import utils

if __name__ == "__main__":
    path = "D:\\Dropbox\\Apps\\Obsidian\\Public\\www"
    folderConvertor.run_command_on_files(path, "pandoc", "-s -t html -o ", ".html")
    path_index = path+ os.sep +"index.html"
    runtime_path_css = utils.get_script_path() + os.sep + "resources" + os.sep+ "styles.css"
    path_css = path + os.sep + "styles.css"
    utils.copy_file(runtime_path_css, path_css)
    fileStructureGenerator.generate_html_file(path, path_index)
    ftp.upload_files(path)
    folderConvertor.delete_files(path, [".html", ".css"])