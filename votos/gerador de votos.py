import os
import json
import random


def criador_arquivos(num_regioes, num_candidatos):
    # exclude all json files from the directory
    files = [file for file in os.listdir("votos") if file.endswith(".json")]
    for file in files:
        os.remove(os.path.join("votos", file))

    for i in range(num_regioes):
        # Generate a random number for the filename
        filename = f"{i+1:0{len(str(num_regioes))}d}.json"
        filepath = os.path.join("votos", filename)

        # Create a dictionary with 50 candidates and random vote counts
        candidates = {}
        for j in range(num_candidatos):
            candidate_name = f"Candidato {j+1}"
            vote_count = random.randint(0, 1000)
            candidates[candidate_name] = vote_count

        # Write the dictionary to a JSON file
        with open(filepath, "w") as f:
            json.dump(candidates, f)


criador_arquivos(10, 15)
