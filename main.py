from game import DecoderGame

from constants import GameConstants

from rules import GameRules

def main():
    read_rules = input("Do you want to read the rules? (yes/no): ").lower().strip()

    if read_rules in ['yes', 'y']:

        print(GameRules.RULES)

    game = DecoderGame()

    while True:
        game.play()
        play_again = input(GameConstants.MESSAGES['play_again']).lower().strip()

        if play_again == 'no':

            print(GameConstants.MESSAGES['goodbye'])
            break

if __name__ == "__main__":
    main()