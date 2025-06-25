# Importar bibliotecas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service         # Para criar o serviço do ChromeDriver
from selenium.webdriver.chrome.options import Options         # Para configurar o navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from pathlib import Path
import random
import time
from datetime import datetime, timedelta
import schedule



#INFORMAÇÕES GERAIS

APPDATA = os.path.expanduser('~')

Contatos1 = ['GRUPO OU CONTATO']
Contatos2 = ['GRUPO OU CONTATO']

mensagens = {
    "APELIDO CONTATO 1": [
        "MENSAGEM OU MENSAGEM QUE DESEJA SER ENVIDA"
    ],
    "APELIDO CONTATO 2": [
        "MENSAGEM OU MENSAGEM QUE DESEJA SER ENVIDA"
    ]
}

def executar():
    
    options = Options()         # Configurar opções do navegador
    service = Service(ChromeDriverManager().install())          # Criar o serviço, usando o ChromeDriverManager para baixar o ChromeDriver certo
    options.add_argument(f"user-data-dir={APPDATA}\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

    # Navegar até o web whats
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://web.whatsapp.com/')
    time.sleep(40)

    # Deleta o contato anteriormente digitado
    def detele_contato():
        time.sleep(3)
        campo_de_texto = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        campo_de_texto.click()
        campo_de_texto.send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        campo_de_texto.send_keys(Keys.DELETE)
    
    def buscar_contato(contato):
        time.sleep(1)  # aguarda o WhatsApp carregar
        campo_pesquisa = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        time.sleep(3)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contato)
        time.sleep(1)
        campo_pesquisa.send_keys(Keys.ENTER)

    def enviar_mensagem(mensagem):
        try:
            # Buscar todos os campos contenteditable (textos onde se pode digitar)
            campos_editaveis = driver.find_elements(By.XPATH, '//div[@contenteditable="true"]')
            if not campos_editaveis:
                print("\nNenhum campo de digitação encontrado.")
                return

            campo_mensagem = campos_editaveis[-1]  # O último normalmente é o campo de digitação
            campo_mensagem.click()
            time.sleep(1)
            campo_mensagem.send_keys(mensagem)
            time.sleep(1)
            campo_mensagem.send_keys(Keys.ENTER)
            print("\nMensagem enviada com sucesso!")
        except NoSuchElementException:
            print("\nErro: campo de mensagem não encontrado.")
        except Exception as e:
            print(f"\nErro ao tentar enviar mensagem: {e}")

    #Juntando duplicados
    def delete_da_mensagem():
        print("\nDeletando mensagem")
        detele_contato()
        print("\nMensagem deletada")

    def fechando_navegador():
        print(f"\nFinalizando o sistema por hoje, até amanhã!")
        time.sleep(5) # Espera alguns segundos e fecha o navegador
        driver.quit()

    def envio_mensagem2():
        buscar_contato(Contatos2[0])
        mensagem = random.choice(mensagens["APELIDO CONTATO 2"]) #ENVIA A MENSAGEM DE FORMA ALEATÓRIA
        enviar_mensagem(mensagem)
        print(f"\nMensagem enviada ao grupo '{Contatos2}': {mensagem}")


    #Executa a automação
    print("\nAutomação iniciada para envio de mensagens de segurança no grupo.")

    if not Contatos1:
        print("Contatos1 está vazio. Verificando contato 2")

        if not Contatos2:
            print("Contatos2 está vazio. Finalizando o bot.")
            time.sleep(2)
            exit()
    
        else:
            envio_mensagem2()
            fechando_navegador()

    else:
        buscar_contato(Contatos1[0])
        mensagem = random.choice(mensagens["APELIDO CONTATO 1"]) #ENVIA A MENSAGEM DE FORMA ALEATÓRIA
        enviar_mensagem(mensagem)
        print(f"\nMensagem enviada ao grupo '{Contatos1}': {mensagem}")
        
    
        if not Contatos2:
            print("Contatos2 está vazio. Finalizando o bot.")
            fechando_navegador()
        
        else:
            delete_da_mensagem()
            envio_mensagem2()
            fechando_navegador()

schedule.every().day.at("08:00:00").do(executar)

while True:
    schedule.run_pending()
    time.sleep(20)
