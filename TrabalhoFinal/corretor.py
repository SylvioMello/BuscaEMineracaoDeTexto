from openai import OpenAI
from redacoes_getter import get_redacoes
from pathlib import Path
client = OpenAI()

def save_correcao(filename, correcao):
    dir_path = Path("TrabalhoFinal\\correcoes")
    dir_path.mkdir(parents=True, exist_ok=True)
    filename = f'{filename}-corrigida.txt'
    file_path = dir_path / filename
    with file_path.open('w', encoding='utf-8') as f:
        f.write(correcao)

def corrige(redacao, filename):
    contexto =  ((Path("TrabalhoFinal\\prompts") / 'contexto.txt').open('r', encoding='utf-8')).read()
    content =  ((Path("TrabalhoFinal\\prompts") / 'content.txt').open('r', encoding='utf-8')).read()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": contexto},
            {"role": "user", "content": f'{content} {redacao}' }
        ]
    )
    correcao = completion.choices[0].message.content
    save_correcao(filename, correcao)


redacoes = get_redacoes()
for filename, texto in redacoes.items():
    corrige(texto, filename)