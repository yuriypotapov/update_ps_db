import sys
import psycopg2
from form_sql import FormSql
from tqdm import tqdm


class ConnectToDb(FormSql):

    name_db = None
    user_db = None
    password_db = None

    def __init__(self, name_db, user_db, password_db, **kwargs):
        self.name_db = name_db
        self.user_db = user_db
        self.password_db = password_db
        self.connect_to_db()

    def connect_to_db(self):
        connect_to_db = psycopg2.connect(database=self.name_db, user=self.user_db, password=self.password_db)
        print connect_to_db
        cr = connect_to_db.cursor()
        form_query = self.form_update_sql
        try:
            cr.execute(form_query())
            if cr:
                print "\n", self.name_db, "is updated"
            connect_to_db.commit()
        except Exception, a:
            print a
        finally:
            cr.close()
            connect_to_db.close()
