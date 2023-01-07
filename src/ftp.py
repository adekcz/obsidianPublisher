#load password and username from file
from ftplib import FTP


def load_credentials():
    with open("credentials.txt") as file:
        lines = file.readlines()
        username = lines[0].strip()
        password = lines[1].strip()
        ftp = lines[2].strip()
    return username, password, ftp

#upload file to ftp
def upload_file(file_path, ftp_path):
    username, password, ftp = load_credentials()
    ftp = FTP(ftp)
    ftp.login(username, password)
    ftp.cwd