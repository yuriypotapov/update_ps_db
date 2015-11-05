import ConfigParser
import sys
import glob, os
import settings
from tqdm import tqdm


class params_connect():

    config = ConfigParser.ConfigParser()
    file_d = ''
    files = {}
    params_to_db = {}

    def __init__(self):
        if '-c' in sys.argv:
            get_index_cfg_file = sys.argv.index('-c') + 1
            self.file_d = sys.argv[get_index_cfg_file]
            self.get_params_to_db()
        if '--help' in sys.argv:
            print settings.help_message
            quit()

    def get_params_to_db(self):
        self.config.read(self.file_d)
        name_db = self.config.get('options', 'db_name') if self.file_d else ''
        user_db = self.config.get('options', 'db_user') if self.file_d else ''
        password_db = self.config.get('options', 'db_password') if self.file_d else ''
        port_db = self.config.get('options', 'db_port') if self.file_d else ''

        value = {'name_db': name_db,
                 'user_db': user_db,
                 'password_db': password_db,
                 'port_db': port_db}
        self.params_to_db.update(value)

    def find_file(self):
        iterator = 0
        for file in tqdm(glob.glob("*.cfg")):
            self.files.update({iterator: file})
            iterator += 1
        return self.files

    def set_file_d(self, file):
        self.file_d = file
        self.get_params_to_db()
        return True

