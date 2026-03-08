# REQUISITOS PARA A MINHA AUTOMAÇÃO
  
# Passo 1: Entrar no sistema da empresa
# Paaso 2: Fazer login
# Passo 3: abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos

# python -m pip install pyautogui

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

import time
import pyautogui
import pandas
pyautogui.PAUSE = 0.3
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# abrir o navegador (chrome)

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Passo 1: Abrir o Chrome já na página de login para o Mack

# subprocess.Popen(["open", "-na", "Google Chrome", "--args", "--new-window", link])
# time.sleep(3)


# Passo 2: Fazer login
# pyautogui.click(x=685, y=451)
pyautogui.click(x=723, y=436)
pyautogui.write("pythonimpressionador@gmail.com", interval=0.05)
pyautogui.press("tab") # passar para o proxímo campo
pyautogui.write("sua senha", interval=0.05)
pyautogui.press("tab") # passar para o proxímo campo
pyautogui.press("enter") # passar para o proxímo campo
time.sleep(4)

# Passo 3: Importar a base de produtos
# python -m pip install pandas openpyxl

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4 e 5: Cadastrar os produtos em loop
for linha in tabela.index:
    pyautogui.click(x=653, y=294)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo),)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]),)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]),)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]),)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]),)
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]),)
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs),)
    
    pyautogui.press("tab")
    pyautogui.press("enter")

     # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

print("Todos os produtos cadastrados!")