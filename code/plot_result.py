import json
from pathlib import Path
import matplotlib.pyplot as plt


json_file = Path(__file__).resolve().parent.parent / "sorting_results.json"

# Load the saved benchmark results
with open("sorting_results.json", "r") as file:
    results = json.load(file)


# Convert JSON dictionary keys from strings back to integers
for algorithm in results:
    results[algorithm] = {
        int(size): time_taken
        for size, time_taken in results[algorithm].items()
    }


# List sizes in the correct order
sizes = sorted(results["bubble"].keys())


# Extract timing data
bubble_times = [results["bubble"][n] for n in sizes]
quick_times = [results["quick"][n] for n in sizes]
bubble_sorted_times = [results["bubble_sorted"][n] for n in sizes]


# Create the graph
plt.figure(figsize=(10, 6))

plt.plot(
    sizes,
    bubble_times,
    marker="o",
    label="Bubble sort - random"
)

plt.plot(
    sizes,
    quick_times,
    marker="o",
    label="Quick sort - random"
)

plt.plot(
    sizes,
    bubble_sorted_times,
    marker="o",
    label="Bubble sort - already sorted"
)


# Labels and title
plt.xlabel("List size, n")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Performance")

# Show the legend
plt.legend()

# Make the graph easier to read
plt.grid(True)

# Display the graph
plt.show()