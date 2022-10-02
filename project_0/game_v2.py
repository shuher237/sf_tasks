"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binary_search(list, item: int=1) -> int:
    """ИСпользуем алгоритм бинарного поиска, чтобы угадать число

    Args:
        list (_type_): список загаданных чисел
        item (_type_): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    low = 0
    high = len(list)-1
    
    cnt=0
    while low <= high:
        cnt+=1
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return cnt
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return cnt

def score_game(binary_search) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        binary_search (_type_): функция угадывания числа

    Returns:
        int: количество попытокв среднем, необходимое для угадывания
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = list(np.random.randint(1, 101, size=(1000)))  # загадали список чисел
    random_array.sort()

    for number in random_array:
        count_ls.append(binary_search(random_array, number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_search)
