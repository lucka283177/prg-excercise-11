import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]
def selection_sort(numbers):
    min_index = 0
    min_number = numbers[min_index]
    for j in range(len(numbers)):
        min_index = j
        min_number = numbers[min_index]
        for i in range(j + 1, len(numbers)):
            if numbers[i] < min_number:
                min_index = i
                min_number = numbers[i]
        numbers[j], numbers[min_index] = numbers[min_index], numbers[j]
        print(numbers)
    return numbers

if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]

    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
    print(selection_sort(values))
