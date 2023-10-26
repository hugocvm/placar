from mongoengine import Document, DictField,DateTimeField
from datetime import datetime

class Gol (Document):
    data_hora = DateTimeField(default=datetime.now)
    jogador = DictField()
    partida = DictField()
    