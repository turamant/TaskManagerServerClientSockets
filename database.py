import psycopg2
from tabulate import tabulate


class DataBase:
    def __init__(self, db_user, password, host, port, database):
        self.db_user = db_user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.connection = psycopg2.connect(
            user=self.db_user,
            password=self.password,
            host=self.host,
            port=self.port,
            database=self.database,
        )

        def show_data(self, query):
            with self.connection:
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    records = cursor.fetchall()
                    headers = [head[0] for head in cursor.description]
                    table = tabulate(records, headers, tablefmt="psql")
                    return table

        def get_user(self, username):
            """return user tuple if user exists"""
            with self.connection:
                with self.connection.cursor() as cursor:
                    query = "SELECT * FROM users WHERE username = %s"
                    cursor.execute(query, (username,))
                    record = cursor.fetchone()
                    print(cursor.statusmessage)
                    return record

        def add_user_to_DB(self):
            pass

        def delete_user_from_DB(self):
            pass

        def send_direct_msg(self):
            pass

        def read_msg_box(self):
            pass

