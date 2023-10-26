from crud.jogador import incluir_jogador, listar_jogadores

def incluir_jogador_controller(dados):
    nome = dados['nome']
    idade = dados['idade']
    
    if len(nome) < 3:
        return "nome invalido"
    
    incluir_jogador(nome, idade)
    
    
def listar_jogadores_controller():
    return listar_jogadores()