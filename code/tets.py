from bubblesort import bubble_sort
from quicksort import quick_sort

test_cases = [
    [],
    [5],
    [3, 3, 3],
    [1, 2, 3, 4, 5],          # already sorted
    [5, 4, 3, 2, 1],          # reverse sorted
    [3, 1, 4, 1, 5, 9, 2, 6], # random with duplicates
]

for case in test_cases:
    assert bubble_sort(case.copy()) == sorted(case), f"bubble_sort failed on {case}"
    assert quick_sort(case.copy()) == sorted(case), f"quick_sort failed on {case}"

print("\nAll correctness tests passed.")