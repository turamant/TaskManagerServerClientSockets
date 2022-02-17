from datetime import datetime


class Server:
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

        def server_uptaime(self):
            now = datetime.now()
            uptime = str(now - self.start_time)
            return uptime[:-7]

        # HANDLERS
        def show_server_info(self, *args, **kwargs):
            return "info", f"{self.version} | created: {self.created}"

        def show_server_commands(self, *args, **kwargs):
            return "help", self.commands

        def connection_closed(self, *args, conn):
            self.send_msg(conn, "CONNECTION CLOSED")
            print("CONNECTION CLOSED")

