from selenium import webdriver as web
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
import os
import pyautogui as g

options = Options()

# browser.find_element(By.ID, "endereco").send_keys("18078458")

nome_arquivo_cep = "C:\cep-correios\pesquisa_cep.xlsx"
planilha_dados = load_workbook(nome_arquivo_cep)
shet_selecionada = planilha_dados["CEP"]

browser = web.Chrome()
browser.get('https://buscacepinter.correios.com.br/app/endereco/index.php?t')

for linha in range(1, len(shet_selecionada['A']) + 1 ):
    cep = shet_selecionada['A%s' % linha].value
    if cep is not None:
        browser.find_element(By.NAME, "endereco").send_keys(cep)

        browser.find_element(By.NAME, 'btn_pesquisar').click()
        g.sleep(2)
        rua = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]')[0].text
        bairro = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[1]/td[2]')[0].text
        cidade = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr[1]/td[3]')[0].text
        cep = browser.find_elements(By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]')[0].text
        sheet_dados = planilha_dados["Dados"]
        linha_corrente = len(sheet_dados['A']) + 1

        colunaA = "A" + str(linha_corrente)
        colunaB = "B" + str(linha_corrente)
        colunaC = "C" + str(linha_corrente)
        colunaD = "D" + str(linha_corrente)

        sheet_dados[colunaA] = rua
        sheet_dados[colunaB] = bairro
        sheet_dados[colunaC] = cidade
        sheet_dados[colunaD] = cep
        g.sleep(2)
        browser.find_element(By.ID, 'btn_nbusca').click()

    if len(shet_selecionada['A']) == 1:
        break



planilha_dados.save(filename=nome_arquivo_cep)

os.startfile(nome_arquivo_cep)
