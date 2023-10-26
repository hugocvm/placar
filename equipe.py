
class Equipe: 
    
    def __init__(self, nome):
        self.nome = nome
    
    def info_equipe(self):
        print(f'Nome: {self.nome}')   

    def to_json(self):
        return {'nome': self.nome}  
        
    
       