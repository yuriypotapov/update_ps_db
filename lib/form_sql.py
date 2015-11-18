from parse_xml import ParseXml


class FormSql(ParseXml):

    default_query = ""

    @staticmethod
    def set_query(key=None, table={}):
        for field, value in table[key].iteritems():
            print "Set %s in %s field \n" % (value, field)
        res = ', '.join("%s = '%s'" % (field, value) for field, value in table[key].iteritems())
        return res

    @staticmethod
    def set_sql_query(table_name, where, fields):
        query = "UPDATE %s SET %s" % (table_name, fields)
        if where:
            query += "WHERE %s" % where
        return query

    def form_update_sql(self):
        main_query = ''
        for table in self.parse_all():
            fields = self.set_query('fields', table)
            where = self.set_query('where', table)
            table_name = table['table']['name']
            main_query += self.set_sql_query(table_name, where, fields) + ";"
        return main_query