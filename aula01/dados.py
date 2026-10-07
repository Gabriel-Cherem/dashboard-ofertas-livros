"""Leitura dos arquivos CSV do projeto.
"""

from pathlib import Path
import csv

# Pasta onde este arquivo .py está. Assim o programa encontra o CSV
# mesmo quando é executado a partir de outra pasta (como no Streamlit Cloud).
PASTA = Path(__file__).parent
CAMINHO_LIVROS = PASTA / "livros.csv"


def ler_livros():
    arquivo = None
    livros = []
    try:
        with open("livros.csv", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                livros.append(linha)       
    except FileNotFoundError: 
        print("O arquivo livro não foi encontrado!! ")
    except Exception as Error:
        print("Ocorreu algum erro na leitura do arquivo!!", Error)
    finally:
        if arquivo is not None:
            arquivo.close()


livros = ler_livros()
print(f"A quantidade de livros da coleção é de {len(livros)} livros. ")


if __name__ == "__main__":
    livros = ler_livros()
    print(f"A quantidade de livros da coleção é de {len(livros)} livros. ")

