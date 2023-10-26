from flask import Flask , jsonify, request
from controller.jogador import incluir_jogador_controller, listar_jogadores_controller
from mongoengine import connect

from crud.gol import incluir_gol, listar_jogadores
from model.jogador import Jogador
from model.partida import Partida
import json
#jogadores = [Jogador]
app= Flask(__name__)

connect(host="mongodb+srv://hugovm41:Basehugo33@cluster0.ak9vwsj.mongodb.net/assistant")








@app.route('/jogadores',methods=['GET'])
def obter_jogadores():
    return jsonify(listar_jogadores_controller())



@app.route('/jogadores',methods=['POST'])
def inserir_jogadores():
    dados = request.json
    return jsonify(incluir_jogador_controller(dados))



app.run(port=3000,host='localhost')

