from InquirerPy import prompt
from rich.progress import track
from rich.console import Console
from rich import print
from time import sleep
from os import system

def title(msg:str=''):
    linha = f"{'':-^50}"
    mensagem = f"{msg:^50}"
    print(linha)
    print(mensagem.upper())
    print(linha)

def barra_processo(msg=''):
    system('clear')
    print(msg)
    for i in track(range(100), description='Salvando...', style='#8d99ae'):
        sleep(.02)