import time
from string import ascii_letters, digits, punctuation


# Один из первых вариантов.
def my_algorithm(display_limit=0):
    # Создаём общий набор доступных символов.
    characters = ascii_letters + digits + punctuation

    # Создаём счётчик комбинаций.
    count = 0

    for a in characters:
        for b in characters:
            for c in characters:
                for d in characters:
                    # Выводим только ограниченное количество комбинаций.
                    if count < display_limit:
                        print(a, b, c, d)

                    count += 1

    print("Количество результатов:", count)


if __name__ == "__main__":
    # Измеряем общее время выполнения.
    start_time = time.perf_counter()
    my_algorithm(display_limit=10)
    end_time = time.perf_counter()

    print(f"Время выполнения: {end_time - start_time:.6f} секунд")