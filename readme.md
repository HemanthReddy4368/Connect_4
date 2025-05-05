# Connect 4 AI

THis Repository has the code for connect 4 game which is implemented in python using pygame library. In this project we will be developing AI agents that will play the game by implementing the below agents:

* **Minimax with Alpha-Beta Pruning:** It is A classic search algorithm which is best for two player games where it explores efficiently the game tree to find the best optimal move.
* **Q-Learning:** This is a reinforcement learning algorithm that will allow the agent to learn and experience.

## Technologies Used

* **Python:** We used pyhton as the main language in this project.
* **Pygame:**  For game design we are using the pygame library.

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/HemanthReddy4368/Connect_4.git
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the game**
    ```bash
    python main.py
    ```

## Implementation Roadmap

Our development will follow these steps:

1.  **Implement the core Connect 4 game logic:**
    * Creating the game board.
    * Implementing functions for dropping pieces, checking for valid moves, and detecting winning conditions.
    * Handling game state and turns.

2.  **Integrate Pygame for a graphical user interface:**
    * Visualizing the game board and pieces.
    * Handling user input (mouse clicks for dropping pieces).

3.  **Implement the Minimax algorithm with Alpha-Beta Pruning:**
    * Developing a function to evaluate the game state.
    * Implementing the recursive Minimax algorithm with alpha-beta pruning to optimize search.

4.  **Implement the Q-Learning algorithm:**
    * Defining the state space and action space for the Connect 4 game.
    * Creating a Q-table to store action-value pairs.
    * Implementing the Q-learning update rule.
    * Developing a training loop for the Q-learning agent.

5.  **Create different AI agents:**
    * Human player agent.
    * Random move agent (for baseline comparison).
    * Minimax/Alpha-Beta agent.
    * Q-learning agent.

6.  **Develop evaluation and testing mechanisms:**
    * Scripts to play different agents against each other.
    * Metrics to evaluate the performance of the AI agents.

## Contact

[Intro to AI Group 4]

---

**Let the AI Connect 4 battles begin!**