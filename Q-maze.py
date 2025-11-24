import numpy as np
import random
import time
#import matplotlib.pyplot as plt

# Configurações do ambiente
LINHAS, COLUNAS = 10, 14
PORTAS = [(4, 6), (2, 9)]      # posições das portas dinâmicas
NPCS = [(3, 5), (6, 10)]       # posições iniciais dos NPCs móveis
PAREDES = [(1, 1), (1, 2), (2, 2), (4, 4), (7, 8), (8, 3)]  # paredes fixas
SAIDA = (9, 13)                # posição final (meta)
INICIO = (0, 0)                # posição inicial do agente

CICLO_PORTA = 5                # intervalo de tempo para alternância das portas


# Parâmetros do Q-Learning
ALPHA = 0.1    # taxa de aprendizado
GAMMA = 0.9    # fator de desconto
EPSILON = 0.2  # taxa de exploração inicial
DECAY = 0.995  # fator de decaimento de exploração
EPISODIOS = 800

ACOES = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# Criação da Q-Table como dicionário
Q = {}


# Funções auxiliares
def estado_atual(agente, tempo, npcs):
    """
    Representa o estado do ambiente como uma tupla:
    (posição do agente, fase da porta, posições dos NPCs).
    """
    fase_porta = (tempo // CICLO_PORTA) % 2  # alterna entre 0 (fechada) e 1 (aberta)
    return (agente[0], agente[1], fase_porta, tuple(npcs))

def mover_agente(pos, acao):
    """Retorna a nova posição do agente conforme a ação tomada."""
    x, y = pos
    if acao == 'UP':
        x = max(0, x - 1)
    elif acao == 'DOWN':
        x = min(LINHAS - 1, x + 1)
    elif acao == 'LEFT':
        y = max(0, y - 1)
    elif acao == 'RIGHT':
        y = min(COLUNAS - 1, y + 1)
    return (x, y)

def mover_npcs(npcs):
    """Atualiza aleatoriamente a posição dos NPCs móveis."""
    novas_pos = []
    for npc in npcs:
        direcao = random.choice(ACOES)
        novo = mover_agente(npc, direcao)
        novas_pos.append(novo)
    return novas_pos

def recompensa(agente, npcs, portas_abertas):
    """
    Define a função de recompensa do ambiente.
    Penaliza passos, colisões e concede bônus ao alcançar a saída.
    """
    if agente == SAIDA:
        return 200
    if agente in PAREDES:
        return -5
    if agente in npcs:
        return -50
    if agente in PORTAS and agente not in portas_abertas:
        return -5
    return -1

def melhor_acao(estado):
    """Retorna a ação com maior valor Q para o estado atual."""
    if estado not in Q:
        Q[estado] = np.zeros(len(ACOES))
    return np.argmax(Q[estado])


# Loop principal de treinamento
for episodio in range(EPISODIOS):
    agente = INICIO
    npcs = NPCS.copy()
    tempo = 0
    total_recompensa = 0

    for passo in range(300):  # limite de passos por episódio
        estado = estado_atual(agente, tempo, npcs)
        if estado not in Q:
            Q[estado] = np.zeros(len(ACOES))

        # Política ε-greedy: explora ou explora
        if random.random() < EPSILON:
            acao = random.randint(0, len(ACOES) - 1)
        else:
            acao = melhor_acao(estado)

        nova_pos = mover_agente(agente, ACOES[acao])

        # Atualiza NPCs e portas
        npcs = mover_npcs(npcs)
        fase_porta = (tempo // CICLO_PORTA) % 2
        portas_abertas = PORTAS if fase_porta == 1 else []

        r = recompensa(nova_pos, npcs, portas_abertas)
        total_recompensa += r

        novo_estado = estado_atual(nova_pos, tempo + 1, npcs)
        if novo_estado not in Q:
            Q[novo_estado] = np.zeros(len(ACOES))

        # Atualização da Q-Table (equação clássica do Q-Learning)
        Q[estado][acao] += ALPHA * (r + GAMMA * np.max(Q[novo_estado]) - Q[estado][acao])

        agente = nova_pos
        tempo += 1

        if agente == SAIDA:
            break

    # Decaimento progressivo da taxa de exploração
    EPSILON = max(0.01, EPSILON * DECAY)

    if (episodio + 1) % 100 == 0:
        print(f"Episódio {episodio + 1}: Recompensa total = {total_recompensa}")


# Avaliação do agente treinado
print("\nTreinamento concluído. Iniciando avaliação...\n")
agente = INICIO
npcs = NPCS.copy()
tempo = 0

for passo in range(100):
    estado = estado_atual(agente, tempo, npcs)
    acao = melhor_acao(estado)
    agente = mover_agente(agente, ACOES[acao])
    npcs = mover_npcs(npcs)

    fase_porta = (tempo // CICLO_PORTA) % 2
    portas_abertas = PORTAS if fase_porta == 1 else []

    print(f"Passo {passo + 1} | Agente: {agente} | Ação: {ACOES[acao]} | Portas {'Abertas' if portas_abertas else 'Fechadas'}")

    if agente == SAIDA:
        print("\n O agente alcançou a saída com sucesso!")
        break
    tempo += 1
    time.sleep(0.1)

print("\nExecução finalizada.")

