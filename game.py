import random

from typing import List, Tuple

from constants import GameConstants

class DecoderGame:

    def __init__(self):
        self.constants = GameConstants

    def generate_code(self) -> str:

        return ''.join(random.sample(self.constants.DIGITS_RANGE, self.constants.CODE_LENGTH))

    def validate_guess(self, guess: str) -> bool:

        return (guess.isdigit() and
                len(guess) == self.constants.CODE_LENGTH and
                all(d in self.constants.DIGITS_RANGE for d in guess))

    def check_guess(self, secret_code: str, guess: str) -> Tuple[int, int]:
        exact_matches = sum(1 for i in range(self.constants.CODE_LENGTH) if guess[i] == secret_code[i])
        digit_matches = sum(min(secret_code.count(d), guess.count(d)) for d in set(guess)) - exact_matches

        return exact_matches, digit_matches

    @staticmethod

    def format_feedback(exact_matches: int, digit_matches: int) -> str:

        return '+' * exact_matches + '-' * digit_matches

    def get_hint(self, secret_code: str, used_positions: List[int]) -> Tuple[int, str]:
        available_positions = [i for i in range(self.constants.CODE_LENGTH) if i not in used_positions]
        position = random.choice(available_positions) if available_positions else -1

        return position, secret_code[position] if position >= 0 else ""

    def get_difficulty_input(self) -> str:

        while True:

            print("\nChoose a difficulty level:")

            for level, params in self.constants.DIFFICULTY_LEVELS.items():
                print(f"- {level} (attempts: {params['attempts']}, hints: {params['hints']})")

            choice = input("Your choice: ").lower().strip()

            if choice in self.constants.DIFFICULTY_LEVELS:
                return choice

            print("Please enter 'easy', 'medium' or 'hard'.")

    def play(self) -> bool:

        print(self.constants.MESSAGES['welcome'])

        print(self.constants.MESSAGES['code_rules'])

        difficulty = self.get_difficulty_input()
        params = self.constants.DIFFICULTY_LEVELS[difficulty]
        max_attempts, hints_left = params['attempts'], params['hints']

        secret_code = self.generate_code()
        used_hint_positions = []

        while max_attempts > 0:
            guess = input(f"Enter {self.constants.CODE_LENGTH} digits (1-10) or 'h' for a hint: ").strip().lower()

            if guess == 'h':
                if hints_left > 0:
                    position, value = self.get_hint(secret_code, used_hint_positions)
                    if position >= 0:
                        hints_left -= 1
                        used_hint_positions.append(position)

                        print(f"Hint: Position {position + 1} is the digit {value}. Hints left: {hints_left}")

                    else:

                        print(self.constants.MESSAGES['all_positions_revealed'])

                else:

                    print(self.constants.MESSAGES['no_hints'])
                continue

            if not self.validate_guess(guess):

                print(self.constants.MESSAGES['invalid_format'])
                continue

            exact, partial = self.check_guess(secret_code, guess)
            print(f"Result: {self.format_feedback(exact, partial)}")
            max_attempts -= 1

            if exact == self.constants.CODE_LENGTH:

                print(self.constants.MESSAGES['win'].format(params['attempts'] - max_attempts))
                return True

        print(self.constants.MESSAGES['lose'].format(secret_code))
        return False