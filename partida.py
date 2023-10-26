
from equipe import Equipe
from datetime import datetime
from jogador import Jogador

class Partida: 
    time_visitante:Equipe ('visitante')
    time_mandante: Equipe ('mandante')
    
    placar_visitate = 0
    placar_mandante = 0
    
    data_inicio = None
    data_fim = None
    tempo_decorrido = None
    
    def __init__(self, time_mandante, time_visitante):
        self.time_mandante = time_mandante
        self.time_visitante = time_visitante
        
    def comecar_partida(self):
        self.data_inicio = datetime.now()
        
    def finalizar_partida(self):
        self.data_fim = datetime.now()
        self.tempo_decorrido = self.data_fim - self.data_inicio
     
        
    def adicionar_gol(self, jogador: Jogador):
        if not self.time_visitante.has_jogador(jogador) and not self.time_mandante.has_jogador(jogador):
            raise Exception("Jogador é invalido")
        
        print(self.time_visitante.has_jogador(jogador))
        if self.time_visitante.has_jogador(jogador):
            self.placar_visitate += 1
            return

        self.placar_mandante+=1
            
        
    
     
        
