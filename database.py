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

