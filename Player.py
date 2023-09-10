import numpy as np
import pickle

BOARD_ROWS = 3
BOARD_COLS = 3

class Learning_Player:
    def __init__(self, name, exp_rate=0.3):
        self.name = name
        self.states = []  # record all positions taken
        self.lr = 0.2
        self.exp_rate = exp_rate
        self.decay_gamma = 0.9
        # self.states_value = {}  # state -> value
        self.q_table = {}  # state -> action values

    def anneal_exp_rate(self):
        self.exp_rate *=0.99

    def getHash(self, board):
        boardHash = str(board.reshape(BOARD_COLS * BOARD_ROWS))
        return boardHash

    def chooseAction(self, positions, current_board, symbol):
        if np.random.uniform(0, 1) <= self.exp_rate:
            # take a random action
            idx = np.random.choice(len(positions))
            action = positions[idx]
        else:
            value_max = -999
            action = None  # Initialize action to None
            for p in positions:
                next_board = current_board.copy()
                next_board[p] = symbol
                next_boardHash = self.getHash(next_board)
                if self.q_table.get(next_boardHash) is not None:
                    value = self.q_table[next_boardHash]
                    if value >= value_max:
                        value_max = value
                        action = p
            # If action is still None, choose a random action
            if action is None:
                idx = np.random.choice(len(positions))
                action = positions[idx]
        return action

    # append a hash state

    def addState(self, state):
        self.states.append(state)

    def feedReward(self, reward):
        target = reward
        for state in reversed(self.states):
            if self.q_table.get(state) is None:
                self.q_table[state] = 0
            self.q_table[state] += self.lr * (target - self.q_table[state])
            target = self.q_table[state] * self.decay_gamma

    def reset(self):
        self.states = []

    def savePolicy(self):
        fw = open('policy_' + str(self.name), 'wb')
        pickle.dump(self.q_table, fw)
        fw.close()

    def loadPolicy(self, file):
        fr = open(file, 'rb')
        self.q_table = pickle.load(fr)
        fr.close()


class Human_Player:
    def __init__(self, name):
        self.name = name

    def chooseAction(self, positions):
        while True:
            row = int(input("Input your action row:"))
            col = int(input("Input your action col:"))
            action = (row, col)
            if action in positions:
                return action

    # append a hash state
    def addState(self, state):
        pass

    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        pass

    def reset(self):
        pass

class Random_Player:
    def __init__(self, name):
        self.name = name

    def chooseAction(self, positions):
        idx = np.random.choice(len(positions))
        action = positions[idx]
        return action

    # append a hash state
    def addState(self, state):
        pass

    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        pass

    def reset(self):
        pass
