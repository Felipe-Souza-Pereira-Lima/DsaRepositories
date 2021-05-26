from time import sleep
from os import startfile, system, chdir, getcwd



# Imprimir mensage na tela e usar time.sleep
def echo_delay(mensage, time=1):
    print(mensage)
    sleep(time)

# Só imprime na tela
def echo_(mensage):
    print(mensage)
    

# Extrutura condicional executavel
def condition(Comp_A, Comp_B, SeSim, SeNao):
    if Comp_A == Comp_B:
        print(SeSim)
    else:
        print(SeNao)


# Localização PATH da pasta
def path():
    return getcwd()

# Navegação entre pastas rapida
def cd_(folder=""):
    if folder == "":
        chdir("..")
    else:
        chdir(folder)

# Rapidos comandos
def shell(comando):
    system(comando)

# Iniciando aplicativo
def start(apps):
    startfile(apps)

