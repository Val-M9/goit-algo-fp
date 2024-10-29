items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    for item, details in items.items():
        if details['cost'] <= remaining_budget:
            chosen_items.append(item)
            remaining_budget -= details['cost']
            total_calories += details['calories']

    return chosen_items, total_calories, budget - remaining_budget


def dynamic_programming(items, budget):
    item_list = list(items.values())
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(item_list) + 1)]

    for i in range(1, len(item_list) + 1):
        for j in range(1, budget + 1):
            if item_list[i - 1]['cost'] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - item_list[i - 1]
                               ['cost']] + item_list[i - 1]['calories'])
            else:
                dp[i][j] = dp[i - 1][j]

    total_calories = dp[len(item_list)][budget]
    remaining_budget = budget
    chosen_items = []

    for i in range(len(item_list), 0, -1):
        if dp[i][remaining_budget] != dp[i - 1][remaining_budget]:
            chosen_item_name = list(items.keys())[i - 1]
            chosen_items.append(chosen_item_name)
            remaining_budget -= item_list[i - 1]['cost']

    return chosen_items, total_calories, budget - remaining_budget


greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, 100)
print(f"You chose: {', '.join(greedy_items)}. Total calories: {
      greedy_calories}. Total cost: {greedy_cost}")

dynamic_items, dynamic_calories, Dynamic_cost = dynamic_programming(items, 100)
print(f"You chose: {', '.join(dynamic_items)}. Total calories: {
      dynamic_calories}. Total cost: {Dynamic_cost}")
