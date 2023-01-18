#object containing settings and credetials  for the application
class Credentials:
    def __init__(self):
        self.username = "admin"
        self.password = "admin"
        self.ftp = "webpage.com"
        self.root_directory = "/"
        self.load_from_file()


    def load_from_file(self):
        with open("src/resources/credentials.txt") as file:
            lines = file.readlines()
            self.username = lines[0].strip()
            self.password = lines[1].strip()
            self.ftp = lines[2].strip()
            self.root_directory = lines[3].strip()

    def get_ftp_credentials(self):
        return self.username, self.password, self.ftp