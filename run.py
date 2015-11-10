#!/usr/bin/env python

import sys
import psycopg2
import form_sql
from params import params_connect
from connect_to_db import ConnectToDb


class Main(object):

    connect_to_db = ConnectToDb

    def __init__(self):
        param = params_connect()
        if param.file_d:
            get_params = param.get_params_to_db()
            name_db = get_params.get('db_name')
            user_db = get_params.get('db_user')
            password_db = get_params.get('db_password')
            self.success_connect(name_db, user_db, password_db)
        else:
            self.fail_param_connect(param)

    def success_connect(self, name_db, user_db, password_db, **kwargs):
        self.connect_to_db(name_db=name_db, user_db=user_db, password_db=password_db)
        return True

    def fail_param_connect(self, **kwargs):
            quest = raw_input("Config file didn't set! Would you like search config file in current directory?[y/n]")
            if quest.lower() == 'y':
                files = kwargs.get('param').find_file()
                if files:
                    print "Found %s config files" % (len(files))
                    for i in files:
                        print list(files).index(i), files[i]
                    set_file = int(raw_input("Please set file that you want to use (for example enter '1')"))
                    while set_file not in files.keys():
                        set_file = int(raw_input("Please write correct value!"))
                    kwargs.get('param').set_file_d(files.get(set_file))
                    self.connect_to_db.connect_to_db(name_db=kwargs.get('param').params_to_db['name_db'],
                                                     user_db=kwargs.get('param').params_to_db['user_db'],
                                                     password_db=kwargs.get('param').params_to_db['password_db'])
                else:
                    print "Files not found"


if __name__ == '__main__':
    Main()
