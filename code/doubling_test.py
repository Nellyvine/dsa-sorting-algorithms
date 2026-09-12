import json
from pathlib import Path


# Find sorting_results.json in the project folder
json_file = Path(__file__).resolve().parent.parent / "sorting_results.json"


# Load benchmark results
with open(json_file, "r") as file:
    results = json.load(file)


# JSON converts integer dictionary keys into strings,
# so convert them back into integers.
for algorithm in results:
    results[algorithm] = {
        int(size): time_taken
        for size, time_taken in results[algorithm].items()
    }


sizes = sorted(results["bubble"].keys())


def print_doubling_ratios(name, data):
    print(f"\n{name}")
    print("-" * len(name))

    for i in range(1, len(sizes)):
        previous_n = sizes[i - 1]
        current_n = sizes[i]

        previous_time = data[previous_n]
        current_time = data[current_n]

        ratio = current_time / previous_time

        print(
            f"{previous_n} -> {current_n}: "
            f"{current_time:.6f} / {previous_time:.6f} "
            f"= {ratio:.2f}"
        )


print("DOUBLING TEST")

print_doubling_ratios(
    "Bubble sort - random",
    results["bubble"]
)

print_doubling_ratios(
    "Quick sort - random",
    results["quick"]
)

print_doubling_ratios(
    "Bubble sort - already sorted",
    results["bubble_sorted"]
)