import pandas as pd
import yaml
import os

def criar_usuario():
    arquivo = "/home/dayvisonprogramas/Projetos-python/Aulas-Enderson/dados.yaml"
    if not os.path.exists(arquivo):
        with open(arquivo, "w") as file:
            file.write("usuarios\n")


    
    nome = input("Nome: ")
    idade = input("Idade: ")
    nasc = input('Data de Nascimento: ')
    interesses = []
    while True:
        interesse = input("Interesses: ")
        interesses.append(interesse)
        perg = input("Outro interesse? [s/n]: ").upper().strip()
        if perg != "S":
            break
        

    dados = {
        "nome": nome,
        "idade": idade,
        "data de nascimento": nasc,
        "interesses": interesses  
    }    

    with open(arquivo, "r") as file:
        dados = yaml.safe_load(file) or {}

    if "usuarios" in dados:
        dados["usuarios"].append(dados)
    else:
        dados["usuarios"] = [dados]

    with open(arquivo, "w") as file:
        yaml.dump(dados, file, default_flow_style=False)
    
    


criar_usuario()


# import os

# if os.path.exists("Projetos-python/Aulas-Enderson/nova_pasta"):
#     os.rmdir("Projetos-python/Aulas-Enderson/nova_pasta")
#     print("Arquivo removido...")
# else:
#     print('Arquivo não existe...')

