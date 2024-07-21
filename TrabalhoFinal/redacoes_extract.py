import nltk
nltk.download('punkt')
import uol_redacoes_xml
from pathlib import Path

essays = uol_redacoes_xml.load()
e = essays[0].text
for index, essay in enumerate(essays):
    dir_path = Path(f"TrabalhoFinal\\redacoes")
    dir_path.mkdir(parents=True, exist_ok=True)
    filename = f'redacao-{index}.txt'
    file_path = dir_path / filename
    with file_path.open('w', encoding='utf-8') as f:
        f.write(essay.text)
