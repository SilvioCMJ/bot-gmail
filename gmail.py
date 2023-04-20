import pyautogui
import time

# aq vai preencher os dados essenciais

destino = "teste@gmail.com "
assunto = "teste123"
msg = "teste321"
navegador = "opera"


# abrindo navegador
pyautogui.press("win")
time.sleep(2)
pyautogui.write(navegador)
pyautogui.press("enter")
time.sleep(8)
pyautogui.write('https://mail.google.com/mail/u/0/#inbox')
time.sleep(30)

# madando email
pyautogui.click(x=90, y=150)
time.sleep(7)

pyautogui.write(destino)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write(assunto)

pyautogui.press('tab')
pyautogui.write(msg)
time.sleep(2)
pyautogui.hotkey('ctrl', 'enter')