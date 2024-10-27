class GameRules:

    RULES = """
    Rules of the "Decoder" Game:

    1. Objective: Your goal is to guess the secret code consisting of 4 digits (from 0 to 9).

    2. Input: You need to enter 4 digits to make a guess. Ensure you only enter digits.

    3. Hints: If you get stuck, you can ask for a hint. To do this, enter 'h'. The number of hints depends on the difficulty you choose.

    4. Feedback: After each guess, the game provides feedback in the form of symbols:

       - '+' means that you guessed the number correctly and it is in the right place.
       - '-' means that you guessed the number, but it is in the wrong place.
       - ' ' means that this number is not in the secret code.

    5. End of Game: The game ends when you either guess the code or run out of attempts.

    Good luck guessing the secret code!
    """