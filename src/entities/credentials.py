#object containing settings and credetials  for the application
class Credentials:
    def __init__(self):
        self.username = "admin"
        self.password = "admin"
        self.ftp = "webpage.com"
        self.load_credentials()


    def load_credentials(self):
        with open("src/resources/credentials.txt") as file:
            lines = file.readlines()
            self.username = lines[0].strip()
            self.password = lines[1].strip()
            self.ftp = lines[2].strip()

    def get_ftp_credentials(self):
        return self.username, self.password, self.ftp