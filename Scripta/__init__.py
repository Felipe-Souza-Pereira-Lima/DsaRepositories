from time import sleep, strftime
from os import startfile, system
import socket

__version__ = '1.0.4'
__package__ = 'Scripta'
__language__ = 'Português (Brasil)'

# Inicia o código
Class Scripta:
    def __init__():
        pass
# Escreva na tela
    def echo(text):
        print(text)
# Adiciona mais cmmandos na linha
    def additions(code):
        code
# Conecta com servidor IPV4\TCP
    def connect_to(ip, port):
        try:
            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c.connect(ip, port)
        except:
            print('Erro ao conectar!')
        else:
            print(f'Conectado com sucesso a IP: [{ip}] Porta: [{port}]')
# Cria servidor socket IPV4\TCP
    def server_init(ip, port, listen):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((ip, port))
            s.listen(listen)
        except:
            print('Erro ao criar o servidor!')
        else:
            print('Servidor criado com sucesso!')
            s.accept()
# Executa comandos do sistema
    def command(systemcommand):
        system(systemcommand)
        pass
# Esperar
    def wait(seconds):
        try:
            sleep(seconds)
        except:
            raise TypeError('não é possivel esperar strings ou TrueValues\n')
# Executa programas .exe
    def exe(filelocal):
        try:
           startfile(filelocal)
        except:
            print('Esse programa não existe!')
        else:
            print(f'{filelocal} Foi iniciado!')
# Condição rapida
    def maybe(comparador, repositorio, SeTrue, SeFalse):
        if comparador == repositorio:
            SeTrue
        else:
            SeFalse
# abre e escreve algo em um arquivo
    def open_write(to_open, str, mode='a'):
        with open(to_open, '') as f:
            write(f, str)
# Tentar de uma linha
    def trying(tentar, mensagem_de_erro):
        try:
            tentar
        except:
             print(mensagem_de_erro)
