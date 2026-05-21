import interface
from time import sleep


agenda = list()
tarefa = dict()

def iniciar(segundos):
    while segundos > 0:
        print(f"\rTempo restante: {segundos:02d}", end="")
        sleep(1)
        segundos -= 1
    print("\rTempo esgotado!            ")

def adicionar_tarefa():

    tarefa['Titulo'] = input('Titulo: ')
    x = interface.leiaint('Quanto tempo dessa tarefa: ')
    tarefa['Tempo'] = x
    while True:
        formato = input('Segundo, Minuto ou Hora? [S/M/H] ').strip().upper()
        if formato == 'S':
            if x > 1:
                tarefa['Formato'] = 'Segundos'
            else:
                tarefa['Formato'] = 'Segundo'
            break
        elif formato == 'M':
            if x > 1:
                tarefa['Formato'] = 'Minutos'
            else:
                tarefa['Formato'] = 'Minuto'
            break
        elif formato == 'H':
            if x > 1:
                tarefa['Formato'] = 'Horas'
            else:
                tarefa['Formato'] = 'Hora'
            break
        else:
            print('Erro no formato de tempo!')

    agenda.append(tarefa)
    print(tarefa)

def ver_tarefas():
    print('=' * 42)
    print('Tarefas')
    print('=' * 42)
    if len(agenda) == 0:
        print('Nenhuma tarefa encontrada!')
    else:
        print(f'\n{"Titulo":^5} {"Tempo":>10} {"Formato":>10}')
        print('=====================================')
        for k, v in enumerate(agenda):
            print(f"{v['Titulo']:^5} {v['Tempo']:>10} {v['Formato']:>10}")
        print()

def sair():
    print('Saindo do Sistema...')
    sleep(1)
    print(f'\n{"<<< Volte Sempre >>>":^42}')
    print('=' * 42)
    exit()

def iniciar_tarefa():
    print()
    print('=' * 42)
    print('Tarefas')
    print('=' * 42)
    if len(agenda) == 0:
        print('Nenhuma tarefa encontrada!')
    else:
        print(f'\n{"ID":^5} {"Titulo":>5} {"Tempo":>10} {"Formato":>10}')
        print('=====================================')
        for k, v in enumerate(agenda):
            segundos = 0
            print(f"{k:^5} {v['Titulo']:>5} {v['Tempo']:>10} {v['Formato']:>10}")
            resp = str(input("\nQual o id da tarefa: ")).strip()
            resp = int(resp)
            if k == resp:
                if v['Formato'] == 'Segundos' or v['Formato'] == 'Segundo':
                    segundos = v['Tempo']
                elif v['Formato'] == 'Minutos' or v['Formato'] == 'Minuto':
                    segundos = v['Tempo'] * 60
                elif v['Formato'] == 'Horas' or v['Formato'] == 'Hora':
                    segundos = (v['Tempo'] * 60) * 60
                while segundos > 0:
                    print(f"\rTempo restante: {segundos:02d}", end="")
                    sleep(1)
                    segundos -= 1
                print("\rTempo esgotado!            ")
            else:
                print('Erro: Tarefa não encontrada!')