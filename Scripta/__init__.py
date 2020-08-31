from time import sleep, strftime
from os import startfile, system
import socket

__version__ = '1.0.2'

def init():
    pass
def migrateWarnings(Warnings):
    for i in Warnings:
        if i is not None:
            return i
        else:
            continue
    else:
        return False
def echo(text):
    print(text)
    pass
def additions(code):
    code
def connect_to(ip, port):
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect(ip, port)
    except:
        print('Erro ao conectar!')
    else:
        print(f'Conectado com sucesso a IP: [{ip}] Porta: [{port}]')
def server_init(ip, port, listen):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen(listen)
    except:
        print('Erro ao criar o servidor!')
    else:
        print('Servidor criado com sucesso!')
def command(systemcommand):
    system(systemcommand)
def wait(seconds):
    try:
        sleep(seconds)
    except:
        print('TypeError não é possivel esperar strings ou TrueValues\n')
def exe(filelocal):
    try:
        startfile(filelocal)
    except:
        print('Esse programa não existe!')
    else:
        print(f'{filelocal} Foi iniciado!')
class string(str):
    pass
class numberint(int):
    pass
class numberfloat(float):
    pass
class TrueValues(bool):
    pass
