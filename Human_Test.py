from Player import Learning_Player,Human_Player
from State import State
from Game import Game

def main():
    # competition
    p1 = Learning_Player("X-man", exp_rate=0)
    p1.loadPolicy("policy_p1")
    p2 = Human_Player("O-man")
    st = State(p1, p2)
    Game.human_play(st)

if __name__ == "__main__":
    main()
