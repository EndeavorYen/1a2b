import random
import itertools

def generate_secret():
    # Generate a 4-digit secret number with unique digits and no leading zero
    digits = list('0123456789')
    random.shuffle(digits)
    if digits[0] == '0':
        # Ensure the first digit is not '0'
        for i in range(1, len(digits)):
            if digits[i] != '0':
                digits[0], digits[i] = digits[i], digits[0]
                break
    return ''.join(digits[:4])

def get_all_candidates():
    # Generate all 4-digit numbers with unique digits and no leading zero
    candidates = []
    for perm in itertools.permutations('0123456789', 4):
        if perm[0] != '0':
            candidates.append(''.join(perm))
    return candidates

def get_score(guess, secret):
    # Calculate bulls (correct digit and position) and cows (correct digit but wrong position)
    bulls = sum(1 for i in range(4) if guess[i] == secret[i])
    cows = sum(min(guess.count(d), secret.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def minimax_guess(possible, all_candidates):
    """
    For each candidate in the full candidate set, evaluate the worst-case number of remaining possibilities
    if it were chosen as the guess. Then, select the candidate that minimizes this worst-case count.
    """
    best_guess = None
    best_score = float('inf')
    for guess in all_candidates:
        score_count = {}
        for candidate in possible:
            score = get_score(guess, candidate)
            score_count[score] = score_count.get(score, 0) + 1
        worst_case = max(score_count.values())
        if worst_case < best_score:
            best_score = worst_case
            best_guess = guess
        elif worst_case == best_score and best_guess not in possible and guess in possible:
            best_guess = guess
    return best_guess

def player_game(secret):
    """
    Let the player guess until they guess the secret.
    Returns the number of steps (guesses) the player used.
    """
    print("Player guessing phase: Please guess a 4-digit number with unique digits (no leading zero).")
    steps = 0
    while True:
        guess = input("Enter your guess: ")
        # Validate the guess: must be 4 digits, all numeric, unique digits and first digit not '0'
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4 or guess[0] == '0':
            print("Invalid input. Please make sure the guess is 4 digits, with no leading zero and unique digits.")
            continue
        steps += 1
        bulls, cows = get_score(guess, secret)
        print(f"{bulls}A{cows}B")
        if bulls == 4:
            print(f"Congratulations! You guessed the secret number {secret} in {steps} steps.")
            break
    return steps

def algorithm_game(secret):
    """
    Use minimax algorithm to guess the secret.
    Returns the number of steps (guesses) the algorithm used.
    """
    print("\nAlgorithm guessing phase: The algorithm starts guessing the secret.")
    all_candidates = get_all_candidates()
    possible = all_candidates.copy()
    # Starting with an initial guess "1234" if valid
    guess = "1234" if "1234" in all_candidates else possible[0]
    steps = 0
    while True:
        steps += 1
        bulls, cows = get_score(guess, secret)
        print(f"Step {steps}: Guess = {guess} -> {bulls}A{cows}B")
        if bulls == 4:
            print(f"The algorithm found the secret number {secret} in {steps} steps!")
            break
        # Filter the possible candidates based on the feedback
        possible = [cand for cand in possible if get_score(guess, cand) == (bulls, cows)]
        guess = minimax_guess(possible, all_candidates)
    return steps

def main():
    secret = generate_secret()
    # Player guessing phase
    player_steps = player_game(secret)
    # Algorithm guessing phase
    algorithm_steps = algorithm_game(secret)
    
    print("\nGuessing result comparison:")
    print(f"Player steps: {player_steps}")
    print(f"Algorithm steps: {algorithm_steps}")
    if player_steps < algorithm_steps:
        print("Player wins!")
    elif player_steps > algorithm_steps:
        print("Algorithm wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()
