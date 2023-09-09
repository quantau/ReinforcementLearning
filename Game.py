from State import State
from tqdm import tqdm

class Game:
    def play(state, rounds=100):
        for i in tqdm(range(rounds)):
            while not state.isEnd:
                # Player 1
                positions = state.availablePositions()
                p1_action = state.p1.chooseAction(
                    positions, state.board, state.playerSymbol)
                # take action and upate board state
                state.updateState(p1_action)
                board_hash = state.getHash()
                state.p1.addState(board_hash)
                # check board status if it is end

                win = state.winner()
                if win is not None:
                    # state.showBoard()
                    # ended with p1 either win or draw
                    state.giveReward()
                    state.p1.reset()
                    state.p2.reset()
                    state.reset()
                    break

                else:
                    # Player 2
                    positions = state.availablePositions()
                    p2_action = state.p2.chooseAction(
                        positions, state.board, state.playerSymbol)
                    state.updateState(p2_action)
                    board_hash = state.getHash()
                    state.p2.addState(board_hash)

                    win = state.winner()
                    if win is not None:
                        # state.showBoard()
                        # ended with p2 either win or draw
                        state.giveReward()
                        state.p1.reset()
                        state.p2.reset()
                        state.reset()
                        break

    # play with human
    def human_play(state):
        while not state.isEnd:
            # Player 1
            positions = state.availablePositions()
            p1_action = state.p1.chooseAction(
                positions, state.board, state.playerSymbol)
            # take action and upate board state
            state.updateState(p1_action)
            state.showBoard()
            # check board status if it is end
            win = state.winner()
            if win is not None:
                if win == 1:
                    print(state.p1.name, "wins!")
                else:
                    print("tie!")
                state.reset()
                break

            else:
                # Player 2
                positions = state.availablePositions()
                p2_action = state.p2.chooseAction(positions)

                state.updateState(p2_action)
                state.showBoard()
                win = state.winner()
                if win is not None:
                    if win == -1:
                        print(state.p2.name, "wins!")
                    else:
                        print("tie!")
                    state.reset()
                    break

    def random_play(state,rounds=100):
        for i in tqdm(range(rounds)):
            for j in 100:
                while not state.isEnd:
                    # Player 1
                    positions = state.availablePositions()
                    p1_action = state.p1.chooseAction(
                        positions, state.board, state.playerSymbol)
                    # take action and upate board state
                    state.updateState(p1_action)
                    # check board status if it is end

                    win = state.winner()
                    if win is not None:
                        # state.showBoard()
                        # ended with p1 either win or draw
                        state.p1.reset()
                        state.p2.reset()
                        state.reset()
                        break

                    else:
                        # Player 2
                        positions = state.availablePositions()
                        p2_action = state.p2.chooseAction(
                            positions, state.board, state.playerSymbol)
                        state.updateState(p2_action)

                        win = state.winner()
                        if win is not None:
                            # state.showBoard()
                            # ended with p2 either win or draw
                            state.p1.reset()
                            state.p2.reset()
                            state.reset()
                            break

