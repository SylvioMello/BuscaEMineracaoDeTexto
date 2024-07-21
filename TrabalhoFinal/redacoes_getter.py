from pathlib import Path

def get_redacoes():
    dir_path = Path("TrabalhoFinal\\redacoes")
    redacoes = {}
    i = 0
    for txt_file in dir_path.glob("*.txt"):
        with txt_file.open('r', encoding='utf-8') as file:
            content = file.read()
            redacoes[txt_file.name] = content
            i+=1
            if i > 115:
                return redacoes