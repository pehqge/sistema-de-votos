import os
from Candidato import Candidato
Candidato1 = Candidato("jose")
Canditado2 = Candidato("maria")
Candidato3 = Candidato("joao")

candidatos = [Candidato1, Canditado2, Candidato3]
candidato = [candidato for candidato in candidatos if candidato == "jose"]
print(sorted(os.listdir('votos')))
