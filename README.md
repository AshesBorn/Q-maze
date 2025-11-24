# 🇧🇷 README – Português (Brasil)

## 🧠 Navegação em Labirinto com Q-Learning
Este projeto implementa um agente inteligente capaz de navegar em um labirinto 2D utilizando o algoritmo de Q-Learning. O ambiente inclui paredes fixas, NPCs móveis que se deslocam de forma aleatória e portas que alternam entre abertas e fechadas conforme o tempo, criando um cenário dinâmico e desafiador.

## 🎯 Objetivos do Projeto
- Criar um ambiente de labirinto com elementos estáticos e dinâmicos.
- Implementar Q-Learning para treinar um agente a encontrar a saída.
- Avaliar o desempenho do agente em cenários estático, com NPCs e com portas dinâmicas.
- Comparar as estratégias aprendidas.
- Identificar limitações e sugerir melhorias futuras.

## 🧩 Funcionalidades
- Grid 10x14 representado em matriz.
- Portas com ciclos de abertura/fechamento.
- NPCs móveis.
- Política ε-greedy com decaimento.
- Geração automática de gráficos.
- Armazenamento dos resultados.

## 🔧 Como Executar
pip install numpy matplotlib
python main.py

## 📊 Resultados
O sistema gera gráficos como:
- Recompensa média por episódio  
- Comparação entre cenários  
- Convergência do aprendizado  

## 🧭 Melhorias Futuras
- Testar Deep Q-Learning  
- Aumentar o tamanho do ambiente  
- NPCs com comportamento mais complexo  
- Introdução de visão parcial  

## 📚 Referências
- Sutton & Barto (2018) – Reinforcement Learning: An Introduction  
- Watkins (1989) – Learning from Delayed Rewards  

---

# 🇺🇸 README – English Version

## 🧠 Maze Navigation with Q-Learning
This project implements an intelligent agent capable of navigating a 2D maze using the Q-Learning algorithm. The environment includes fixed walls, randomly moving NPCs, and dynamic doors that open and close over time.

## 🎯 Project Goals
- Build a maze with static and dynamic elements.
- Train an agent using Q-Learning to reach the exit efficiently.
- Evaluate the agent under static, NPC-based, and dynamic-door scenarios.
- Compare learned strategies.
- Identify limitations and propose improvements.

## 🧩 Features
- 10x14 matrix-based grid  
- Dynamic doors with time cycles  
- Random NPC movement  
- ε-greedy policy with decay  
- Automatic performance graphs  
- Result logging and storage  

## 🔧 How to Run
pip install numpy matplotlib
python main.py

## 📊 Results
Generated figures include:
- Average reward per episode  
- Scenario comparison  
- Learning convergence  

## 🧭 Future Work
- Apply Deep Q-Learning  
- Expand maze dimensions  
- More advanced NPC behaviors  
- Add partial observability  

## 📚 References
- Sutton & Barto (2018) – Reinforcement Learning: An Introduction  
- Watkins (1989) – Learning from Delayed Rewards  
