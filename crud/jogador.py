from model.jogador import Jogador




def listar_jogadores():
    return Jogador.objects().only("nome","idade","gols").all().to_json()

def incluir_jogador(nome, idade):
    Jogador(nome=nome, idade=idade, gols=0).save()
    return "Incluido com sucesso"
