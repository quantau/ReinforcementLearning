from Player import Learning_Player, Random_Player
from State import State
from Game import Game
import matplotlib.pyplot as plt
from tqdm import tqdm

def eval_players(st,num_battles, games_per_battle=100):
    p1_wins = []
    p2_wins = []
    draws = []
    count = []

    for i in tqdm(range(num_battles)):
        p1win = 0
        p2win = 0
        draw = 0
        for j in range(games_per_battle):
            winner = Game.random_play(st)
            if winner == 1:
                p1win+=1
            elif winner == 0:
                draw+=1
            else: 
                p2win+=1
        p1_wins.append(p1win*100.0/games_per_battle)
        p2_wins.append(p2win*100.0/games_per_battle)
        draws.append(draw*100.0/games_per_battle)
        count.append(i*games_per_battle)
        p1_wins.append(p1win*100.0/games_per_battle)
        p2_wins.append(p2win*100.0/games_per_battle)
        draws.append(draw*100.0/games_per_battle)
        count.append((i+1)*games_per_battle)

    plt.ylabel('Game outcomes in %')
    plt.xlabel('Game number')

    plt.plot(count, draws, 'r-', label='Draw')
    plt.plot(count, p1_wins, 'g-', label='Player 1 wins')
    plt.plot(count, p2_wins, 'b-', label='Player 2 wins')
    plt.legend(loc='best', shadow=True, fancybox=True, framealpha=0.7)
    plt.show()

def main():
    # competition
    p1 = Learning_Player("X-man", exp_rate=0)
    p1.loadPolicy("policy_p1")
    p2 = Random_Player("O-man")
    st = State(p1, p2)
    eval_players(st,100)


if __name__ == "__main__":
    main()
