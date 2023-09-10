from tqdm import tqdm
from Player import Learning_Player


class Game:
    def play(state,p1,p2, rounds=100):

        annealing_interval = 50

        for i in tqdm(range(rounds)):
            if (i + 1) % annealing_interval == 0:
                p1.anneal_exp_rate()
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
                    p1_wins_count+=1
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
                        p2_wins_count+=1
                        state.giveReward()
                        state.p1.reset()
                        state.p2.reset()
                        state.reset()
                        break
                    ties_count+=1

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

    def random_play(state):
        while not state.isEnd:
            # Player 1
            positions = state.availablePositions()
            p1_action = state.p1.chooseAction(
                positions, state.board, state.playerSymbol)
            # take action and upate board state
            state.updateState(p1_action)
            # print("action for p1 is", p1_action)
            # state.showBoard()
            # check board status if it is end
            win = state.winner()
            if win is not None:
                state.reset()
                if win == 1:
                    return 1
                else:
                    return 0
            else:
                # Player 2
                positions = state.availablePositions()
                p2_action = state.p2.chooseAction(positions)

                state.updateState(p2_action)
                win = state.winner()
                if win is not None:
                    state.reset()
                    if win == -1:
                        return 1
                    else:
                        return 0


