# Profº André Tinassi - Sistemas Operacionais
# João Pedro Neigri Heleno 
# Trabalho 2 - Simulador do escalonador Round Robin

from typing import Deque, Any
from collections import deque
import sys

#------------------------------------------------------------------------
# Funções

def roundRobin(quantum, cursor):

    backup = quantum
    tempo = 0
    controle = True
    
    # Cria fila com os processos
    queue: Deque[Any] = deque()
    queue.append(0)

    while(controle):

        # Organiza a lista de acordo com a ordem de chegada
        if tempo == listaChegada[cursor] and cursor < len(listaProcessos) :
            queue.append(cursor)
            if cursor < (len(listaProcessos) - 1):
                cursor = cursor + 1

        if quantum == backup and listaTempo[queue[0]] == listaTempoBackup[queue[0]]:
            vetTempoInicio.append(tempo)

        if listaTempo[queue[0]] > 0 and quantum > 0:

            listaTempo[queue[0]] = listaTempo[queue[0]] - 1
            tempo = tempo + 1
            quantum = quantum - 1

        elif listaTempo[queue[0]] == 0:
            print(" |-----", listaProcessos[queue[0]], "-----|", tempo, end = "")
            
            vetTempoFim[queue[0]] = tempo
            
            queue.popleft()
            quantum = backup

        else: 
            print(" |-----", listaProcessos[queue[0]], " -----|", tempo, "", end = "")
            aux = queue.popleft()
            queue.append(aux)
            quantum = backup

        # Verifica se todos os processos foram executados

        cont = 0

        for i in range(len(listaProcessos)):
            cont = cont + listaTempo[i]

        if cont == 0:
            controle = False       
       
    vetTempoFim[queue[0]] = tempo   
    print(" |-----", listaProcessos[queue[0]], "-----|", tempo)
    queue.popleft()

def cabecalho():
    for i in range(len(listaProcessos)):
        print(listaProcessos[i], end = ' ')
    print('\n')

#------------------------------------------------------------------------
# Main

# Leitura do arquivo de 
fileInput = open(sys.argv[1], 'r')

listaProcessos = fileInput.readline()
listaTempo = fileInput.readline()
listaChegada = fileInput.readline()
listaPrioridade = fileInput.readline()

# Tratamento vetor
listaProcessos = listaProcessos.split(' ')
listaTempo = listaTempo.split(' ')
listaChegada = listaChegada.split(' ')
listaPrioridade = listaPrioridade.split(' ')

listaProcessos.pop(0)
listaTempo.pop(0)
listaChegada.pop(0)
listaPrioridade.pop(0)
listaProcessos[-1] = listaProcessos[-1].strip('\n')
listaChegada[-1] = listaChegada[-1].strip('\n')

listaTempoBackup = listaTempo[:]
vetTempoInicio = []
vetTempoFim = listaProcessos[:]

for i in range(len(listaTempo)):
    listaTempo[i] = int(listaTempo[i])
    listaChegada[i] = int(listaChegada[i])
    listaTempoBackup[i] = int(listaTempoBackup[i])

print("Processos na Fila do First Come First Served: ")
cabecalho()

print("Tempo de CPU requerida pelos processos: ")
print(listaTempo, '\n')

print("Tempo de Chegada dos processos: ")
print(listaChegada, '\n')

roundRobin(5, 1)

print('\n')
cabecalho()

somaInicio = 0
somaFim = 0

for i in range(len(vetTempoInicio)):
    print(vetTempoInicio[i] - listaChegada[i], end =' ')
    somaInicio = somaInicio + vetTempoInicio[i] - listaChegada[i]

print('\n')
cabecalho()

for j in range(len(vetTempoFim)):
    vetTempoFim[j] = vetTempoFim[j] - listaChegada[j]

print(vetTempoFim)

for i in range(len(vetTempoFim)):
    somaFim = somaFim + vetTempoFim[i]

print("Tempo Médio de Resposta: ", somaFim/len(listaProcessos))
print("Tempo Médio de Espera: ", somaInicio/len(listaProcessos))
#------------------------------------------------------------------------