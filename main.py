from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pyautogui as g
enderecos = []
options = Options()
# Importando o elemento By

browser = web.Chrome()
browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')
browser.find_element(By.NAME, "endereco").send_keys("18078458")
# browser.find_element(By.ID, "endereco").send_keys("18078458")
browser.find_element(By.NAME, "btn_pesquisar").click()
g.sleep(4)
rua = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[2]/td[1]')[0].text
print(rua)
g.sleep(30)
