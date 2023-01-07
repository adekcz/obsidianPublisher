#load password and username from file
import utils
from ftplib import FTP


def load_credentials():
    with open("src/resources/credentials.txt") as file:
        lines = file.readlines()
        username = lines[0].strip()
        password = lines[1].strip()
        ftp = lines[2].strip()
    return username, password, ftp

#upload file to ftp
def upload_file(file_path):
    username, password, ftp_path = load_credentials()
    ftp = FTP(ftp_path)
    ftp.login(username, password)
    #upload file
    with open(file_path, "rb") as file:
        ftp_path = utils.remove_prefix(file_path, "D:\\temp\\obsidian test\\")
        ftp.storbinary("STOR " + ftp_path, file)
    ftp.quit()
