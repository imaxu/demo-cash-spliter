# coding=utf-8

from flask import Flask


''' create app from config  '''

app = Flask(__name__, static_folder = "./templates/static")

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['DEBUG'] = True


from .mods.chaifen import chaifen as chaifen_blueprint
app.register_blueprint(chaifen_blueprint)




def main():
    app.run(host='0.0.0.0', debug=True, port=80)

if __name__ == '__main__':
    main()