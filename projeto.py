import pyautogui
import pandas
import openpyxl
import time 

pyautogui.PAUSE = 1.5 

#entrando dentro do site    
pyautogui.click(x=557, y=742)

pyautogui.write("chrome")

pyautogui.press("enter")

time.sleep(2)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)

pyautogui.press("enter")

pyautogui.click(x=442, y=378)

pyautogui.write("luizeduardo@gmail.com")

pyautogui.press("tab")

pyautogui.write("1234")

pyautogui.press("tab")

pyautogui.press("enter")

#inserindo os produtos

tabelas = pandas.read_csv("produtos.csv")

for linhas in tabelas.index:
    pyautogui.PAUSE = 1
    
    
    pyautogui.click(x=489, y=262)
    
    
    pyautogui.write(str(tabelas.loc[linhas, "codigo"]))
    pyautogui.scroll(-100)
    pyautogui.press("tab")

    
    pyautogui.write(str(tabelas.loc[linhas, "marca"]))
    pyautogui.scroll(-100)
    pyautogui.press("tab")

    
    pyautogui.write(str(tabelas.loc[linhas, "tipo"]))
    pyautogui.scroll(-100)
    pyautogui.press("tab")

    pyautogui.write(str(tabelas.loc[linhas, "categoria"]))
    pyautogui.scroll(-100)
    pyautogui.press("tab")

    pyautogui.write(str(tabelas.loc[linhas, "preco_unitario"]))
    pyautogui.scroll(-100)
    pyautogui.press("tab")

    pyautogui.write(str(tabelas.loc[linhas, "custo"]))

    pyautogui.press("tab")
    
    obs = str(tabelas.loc[linhas, "obs"])
    
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    
    pyautogui.press("enter")
    
    pyautogui.scroll(10000)

    
    






