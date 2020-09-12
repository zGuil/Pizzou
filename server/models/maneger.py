from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from __init__ import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/pizzou'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100))
    preco_atual = db.Column(db.Float())
    nome = db.Column(db.String(45))
    qtd = db.Column(db.Float())
        
    def get():
        produtos = Produto.query.all()
        return produtos

    def set(body):
        produto = Produto(descricao=body['descricao'], preco_atual=body['preco_atual'],
                          nome=body["nome"], qtd=body['qtd'])
        db.session.add(produto)
        db.session.commit()

        return "OK"


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(12))
    full_name = db.Column(db.String(255))

    def get_users():
        users = Users.query.all()
        return users


if __name__ == '__main__':
    manager.run()