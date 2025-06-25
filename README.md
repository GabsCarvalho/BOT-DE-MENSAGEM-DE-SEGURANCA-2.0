# Bot de Envio Automático de Mensagens no WhatsApp Web

Este projeto é um **bot automatizado** que utiliza **Selenium** para enviar mensagens no WhatsApp Web em horários programados, de forma automática e personalizada para diferentes contatos ou grupos.

---

## Funcionalidades

* Envio de mensagens pré-definidas para um ou mais contatos/grupos no WhatsApp Web.
* Seleção aleatória de mensagens por contato.
* Abertura automática do navegador com login persistente (sem necessidade de escanear o QR Code a cada execução).
* Execução agendada diária (ex: às 08:00).
* Limpeza do campo de busca antes de cada envio.
* Encerramento automático do navegador ao final da rotina.

---

##  Tecnologias e Bibliotecas

* [Python 3](https://www.python.org/)
* [Selenium](https://selenium-python.readthedocs.io/)
* [webdriver-manager](https://pypi.org/project/webdriver-manager/)
* [schedule](https://pypi.org/project/schedule/)

---

##  Pré-requisitos

* Google Chrome instalado.
* Conta ativa no WhatsApp Web previamente logada no Chrome.
* Python instalado com as bibliotecas abaixo:

```bash
pip install selenium webdriver-manager schedule
```

---

##  Como usar

1. **Clone ou baixe este repositório.**

2. **Edite os seguintes dados no código:**

```python
Contatos1 = ['NOME EXATO DO CONTATO OU GRUPO 1']
Contatos2 = ['NOME EXATO DO CONTATO OU GRUPO 2']

mensagens = {
    "APELIDO CONTATO 1": ["mensagem 1", "mensagem 2"],
    "APELIDO CONTATO 2": ["mensagem 3", "mensagem 4"]
}

mensagem = random.choice(mensagens["APELIDO CONTATO 2"]) #ENVIA A MENSAGEM DE FORMA ALEATÓRIA
mensagem = random.choice(mensagens["APELIDO CONTATO 1"]) #ENVIA A MENSAGEM DE FORMA ALEATÓRIA
```

3. **Execute o script:**

```bash
python nome_do_arquivo.py
```

4. O bot irá abrir o WhatsApp Web às 08:00 todos os dias, buscar os contatos definidos e enviar mensagens aleatórias entre as opções fornecidas.

---

## Agendamento

O envio está agendado para:

```python
schedule.every().day.at("08:00:00").do(executar)
```

Altere o horário conforme necessário.

---

## Observações

* O bot usa o Chrome com seu perfil de usuário padrão. Isso evita a necessidade de escanear o QR code a cada execução.
* O caminho para o perfil do Chrome é definido automaticamente com:

```python
options.add_argument(f"user-data-dir={APPDATA}\\AppData\\Local\\Google\\Chrome\\User Data\\Default") #Caso seu sistema esteja em outro idioma ou estrutura de pastas, ajuste este caminho.
```
* Recomenda-se que transforme o arquivo em executavel e coloque para iniciar junto do computador, evitando a necessidade de ativação diária.
* Futuramente será adicionado uma interface gráfica para melhor controle das funcionalidades.


