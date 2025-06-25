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

Contatos1 = ['⛑ Segurança EPD-MS ⛑']
Contatos2 = ['Adm/Escritório/SST🗂⚡']

mensagens = {
    "campo": [
        "Senhores, bom dia! \nUse sempre os EPIs — sua segurança vem em primeiro lugar! \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nNão existe serviço tão urgente que não possa ser feito com segurança.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nCarro limpo e organizado é ambiente seguro.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nNão corra riscos desnecessários. Pare e pense!  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nComunique situações de risco — prevenir é sempre o melhor caminho.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nA pressa é inimiga da segurança. Faça com calma e atenção.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nVerifique seus equipamentos antes de iniciar o trabalho.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nTrabalhe com foco: sua vida vale mais que qualquer tarefa.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nSegurança é um valor. Pratique todos os dias!  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nSua atitude segura protege você e quem está ao seu lado.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nMantenha distância segura de veículos em movimento.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nEm caso de acidente, comunique imediatamente!  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nNão arrisque! Afinal, você é a ferramenta mais importante da empresa.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nUse o trabalho para cuidar da sua família e não para se afastar.   \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nNão esqueçam de se hidratar.   \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nUm segundo de descuido pode custar uma vida inteira\nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nA prevenção é a melhor forma de proteção\nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nSegurança começa com você!\nÓtimo dia para todos",
        "Senhores, bom dia! \nEPI não é enfeite. Use corretamente!\nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
        "Senhores, bom dia! \nTrabalhar seguro é um sinal de inteligência. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nNão espere um acidente acontecer para mudar sua postura. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nUm ambiente seguro é um ambiente produtivo. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nLembre-se de reportar qualquer risco identificado. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nPrevenir é um ato de respeito com os colegas. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nA maioria dos acidentes são causados por comportamento inseguro, então não se esqueça de sempre agir com segurança. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nO corpo dá sinais: se está cansado ou não está bem, pare e comunique. Sua segurança em primeiro lugar \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nNão se esqueça dos 5s. Então separe o essencial do desnecessário e elimine o que não é necessário. Deixe seu carro organizado, afinal, ele é seu ambiente de trabalho principal. Mantenha seu carro limpo. Crie padrões para organização e limpeza.\n E sempre se lembre de manter a disciplina, seguindo os padrões e promovendo organização e limpeza, isso pode ajudar a melhorar sua saúde. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nVocê voltar para casa no fim do dia sempre vai ser a meta mais importante. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nA vida não tem botão de reinício. Previna-se. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nTrabalho seguro é sinal de profissionalismo. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nPequenas ações fazem grandes diferenças na segurança. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nNegligência é o caminho mais rápido para um acidente. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nNão se arrisque, siga o procedimento! \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nSegurança não combina com improviso. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nUm acidente pode ter consequências para toda a vida. Tome cuidado. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nNão corra riscos, trabalhe com consciência. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nDireção defensiva é uma técnica de condução que visa evitar acidentes, mesmo diante de ações incorretas de outros motoristas e condições adversas da estrada. Envolve a antecipação de situações perigosas e a adoção de medidas para minimizar riscos.\nNão se esqueça disso, pode salvar sua vida e a de outras pessoas. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nA segurança é individual, mas o impacto é coletivo. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nResponsabilidade se pratica, não se terceiriza. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nFaça certo, mesmo quando ninguém está olhando. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nA cultura de segurança começa com pequenos hábitos e cuidados. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nFale! Segurança também se constrói com diálogo. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nNenhuma meta é mais importante que sua vida. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nIsso pode salvar sua vida: \nA identificação de riscos é o processo de identificar, reconhecer e descrever riscos ou oportunidades que possam afetar os objetivos de uma organização ou projeto. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nUma cultura de segurança, com a participação ativa de todos, é essencial para garantir a prevenção de acidentes e doenças ocupacionais. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nA segurança do trabalho não se limita à prevenção de acidentes, mas também inclui a promoção da saúde e do bem-estar de todos \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nA cultura de prevenção é um conjunto de valores, crenças e comportamentos que promovem a segurança e a saúde no trabalho. Faça também a sua parte! \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
        "Senhores, bom dia! \nA participação ativa dos trabalhadores no processo de segurança é fundamental para garantir que as medidas de segurança sejam eficazes e que haja uma cultura de prevenção. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos"
    ],
    "adm": [
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nEvite que o corpo pague o preço dos seus descuidos. Mantenha-se atento à postura, à altura da tela e ao apoio dos pés, seus pés devem tocar o chão e seus joelhos formarem um ângulo de 90°. Isso evita dores nas costas e nas pernas. Pequenas correções fazem grande diferença ao longo dos dias. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nCuidado ao andar olhando o celular. Atenção ao ambiente! \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nRelaxe os olhos: a cada 20 minutos, olhe para longe por 20 segundos. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nTrabalhar sentado não é sinônimo de conforto se você ignora a ergonomia. Uma cadeira mal regulada hoje pode se tornar uma dor crônica amanhã. Ajuste, cuide e se movimente. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nLembre-se... Pequenas pausas ao longo do dia reduzem o estresse e aumentam a produtividade. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nNão se esqueça... Não ignore sentimentos persistentes de ansiedade ou tristeza — saúde mental também é prioridade. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nUm ambiente seguro é aquele em que as pessoas se respeitam, se escutam e se apoiam. A segurança emocional é tão necessária quanto a física. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nLembre-se, pode te ajudar! Respire fundo por 1 minuto. Essa simples técnica reduz a frequência cardíaca e alivia a tensão. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nMantenha uma garrafinha de água na mesa — a desidratação causa fadiga e dor de cabeça. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nAproveite o horário de almoço para caminhar ou tomar sol, vitamina D e movimento em um só tempo. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nOrganizar sua rotina com consciência evita que o trabalho invada sua vida pessoal. Cultivar limites saudáveis é sinal de respeito consigo mesmo. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nSe alimente em horários regulares e evite trabalhar durante as refeições. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nDormir bem melhora a tomada de decisão, concentração e humor no trabalho. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nCuriosidade: a maioria dos acidentes em escritórios ocorre por tropeços, escorregões e quedas. Cuidado ao andar! \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nFalar com respeito, ouvir com atenção e agir com empatia são práticas que constroem ambientes saudáveis — e protegem a saúde mental de todos. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nCuidar da saúde emocional é tão importante quanto cumprir prazos. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nTrabalhar com outras pessoas exige mais do que saber fazer: exige saber conviver. Conflitos evitáveis começam onde a empatia termina. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nOrganização reduz o estresse. Comece o dia revisando prioridades. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nA água que você esquece de tomar, o alongamento que você adia e o sono que você sacrifica hoje… serão as dores e os cansaços de amanhã. Cuide de si no presente. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nUma pausa para o café pode ser também um momento de socialização e descanso mental. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nBeba ao menos 2 litros de água por dia, mesmo no ar-condicionado. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nA correria do dia a dia pode nos fazer esquecer que o descanso também é parte do trabalho. Pausar, respirar e se cuidar é um investimento — não um atraso. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nCuriosidade: caminhar 15 minutos por dia já reduz o risco de doenças cardíacas. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nCuide de você fora do trabalho também, sono, alimentação e lazer fazem parte da saúde ocupacional. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nCuriosidade: Boa parte dos acidentes de escritório envolvem quedas de mesma altura. Cuidado! \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nPromover uma cultura de segurança é mais do que seguir normas — é construir um ambiente onde o bem-estar coletivo é prioridade. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nFale com sua liderança se estiver enfrentando dificuldades emocionais ou físicas. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nO ambiente ideal de trabalho é aquele onde você se sente seguro física e emocionalmente. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nNão se esqueça dos 5s. Então separe o essencial do desnecessário e elimine o que não é necessário. Deixe sua estação de trabalho organizada. Mantenha sua mesa e sala limpa. Crie padrões para organização e limpeza.\nE sempre se lembre de manter a disciplina, seguindo os padrões e promovendo organização e limpeza, isso pode ajudar a melhorar sua saúde e a dos seus colegas. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nA cultura de prevenção é um conjunto de valores, crenças e comportamentos que promovem a segurança e a saúde no trabalho. Faça também a sua parte! \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nSegurança não se resume a acidentes graves. É também evitar tropeços, quedas, curtos-circuitos e situações que, por descuido, podem se tornar sérias. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nA participação ativa dos trabalhadores no processo de segurança é fundamental para garantir que as medidas de segurança sejam eficazes e que haja uma cultura de prevenção. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nO corpo dá sinais: se está cansado ou não está bem, pare e comunique. Sua segurança em primeiro lugar \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nA produtividade verdadeira não nasce da pressa, mas do equilíbrio entre esforço, foco e bem-estar. Seu corpo e sua mente precisam de pausas para entregar o melhor. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nSabe onde está o extintor de incêndio mais próximo? Segurança começa com informação. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nEvite multitarefas exageradas. Concentre-se em uma coisa por vez para fazer bem feito. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nRespirar fundo, tomar água e se alongar são ações simples com grande impacto. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nDesconectar é parte do processo: respeite seus horários fora do expediente. Cuidar de você é parte do trabalho. Não negligencie seu bem-estar.\nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nMuitas lesões não surgem de grandes impactos, mas da repetição de pequenos erros ao longo do tempo. Ergonomia é prevenção, não só conforto. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nO cuidado com o ambiente não é apenas uma questão de limpeza ou estética — é uma forma concreta de proteger você e seus colegas. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nPalavras têm impacto. Em um ambiente profissional, gentileza e clareza reduzem conflitos e aumentam a confiança da equipe. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nDelegar com responsabilidade, planejar com clareza e executar com foco são atitudes que aumentam a segurança, reduzem retrabalho e fortalecem a equipe. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nNão se afogue nas tarefas. Um bom planejamento é como um colete salva-vidas: evita que você se perca nas urgências e esqueça das prioridades. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nToda cultura de segurança começa na mente de quem acredita que pequenos cuidados constroem grandes proteções. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nA mudança de hábito mais poderosa começa com uma pergunta simples: 'isso está realmente seguro?' — e com a coragem de ajustar o que não está. \nÓtimo dia para todos",
        "Pessoal, bom dia! \nMensagem de segurança do dia: \nSegurança não é um obstáculo à produtividade — é o que garante que possamos continuar produzindo com qualidade e saúde por muito tempo. \nÓtimo dia para todos"
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
        mensagem = random.choice(mensagens["adm"])
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
        mensagem = random.choice(mensagens["campo"])
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