from ftplib import FTP


class FTPManager:

    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.ftp = None

    def connect(self):
        self.ftp = FTP(self.host)
        self.ftp.login(self.user, self.password)

        print(f"[OK] Connecté à {self.host}")

    def list_files(self):
        files = self.ftp.nlst()

        for file in files:
            print(file)

    def disconnect(self):
        if self.ftp:
            self.ftp.quit()
            print("[OK] Déconnexion")

