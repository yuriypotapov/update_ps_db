import ConfigParser
import sys
import glob, os
import settings
from tqdm import tqdm


class ParamsConnectToDb(object):

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
        value = {}
        try:
            for conf in self.config.sections():
                for opt in self.config.items(conf):
                    value.update({opt})
        except Exception, a:
            raise Exception(a)
        return value

    def find_file(self):
        iterator = 0
        for file in tqdm(glob.glob("*.cfg")):
            self.files.update({iterator: file})
            iterator += 1
        return self.files

    def set_file_d(self, _file):
        self.file_d = _file
