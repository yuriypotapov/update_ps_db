#!/usr/bin/env python

import sys
import psycopg2
import form_sql
from params import params_connect
from connect_to_db import ConnectToDb


class main():

    def connect(self):

        param = params_connect()
        connect_to_db = ConnectToDb()

        if param.file_d:
            connect_to_db.connect_to_db(name_db=param.params_to_db['name_db'],
                                    user_db=param.params_to_db['user_db'],
                                    password_db=param.params_to_db['password_db'])
        else:
            quest = raw_input("Config file didn't set! Would you like search config file in current directory?[y/n]")
            if quest.lower() == 'y':
                files = param.find_file()
                if files:
                    print "Found %s config files" % (len(files))
                    for i in files:
                        print list(files).index(i), files[i]
                    set_file = int(raw_input("Please set file that you want to use (for example enter '1')"))
                    while set_file not in files.keys():
                        set_file = int(raw_input("Please write correct value!"))
                    param.set_file_d(files.get(set_file))
                    connect_to_db.connect_to_db(name_db=param.params_to_db['name_db'],
                                            user_db=param.params_to_db['user_db'],
                                            password_db=param.params_to_db['password_db'])
                else:
                    print "Files not found"
        return True

if __name__ == '__main__':
    main().connect()
