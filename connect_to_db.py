import sys
import psycopg2
import form_sql
from tqdm import tqdm


class ConnectToDb(object):

    def connect_to_db(self, name_db=None, user_db=None, password_db=None, **kwargs):
        if name_db and user_db and password_db:
            connet_to_db = psycopg2.connect(database=name_db, user=user_db, password=password_db)
            print connet_to_db
            cr = connet_to_db.cursor()
            tqdm(cr.execute(form_sql.query_update))
            if cr:
                print "\n", name_db, "is updated"
            connet_to_db.commit()
            cr.close()
            connet_to_db.close()
            return True