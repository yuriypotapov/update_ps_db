#!/usr/bin/env python

from params import ParamsConnectToDb
from connect_to_db import ConnectToDb


class Main(ParamsConnectToDb, ConnectToDb):

    connect_to_db = ConnectToDb
    name_db = None
    user_db = None
    password_db = None

    def get_parameters(self):
        param = ParamsConnectToDb()
        if self.file_d:
            get_params = self.get_params_to_db()
            self.name_db = get_params.get('db_name')
            self.user_db = get_params.get('db_user')
            self.password_db = get_params.get('db_password')
            self.success_connect()
        else:
            try_agein = self.fail_get_param(param)
            if try_agein is not None:
                self.get_parameters()

    def success_connect(self, **kwargs):
        self.connect_to_db(name_db=self.name_db, user_db=self.user_db, password_db=self.password_db)
        return True

    def fail_get_param(self, params):
            quest = raw_input("Config file didn't set! Would you like search config file in current directory?[y/n]")
            if quest.lower() == 'y':
                files = self.find_file()
                if files:
                    print "Found %s config files" % (len(files))
                    for i in files:
                        print list(files).index(i), files[i]
                    set_file = int(raw_input("Please set file that you want to use (for example enter '1')"))
                    while set_file not in files.keys():
                        set_file = int(raw_input("Please write correct value!"))
                    self.set_file_d(files.get(set_file))
                    return True
                else:
                    print "Files not found"


if __name__ == '__main__':
    main = Main()
    main.get_parameters()
