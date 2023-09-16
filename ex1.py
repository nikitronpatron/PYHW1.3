# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

input_list = [1, 2, 2, 3, 4, 4, 5]

def find_duplicates(input_list):
    seen = set()
    duplicates = []
    for item in input_list:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

result = find_duplicates(input_list)
print(result)
