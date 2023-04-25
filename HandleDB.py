import sqlite3


class QueryDb:

    def __init__(self):
        conn = sqlite3.connect(self.dbname)
        self.conn = conn
        c = conn.cursor()
        self.c = c
        pass

    def run(self):
        # todo: create decorator to handle exceptions: eg. table already exists
        self.c.execute()
        self.conn.commit()
        self.conn.close()
        pass

    def query_table(self):
        pass

    def create_table(self):

        fields = ', '.joiin([' '.join(field, field_type) for field, field_type in self.fields_dct.items()])
        return f"""CREATE TABLE {self.table} ({fields})""" # fields: field1 field1Type, field2 fiel2Type, ...

        pass

    def insert_data(self):
        data = ', '.join([i for i in self.data])
        return f"""INSERT INTO {self.table} VALUES ({data})"""  # todo: user (?, ?), (val1, val2) instead
                                                                # todo: or (:col1, :col2), {col1: val, col2:val}

    def delete_data(self):
        pass

    def drop_table(self):
        pass

    def read_data(self, table):
        columns = ', '.join([col for col in self.cols])
        return f"""SELECT {columns} FROM {table}"""

    def generate_view(self):
        pass

    def add_column(self):
        pass
