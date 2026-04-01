from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Jogador(BaseModel): 
    nome: str 
    idade: int 
    time: str

class Atualizajogador(BaseModel):
    nome: Optional[str] = None 
    idade : Optional[int] = None
    time: Optional[str] = None

app = FastAPI()



jogadores ={
    1: {
        'Nome': 'Messi',
        'Idade': '44', 
        'time': 'Barcelona'
    },

    2: {
        'Nome': 'Zico',
        'Idade': '45', 
        'time': 'Flamengo'
    }
}

#decorator 

@app.get('/')

def inicio():
    return jogadores


@app.get('/get-jogador/{jogador_id}')

def get_jogador(jogador_id: int):
    return jogadores[jogador_id]

@app.get('/get-jogador-time')

def get_jogador_time(time:str):
    for jogador_id in jogadores: 
        if jogadores[jogador_id]['time'] == time:
            return jogadores[jogador_id]
    return {'dados não encontrados'}


@app.post('/inserir-jogador/{jogador_id}')

def inserir_jogador(jogador_id: int, jogador: Jogador):
    if jogador_id in jogadores:
        return {'erro': 'jogador existente'}
    jogadores[jogador_id] = jogador
    return jogadores[jogador_id]


@app.put("/atualiza-jogador/{jogador_id}")

def atualiza_jogador(jogador_id: int, jogador:Atualizajogador):
    if jogador_id not in jogadores: 
        return {'erro':'jogador não existe' }
    if jogador.nome != None:
        jogadores[jogador_id]['nome'] = jogador.nome 
    if jogador.idade != None: 
        jogadores[jogador_id]['idade'] = jogador.idade
    if jogador.time != None:
        jogadores[jogador_id]['time'] = jogador.time 

    return jogadores[jogador_id]






@app.delete('/excluir-jogador/{jogador_id}')

def exclui_jogador(jogador_id: int): 
    if jogador_id not in jogadores:
        return {'erro': 'jogador não existe'}
    
    del jogadores[jogador_id]
    return {'mensagem': 'jogador excluído '}

