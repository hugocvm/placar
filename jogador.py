from equipe import Equipe

 

class Jogador:
    
    
    def __init__(self, nome):
        self.nome = nome
        
    def info_jogador(self):
        print(f'Nome: {self.nome}')   

    def to_json(self):
        return {'nome': self.nome}
    


        
        
# time = Time('Vasco')
# jogador = Jogador('Hugo', 29) 
# time.adicionar_jogador(jogador)

# for jogador in time.lista_jogadores:
#     print(jogador.nome)
# # jogador.info_jogador()

