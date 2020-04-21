# coding=utf-8

from app import main
from flask_script import Manager, Server


app = main.app
manager = Manager(app)


def main():
    server = Server(host="0.0.0.0", port=8700, use_reloader=True, use_debugger=True)
    manager.add_command("dev", server)
    manager.run()

if __name__ == '__main__':
    main()