from Player import Learning_Player
from State import State
from Game import Game

def main():
    # training
    p1 = Learning_Player("p1")
    p2 = Learning_Player("p2")

    st = State(p1, p2)
    print("training...")
    Game.play(st,p1,p2,50000)

    p1.savePolicy()
    p2.savePolicy()

if __name__ == "__main__":
    main()
