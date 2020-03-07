from cryptography.fernet import Fernet
import os, sys


class Encryption():
    def get_key(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        config_dir = basedir + "/config"
        site_key_file = config_dir + "/siteKey"

        with open(site_key_file, 'rb') as f:
            counter = 0
            for line in f:
                counter += 1
                if counter > 1:
                    print("siteKey must contain only one single line.")
                    exit(1)
                line = line.strip()
                if line:
                    return line.decode('utf-8')

    def encrypt(self, to_encrypt):
        key = Encryption().get_key()
        f = Fernet(key)
        return f.encrypt(to_encrypt.encode())

    def decrypt(self, to_decrypt):
        key = Encryption().get_key()
        f = Fernet(key)
        return f.decrypt(to_decrypt).decode()


if __name__ == '__main__':
    print(Encryption().encrypt(sys.argv[1]))
