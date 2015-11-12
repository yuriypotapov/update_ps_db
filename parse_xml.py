from xml.etree import ElementTree


class ParseXml(object):

    tables_with_all = []
    fields = {}
    _where = {}
    default_file = 'set_value_to_update.xml'

    def __init__(self, file_name=None):
        if file_name and '.xml' in file_name:
            self.default_file = file_name

    def get_xml_tree(self):
        try:
            with open(self.default_file, 'rt') as f:
                tree = ElementTree.parse(f)
            root = tree.getroot()
            return root
        except Exception, a:
            print a

    def parse_all(self):
        root = self.get_xml_tree()
        if root is not None:
            tables = self.parse_tables(root=root)
            for table in tables:
                equal = self.parse_equal(table=table)
                fields = self.parse_fields(table=table)
                self.tables_with_all.append({'table': table.attrib, 'fields': fields, 'where': equal})
        return self.tables_with_all

    def parse_tables(self, root):
        try:
            return root.findall('table')
        except Exception, a:
            print "Error 'table': Please set correct format: <table name='table'>[other parameters]</if>\n"

    def parse_equal(self, table):
        res = {}
        try:
            _where_name = table.find('if').attrib['name']
            _where_value = table.find('if').text
            res.update({_where_name: _where_value})
        except SyntaxError, a:
            print "Syntax error", a
        return res

    def parse_fields(self, table):
        res = {}
        try:
            for field in table.findall('field'):
                field_name = field.attrib['name']
                field_value = field.text
                res.update({field_name: field_value})
        except Exception, a:
            print a
        return res
