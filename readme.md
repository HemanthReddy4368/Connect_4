# Connect 4 AI

[![How to Create a Connect Four AI (YouTube)](https://img.youtube.com/vi/Ut3PJblmce8/0.jpg)](https://www.youtube.com/watch?v=Ut3PJblmce8)

This repository contains the code for a Connect 4 game implemented in Python using the Pygame library. In this project, we develop AI agents to play the game by implementing the following agents:

*   **Minimax with Alpha-Beta Pruning:** A classic search algorithm ideal for two-player games, efficiently exploring the game tree to find the optimal move.
*   **Q-Learning:** A reinforcement learning algorithm that enables the agent to learn through experience.

* Link to Download The q-table and use it in the project: https://drive.google.com/file/d/1_EHU972TG3tZV8eLM073zStsG0wQxw_Q/view?usp=sharing

* Link To the explanation video: https://www.youtube.com/watch?v=Ut3PJblmce8

## Technologies Used

*   **Python:** The main programming language for this project.
*   **Pygame:** Used for game design and graphical interface.

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/HemanthReddy4368/Connect_4.git
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the game:**

    ```bash
    python main.py
    ```

## Implementation Roadmap

Our development will follow these steps:

1.  **Implement the core Connect 4 game logic:**

    *   Create the game board.
    *   Implement functions for dropping pieces, checking for valid moves, and detecting winning conditions.
    *   Handle game state and turns.

2.  **Integrate Pygame for a graphical user interface:**

    *   Visualize the game board and pieces.
    *   Handle user input (mouse clicks for dropping pieces).

3.  **Implement the Minimax algorithm with Alpha-Beta Pruning:**

    *   Develop a function to evaluate the game state.
    *   Implement the recursive Minimax algorithm with alpha-beta pruning to optimize search.

4.  **Implement the Q-Learning algorithm:**

    *   Define the state space and action space for Connect 4.
    *   Create a Q-table to store action-value pairs.
    *   Implement the Q-learning update rule.
    *   Develop a training loop for the Q-learning agent.

5.  **Create different AI agents:**

    *   Random move agent (human-like, for baseline comparison).
    *   Minimax/Alpha-Beta agent.
    *   Q-learning agent.

6.  **Develop evaluation and testing mechanisms:**

    *   Scripts to play different agents against each other.
    *   Metrics to evaluate the performance of the AI agents.

## Conclusion
Based on our experiments, The MiniMax Agent outperforms both Q-learning and random move (human like agent). This is mainly because Minimax with alpha beta pruning explores the games's state space strategically. It is evaluating potential moves by looking at several steps ahead and choosing the best path which maximizes the chances of winning and also minimizing the opponents chances.

The Q-learning agent, while showing promising learning behavior, requires extensive training to achieve competitive performance. The current implementation was trained for 300,000 episodes, which allowed it to learn basic game strategies and avoid obvious pitfalls. However, the complexity of Connect 4's state space means that even after this many episodes, the Q-table may not fully represent optimal strategies for all possible game scenarios.

To further enhance the Q-learning agent, several improvements can be considered:

* Extended Training: Increasing the number of training episodes to several million could allow the agent to explore a more comprehensive set of game states and refine its Q-table values.

* Deep Q-Learning: Implementing a deep Q-network (DQN) can address the limitations of the Q-table approach. DQNs use neural networks to approximate the Q-function, allowing the agent to generalize from observed states to unseen states. This can significantly improve the agent's performance in complex environments like Connect 4.

In summary, while the Minimax agent provides a strong baseline for Connect 4 AI, the Q-learning agent offers a pathway for continuous learning and improvement. Future work will focus on implementing deep Q-learning techniques to create a more adaptive and competitive AI for Connect

## Contact

[Intro to AI Group 4]

---

**Let the AI Connect 4 battles begin!**