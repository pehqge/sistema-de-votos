import os
import json
from Candidato import Candidato
from Regiao import Regiao


class Controller:
    def __init__(self):
        self.__regioes = []
        self.__candidatos = []

    # funcao que le os arquivos json e cria as regioes

    def computa_regioes(self, path_pasta):
        arquivos = sorted([arquivo for arquivo in os.listdir(
            path_pasta) if arquivo.endswith('.json')]) # lista de arquivos json

        for arquivo in arquivos:
            with open(os.path.join(path_pasta, arquivo), 'r') as f:  # abre o arquivo
                votos = json.load(f) # carrega o dicionario de votos em "votos"
                # se a regiao nao estiver na lista de regioes
                if not arquivo[:-5] in self.__regioes:
                    # cria uma nova regiao
                    self.__regioes.append(Regiao(arquivo[:-5], votos))
                else:
                    # atualiza os votos da regiao existente
                    self.__regioes[self.__regioes.index(
                        arquivo[:-5])].atualiza_votos(votos) 
        self.computa_candidatos()

    # funcao que cria os candidatos e computa os votos de cada um pelas regioes existentes
    def computa_candidatos(self):
        for regiao in self.__regioes:
            for candidato, voto in regiao.votos.items():
                try:
                    self.__candidatos[self.__candidatos.index(
                        candidato)].computa_voto(regiao.nome, voto)  # computa o voto do candidato se caso ele já estiver na região
                except ValueError: # caso ele não exista ainda, cria um novo candidato e computa os votos dele
                    cand_temp = Candidato(candidato)
                    self.__candidatos.append(cand_temp)
                    cand_temp.computa_voto(regiao.nome, voto)
                    
    def reset(self):
        self.__candidatos = []
        self.__regioes = []

    @property
    def candidatos(self):
        return self.__candidatos

    @property
    def regioes(self):
        return self.__regioes


controle = Controller()
controle.computa_regioes('votos')

print({candidato.nome: candidato.total for candidato in controle.candidatos})
print({regiao.nome: regiao.total for regiao in controle.regioes})
