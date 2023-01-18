#load password and username from file
import utils
import os
from ftplib import FTP
from entities.credentials import Credentials

#upload file to ftp
def upload_file(file_path, file_name, connection):
    
    #upload file
    with open(file_path, "rb") as file:
        connection.storbinary("STOR " + file_name, file)
    

#go through all the files in the directory and upload them to ftp
def upload_files(root_directory):
    username, password, ftp_path = Credentials().get_ftp_credentials()
    ftp = FTP(ftp_path)
    ftp.login(username, password)
    for dir, dirs, files in os.walk(root_directory):
        current_dir = "/" + utils.remove_prefix(dir, root_directory)
        current_dir = current_dir.replace("\\", "/")
        ftp.cwd(current_dir)

        for dir_to_create in dirs:
            if dir_to_create in ftp.nlst():
                continue
            print("creating folder: " + dir_to_create)
            ftp.mkd(dir_to_create)

        for file in files:
            if file.endswith(".html") or file.endswith(".css"):
                file_path = os.path.join(dir, file)
                file_name = utils.get_file_name(file_path)
                if file_name in ftp.nlst():
                    print("deleting file: " + file_name)
                    ftp.delete(file_name)
                print("uploading file: " + file_name)
                upload_file(file_path, file_name, ftp)
    ftp.quit()