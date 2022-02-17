from datetime import datetime

from users import User


class Server:
    @staticmethod
    def send_msg(conn, msg, coder="utf-8"):
        conn.send(msg.encode(coder))

    @staticmethod
    def recv_msg(conn, buffer=1024, coder="utf-8"):
        return conn.recv(buffer).decode(coder)

    @staticmethod
    def server_created_date():
        dt = datetime.now()
        dt = dt.strftime("%d/%m/%Y %H:%M:%S")
        return dt

    def __init__(self):
        self.created = Server.server_created_date()
        self.start_time = datetime.now()
        self.commands = {
            "help": "commands list with short description",
            "uptime": "return server life time",
            "info": "info about server version, server created date",
            "send": "send direct message to another user",
            "read": "read messages from box",
            "clear": "delete all messages from box",
            "stop": "connection closed (end client / server)",
            "reset": "reset user password (ADMIN ONLY)",
            "create": "create new user (ADMIN ONLY)",
            "delete": "remove user from database (ADMIN ONLY)",
        }
        self.handlers = {
            "info": self.show_server_info,
            "help": self.show_server_commands,
            "uptime": self.show_server_uptime,
            "create": self.create_new_user,
            "delete": self.delete_user,
            "reset": self.reset_password,
            "send": self.send_msg_to_user,
            "read": self.read_msg_box,
            "clear": self.clear_user_box,
            "stop": self.connection_closed,
        }

        def server_uptime(self):
            now = datetime.now()
            uptime = str(now - self.start_time)
            return uptime[:-7]

        # LOGIN
        def create_user(self, data):
            userdata = data.split(":")
            if len(userdata) == 3 and userdata[2].upper() in ["USER", "ADMIN"]:
                return User(userdata[0], userdata[1], userdata[2])
            return None

        # HANDLERS
        def show_server_info(self, *args, **kwargs):
            return "info", f"{self.version} | created: {self.created}"

        def show_server_commands(self, *args, **kwargs):
            return "help", self.commands

        def connection_closed(self, *args, conn):
            self.send_msg(conn, "CONNECTION CLOSED")
            print("CONNECTION CLOSED")

        def show_server_uptime(self, *args, **kwargs):
            return "uptime", self.server_uptaime()

        def create_new_user(self, db, logged_user, conn):
            if logged_user.rights == "ADMIN":
                self.send_msg(conn, "Create: Enter -> username:password:rights")
                recv = self.recv_msg(conn)
                user = self.create_user(recv)

                if user:
                    if db.add_user_to_DB(user.get_user_data()):
                        print("DataBase updated:" + "\n", db.show_data("SELECT * FROM users"))
                        return user.username, user.password
                    return "ERROR", f"{user.username} EXISTS !"
                else:
                    return "ERROR", "Invalid data"
            return "ERROR", "Permission denied"



