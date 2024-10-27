class GameConstants:

    CODE_LENGTH = 4

    MIN_DIGIT = 0

    MAX_DIGIT = 9

    DIGITS_RANGE = '0123456789'

    DIFFICULTY_LEVELS = {
        'easy': {'attempts': 12, 'hints': 3},
        'medium': {'attempts': 8, 'hints': 2},
        'hard': {'attempts': 6, 'hints': 1}
    }

    MESSAGES = {
        'welcome': 'Welcome to the "Decoder" game!',
        'code_rules': f'You need to guess a code of {CODE_LENGTH} digits (from {MIN_DIGIT} to {MAX_DIGIT})',
        'hint_info': 'To get a hint, enter "h"',
        'invalid_format': f'Invalid format! Enter {CODE_LENGTH} digits from {MIN_DIGIT} to {MAX_DIGIT}.',
        'no_hints': 'You have no hints left!',
        'all_positions_revealed': 'All positions are already revealed!',
        'win': 'Congratulations! You guessed the code in {} attempts!',
        'lose': 'Game over! The correct code was: {}',
        'play_again': 'Would you like to play again? (yes/no): ',
        'invalid_choice': 'Please enter "easy", "medium" or "hard"',
        'goodbye': 'Thank you for playing!'
    }