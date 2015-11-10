import sys
import psycopg2
import form_sql
from tqdm import tqdm


class ConnectToDb(object):

    name_db = None
    user_db = None
    password_db = None

    def __init__(self, name_db, user_db, password_db, **kwargs):
        self.name_db = name_db
        self.user_db = user_db
        self.password_db = password_db
        self.connect_to_db()

    def connect_to_db(self):
        try:
            connet_to_db = psycopg2.connect(database=self.name_db, user=self.user_db, password=self.password_db)
            print connet_to_db
            cr = connet_to_db.cursor()
            tqdm(cr.execute(form_sql.query_update))
            if cr:
                print "\n", self.name_db, "is updated"
            connet_to_db.commit()
        except Exception, a:
            print a
        finally:
            cr.close()
            connet_to_db.close()
