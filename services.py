from configparser import ConfigParser


def initialize_PostgresDB():
    print("PROD-db-postgres")
    config = ConfigParser()
    config.read("config.ini")




