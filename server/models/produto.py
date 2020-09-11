from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import hashlib 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/pizzou'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))
    preco_atual = db.Column(db.Float())
    

    def get_produtos():
        users = Users.query.all()
        return users


if __name__ == '__main__':
    manager.run()
