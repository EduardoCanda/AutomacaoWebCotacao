import time
import automatizacao_web as web

from selenium import webdriver

TEMPO = 0.4


def executar():
    print('Carregando execução...')
    print()

    print('[                     ] %00')
    time.sleep(TEMPO)

    print('[=====                ] %25')
    time.sleep(TEMPO)

    print('[==========           ] %50')
    time.sleep(TEMPO)

    print('[===============      ] %75')
    time.sleep(TEMPO)

    print('[=====================] %100')
    time.sleep(TEMPO)

    print()
    web.obter_cotacoes(webdriver.Edge())


if __name__ == '__main__':
    executar()
