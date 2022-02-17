from database import DataBase

from configparser import ConfigParser


def initialize_PostgresDB():
    config = ConfigParser()
    config.read("config.ini")

    db = DataBase(
        config["DATABASE"]["db_user"],
        config["DATABASE"]["password"],
        config["DATABASE"]["host"],
        config["DATABASE"]["port"],
        config["DATABASE"]["database"],
    )
    return db


