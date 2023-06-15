import pyautogui
from time import sleep

dia_hoje = input('Que dia é hoje: ex: 00/00/0000 ')

icone_navegador = (504,739)
campo_busca = (558,52)
link = (231,306)
escrever_email = (104,213)
docente_email = (913,301)
assunto_email = (754,359)
enviar_email = (787,682)
email_docente = 'luciene.etec@gmail.com'
termo_de_busca = 'Login Gmail'


pyautogui.moveTo(icone_navegador, duration=2)
pyautogui.sleep(1)
pyautogui.click()
pyautogui.sleep(4.5)

#Busca pelo o canal

pyautogui.moveTo(campo_busca,duration=2)
sleep(0.5)
pyautogui.typewrite(termo_de_busca,0.3)
pyautogui.sleep(1)
pyautogui.press('enter')

#Acessar o resultado

pyautogui.sleep(2)
pyautogui.moveTo(link,duration=2)
pyautogui.sleep(5)
pyautogui.click()

#escrever email

pyautogui.moveTo(escrever_email, duration=2)
sleep(2.5)
pyautogui.click()
sleep(2.5)
pyautogui.moveTo(docente_email, duration=2)
sleep(2.5)
pyautogui.typewrite(email_docente,0.3)
sleep(2.5)
pyautogui.hotkey('enter')
sleep(2.5)
pyautogui.moveTo(assunto_email, duration=2)
sleep(1.5)
pyautogui.click()
sleep(2)
pyautogui.typewrite(f'Aula do dia {dia_hoje}',0.3)
sleep(2)
pyautogui.hotkey('ctrl' + 'enter')
sleep(1.5)
pyautogui.hotkey('enter')
sleep(1)
pyautogui.moveTo(enviar_email, duration=1.5)
sleep(1.7)
pyautogui.click()
sleep(0.7)
print("Email enviado com sucesso!")

