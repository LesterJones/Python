import random


TAIL_WIN_PERCENTAGE = 49
SESSIONS = 4                 # This is how many times we will repeat the experiment.
ROLLS_PER_SESSION = 6        # This is how many rolls will be done each session.
BETTING_PATTERN = 'HTt'      # This can be any length and it will repeat. Or you can make it match the length
                             # of SESSIONS.  "H' is heads, 'T' is Tails, 't' is tie.


def who_won(result):
    i = 0
    h_count = 0
    t_count = 0
    while i < len(result):
        if result[i] == 'H':
            h_count += 1
        else:
            t_count += 1
        i += 1
    if h_count > t_count:
        return 'Heads'
    elif t_count > h_count:
        return 'Tails'
    else:
        return 'Tie'


def coin_flip():
    results = list()
    outcomes = list()
    all_outcomes = ''
    heads = 0
    tails = 0
    i = 0
    while i < SESSIONS:
        j = 0
        result = ''
        while j < ROLLS_PER_SESSION:
            value = random.randint(1, 100)
            if value <= TAIL_WIN_PERCENTAGE:
                result = result + 'T'
                tails += 1
            else:
                result = result + 'H'
                heads += 1
            j += 1
        results.append(result)
        all_outcomes = all_outcomes + result
        winner = who_won(result)
        outcomes.append(winner)
        i += 1
    return results, outcomes, heads, tails, all_outcomes


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Start a loop.

    while True:
        # Run a new simulation.
        input('Hit enter to run a new simulation.')
        results, outcomes, heads, tails, all_outcomes = coin_flip()

        # Print the results.
        print('======= Section 1: ==========')
        i = 0
        while i < len(results):
            print(str(i+1) + ') ' + results[i] + ' (Result: ' + outcomes[i] + ')')
            i += 1

        print('')
        print('======= Section 2: ==========')
        print('Total coin flips: ' + str(SESSIONS * ROLLS_PER_SESSION) + ' total')
        print('Tails: ' + str(tails) + ' (' + str(round(100 * (tails / (heads + tails)))) + '%)')
        print('Heads: ' + str(heads) + ' (' + str(round(100 * (heads / (heads + tails)))) + '%)')
        print(' ')

        print('======= Section 3: ==========')
        print('Total Rows: ' + str(SESSIONS))

        t_wins = outcomes.count('Tails')
        h_wins = outcomes.count('Heads')
        tie = outcomes.count('Tie')
        total = t_wins + h_wins + tie

        print('Tails row count total: ' + str(t_wins) + ' or ' + str(round(100 * (t_wins/total))) + '%')
        print('Heads row count total: ' + str(h_wins) + ' or ' + str(round(100 * (h_wins / total))) + '%')
        print('Tie row count total: ' + str(tie) + ' or ' + str(round(100 * (tie / total))) + '%')
        print('')

        # Calculate the stats for section 4.
        index = 0
        correct = 0
        incorrect = 0
        max_correct_streak = 0
        max_incorrect_streak = 0
        i = 0
        win_streak = 0
        lose_streak = 0
        while i < len(all_outcomes):
            while index >= len(BETTING_PATTERN):
                index = index % len(BETTING_PATTERN)
            outcome = all_outcomes[i]
            bet = BETTING_PATTERN[index]
            if outcome == bet:
                correct += 1
                win_streak += 1
                if win_streak > max_correct_streak:
                    max_correct_streak = win_streak
                lose_streak = 0
            else:
                incorrect += 1
                lose_streak += 1
                if lose_streak > max_incorrect_streak:
                    max_incorrect_streak = lose_streak
                win_streak = 0
            i += 1
            index += 1

        total = correct + incorrect

        print('======= Section 4: ==========')
        print('Total bets: ' + str(SESSIONS))
        print('Correct Guesses: ' + str(correct) + ' (' + str(round(100 * (correct / total))) + '%)')
        print('Incorrect Guesses: ' + str(correct) + ' (' + str(round(100 * (incorrect / total))) + '%)')
        print('Longest incorrect guess streak: ' + str(max_incorrect_streak))
        print('Longest correct guesses streak: ' + str(max_correct_streak))
        print('')