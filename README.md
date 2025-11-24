##📘 README (PT-BR)
Navegação em Labirinto com Q-Learning

Este projeto implementa um agente capaz de navegar em um labirinto 2D utilizando o algoritmo Q-Learning, considerando tanto ambientes estáticos quanto ambientes dinâmicos, que podem incluir:

NPCs móveis que se deslocam de forma imprevisível

Portas que se abrem e fecham em ciclos

Obstáculos fixos e paredes

Estados compostos por posição e fase do ambiente

O objetivo é treinar o agente para encontrar a saída do labirinto com o menor número possível de passos, aprendendo por tentativa e erro por meio de recompensas e penalidades.

#🚀 Características do Projeto

Ambiente desenvolvido em Python utilizando matriz 2D

Agente treinado com Q-Learning (representação tabular)

Três cenários de avaliação:

Labirinto estático

Labirinto com NPCs móveis

Labirinto com portas dinâmicas

Métricas analisadas: recompensa média, passos, taxa de sucesso

Gráficos de desempenho e convergência

Fácil adaptação para ambientes maiores ou outros tipos de agentes

#🧠 Tecnologias Utilizadas

Python 3

NumPy

Matplotlib

Ambiente de execução: Google Colab / VS Code

#▶️ Como Executar

Instale as dependências:

pip install numpy matplotlib


Execute o arquivo principal:

python main.py


Os gráficos e métricas serão salvos na pasta results/.

#📌 Possíveis Extensões

Substituir Q-Table por Deep Q-Learning

Criar ambientes maiores e com mais dinâmica

Adicionar múltiplos agentes

Incluir sensores ou percepção parcial

#📄 Licença

Este projeto pode ser utilizado para fins acadêmicos ou experimentação pessoal.

---

##📘 README (EN)
Maze Navigation using Q-Learning

This project implements an intelligent agent capable of navigating a 2D maze using the Q-Learning reinforcement learning algorithm. The environment includes both static and dynamic elements such as:

Moving NPCs acting as unpredictable obstacles

Doors that open and close in timed cycles

Fixed walls and barriers

State representation including agent position and environment phase

The goal is to train the agent to reach the maze exit using the fewest possible steps, learning through trial and error based on rewards and penalties.

#🚀 Project Features

2D grid environment implemented in Python

Q-Learning agent with tabular representation

Three evaluation scenarios:

Static maze

Maze with moving NPCs

Maze with dynamic doors

Performance metrics: average reward, number of steps, success rate

Training and convergence plots

Modular structure for easy extension

#🧠 Technologies

Python 3

NumPy

Matplotlib

Development environment: Google Colab / VS Code

#▶️ How to Run

Install dependencies:

pip install numpy matplotlib


Run the main file:

python main.py


Output graphs and performance logs will be saved in the results/ folder.

#📌 Potential Extensions

Replace Q-Table with Deep Q-Learning

Expand to larger and more complex mazes

Add multi-agent interactions

Include partial observability or sensor models

#📄 License

This project is free for academic use and experimentation.
