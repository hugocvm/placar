from mongoengine import Document, IntField, DictField

class Partida(Document):
    duracao = IntField()
    equipe_visitante = DictField()
    equipe_mandante = DictField()
    placar_visitante = IntField(default=0)
    placar_mandante = IntField(default=0)