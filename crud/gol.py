from model.gol import Gol
from flask import Flask , jsonify, request




def listar_jogadores():
    return Gol.objects().only("autor","partida").all().to_json()

def incluir_gol(jogador, partida):
    Gol(jogador=jogador, partida=partida).save()
    return "Incluido com sucesso"

def editar_gol(gol):
    gol_alterado = request.get_json()
    for i, gol in enumerate(gol):
        if gol.get('id') == id:
            print (listar_jogadores())
        
            gol[i].update(gol_alterado)
            return jsonify(gol[i])
        
    
    