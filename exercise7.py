import random
import matplotlib.pyplot as plt


def simulate_dice_roll(attempts):
    results = {}
    for _ in range(attempts):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        if total in results:
            results[total] += 1
        else:
            results[total] = 1

    probabilities = {key: round((value / attempts) * 100, 2)
                     for key, value in results.items()}

    return probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')

    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f'{prob}%', ha='center')

    plt.show()


if __name__ == '__main__':
    for attempts in [36, 1000, 10000, 100000]:
        probabilities = simulate_dice_roll(attempts)
        plot_probabilities(probabilities)
