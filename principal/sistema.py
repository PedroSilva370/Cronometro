import interface
import funcoes

# ENTRADA
while True:
    resposta = interface.menu(['Iniciar cronometro', 'Adicionar tarefa', 'Ver Tarefas', 'Iniciar Tarefa', 'Sair do Sistema'])
    if resposta == 1:
        resp = interface.leiaint('Tempo do cronometro: [s] ')
        funcoes.iniciar(resp)

    elif resposta == 2:
        funcoes.adicionar_tarefa()

    elif resposta == 3:
        funcoes.ver_tarefas()

    elif resposta == 4:
        funcoes.iniciar_tarefa()

    elif resposta == 5:
        funcoes.sair()

    else:
        print('Você digitou a opção errada.')