from mongoengine import Document, StringField, IntField

class Jogador(Document):
    nome = StringField()
    idade = IntField()
    gols = IntField(default= 0)  