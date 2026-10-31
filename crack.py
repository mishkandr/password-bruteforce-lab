from alphabet import build_alphabet

from string import digits, ascii_letters, punctuation
import time


def my_algorithm():
    characters = ascii_letters + digits + punctuation
    count = 0
    for a in characters:
        for b in characters:
            for c in characters:
                for d in characters:
                    print(a,b,c,d)
                    count += 1
    print("Колличество результатов:",(count))
    sum(range(1000000))

# start_time = time.perf_counter()
# my_algorithm()
# end_time = time.perf_counter()

# print(f"Время выполнения: {end_time - start_time:.6f} секунд")
answer = input("Include digits? (y/n): ")
include_digits = answer == "y"

characters = build_alphabet(include_digits, False, False, False)
print(characters)