import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def obter_cotacoes(webdriver):
    time.sleep(4)
    print('Serviço de cotações em ação...')

    pesquisas_google = [
        'cotação dolar',
        'cotação euro'
    ]

    cotacoes = {}

    for pesquisa in pesquisas_google:
        print(f'Buscando {pesquisa}...')

        # Entrar no google
        webdriver.get('https://www.google.com/')

        # Pesquisar a cotação
        # Selecionar a barra de pesquisa do google
        webdriver.find_element(
            By.XPATH,
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
        ).send_keys(pesquisa)

        # Teclar enter
        webdriver.find_element(
            By.XPATH,
            '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
        ).send_keys(Keys.ENTER)

        # Pegar a cotação
        cotacao = webdriver.find_element(
            By.XPATH,
            '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
        ).get_attribute('data-value')

        cotacoes[pesquisa] = formatar_valor(cotacao)

        print('cotação extraída!')
        print()

    # cotacao ouro
    webdriver.get('https://www.melhorcambio.com/ouro-hoje')

    cotacao = webdriver.find_element(
        By.XPATH,
        '// *[ @ id = "comercial"]'
    ).get_attribute('value')

    print(f'Buscando cotação ouro...')

    cotacao = cotacao.replace(',', '.')

    cotacoes['cotação ouro'] = formatar_valor(cotacao)

    print('cotação extraída!')
    print()

    print(f'Cotações obtidas: {cotacoes}')

    webdriver.quit()

    return cotacoes


def formatar_valor(valor):
    return "{:.2f}".format(float(valor))
