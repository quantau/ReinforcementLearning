# Reinforcement Learning in Tic-Tac-Toe using Q-Learning 

Name: Harshit Singh                                                          Roll No: 2001CS29 

- **Libraries Used**: 
  - **NumPy**:  Used for numerical operations and array handling.
  - **TQDM**: Used for creating progress bars to monitor training progress. 
  - **Matplotlib**: Used for data visualization. 
- **Code Overview:** 
  - Key files in the code: Game.py, Player.py, State.py, Training.py. 
  - The **Game class** consists of methods that control the **flow of the game**, it updates the state after each move, informs the players whether game has ended or not.** 
  - The **Player file** has multiple classes depending on the type of player, it may be a **learning player,** a **random player** or **human player**. It also maintains the Q-table and uses it to decide its   next move and updates the Q-table based on the reward. 
  - The **State class stores information about the state** and has methods that give information about the state e.g. decide winner, legal moves available.  
  - The **Training class** simply trains two learning players against each other. 
- **Training**:  
  - The Q-learning agent underwent training in a simulated environment. 
  - The training process consisted of **50,000 episodes**. 
  - During training, the agent explored its environment with a **exploration rate of 0.3**. 
  - It utilized a **learning rate of 20% (0.2)**. 
  - The agent considered future rewards with a **discount factor of 90% (0.9).** 
  - The reward scheme applied was as follows: a **win** was associated with a **reward value of 1**, a **loss** with a **reward value of 0**, and a **draw** with a **reward value of 0.1.** 
- **Results:** 
  - After training, the agent's performance was evaluated in **5,000 game sessions**. 
  - These game sessions were **against** a **random player**, providing a benchmark for the agent's performance.  
  - It is evident from the data that the **trained model consistently** achieves either a **victory or a draw** when competing **against a randomly** acting opponent. 

![image](https://github.com/quantau/ReinforcementLearning/assets/75159365/27f79a29-a585-48f7-b882-afc42a73f39a)


- If somebody wants to play with the trained model then they should run the command *python .\Human\_Test.py* and will be  ![](Aspose.Words.69a0daf1-1702-481d-99fb-7b532c26b775.002.png)able to play with the trained model.  

![image](https://github.com/quantau/ReinforcementLearning/assets/75159365/4aa19079-b352-4d23-aa58-c83b5235c05e)

![image](https://github.com/quantau/ReinforcementLearning/assets/75159365/286ac454-7e3a-481b-8892-577b9756ef27)
