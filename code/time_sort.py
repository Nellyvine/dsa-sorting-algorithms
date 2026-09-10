import time
import random
import statistics
import json

from bubblesort import bubble_sort
from quicksort import quick_sort


def time_sort(sort_function, build_list, repeats=5):

    times = []

    for _ in range(repeats):
        data = build_list()

        start = time.perf_counter()
        sort_function(data)
        end = time.perf_counter()

        times.append(end - start)

    return statistics.mean(times)


def time_same_input(sort_function_1, sort_function_2, build_list, repeats=5):
    
    times_1 = []
    times_2 = []

    for _ in range(repeats):
        data = build_list()

        # Give each algorithm its own copy
        data_1 = data.copy()
        data_2 = data.copy()

        start = time.perf_counter()
        sort_function_1(data_1)
        end = time.perf_counter()
        times_1.append(end - start)

        start = time.perf_counter()
        sort_function_2(data_2)
        end = time.perf_counter()
        times_2.append(end - start)

    return statistics.mean(times_1), statistics.mean(times_2)


sizes = [500, 1000, 2000, 4000, 8000]

# Store results for plotting later
results = {
    "bubble": {},
    "quick": {},
    "bubble_sorted": {}
}


# Random lists
for n in sizes:

    build_random_list = lambda n=n: [
        random.randint(0, 100000)
        for _ in range(n)
    ]

    bubble_time, quick_time = time_same_input(
        bubble_sort,
        quick_sort,
        build_random_list
    )

    results["bubble"][n] = bubble_time
    results["quick"][n] = quick_time


# Already-sorted lists
for n in sizes:

    build_sorted_list = lambda n=n: list(range(n))

    results["bubble_sorted"][n] = time_sort(
        bubble_sort,
        build_sorted_list
    )


# Print results
print("Results:")
print("Size\tBubble\t\tQuick\t\tBubble (sorted)")

for n in sizes:
    print(
        f"{n}\t"
        f"{results['bubble'][n]:.6f}\t"
        f"{results['quick'][n]:.6f}\t"
        f"{results['bubble_sorted'][n]:.6f}"
    )


# Save results to JSON
with open("sorting_results.json", "w") as file:
    json.dump(results, file, indent=4)

print("\nResults saved to sorting_results.json")