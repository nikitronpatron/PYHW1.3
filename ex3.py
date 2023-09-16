# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. 
# *Верните все возможные варианты комплектации рюкзака.

items = [("Compass", 1), ("Rope", 2), ("Water", 2), ("Knife", 1), ("Coal", 3), ("Jacket", 2), ("Tent", 4)]
knapsack_capacity = 7

def max_weight_knapsack(knapsack_capacity, items, n):
    if n == 0 or knapsack_capacity == 0:
        return 0, []
    if items[n - 1][1] > knapsack_capacity:
        return max_weight_knapsack(knapsack_capacity, items, n - 1)

    included_weight, included_items = max_weight_knapsack(knapsack_capacity - items[n - 1][1], items, n - 1)
    included_weight += items[n - 1][1]
    excluded_weight, excluded_items = max_weight_knapsack(knapsack_capacity, items, n - 1)

    if included_weight > excluded_weight:
        return included_weight, included_items + [items[n - 1]]
    else:
        return excluded_weight, excluded_items

result, knapsack_contents = max_weight_knapsack(knapsack_capacity, items, len(items))
print("Maximum Weight:", result)
print("Knapsack Contents:", knapsack_contents)