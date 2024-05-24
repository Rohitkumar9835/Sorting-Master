import random
import time
import matplotlib.pyplot as plt

def generate_input(n):
    with open("input.txt", "w") as file:
        for i in range(n):
            file.write(str(random.randint(0, 999)) + "\n")

def read_input():
    with open("input.txt", "r") as file:
        arr = [int(line.strip()) for line in file]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def counting_sort(arr):
    max_val = max(arr) + 1
    counts = [0] * max_val
    for num in arr:
        counts[num] += 1
    sorted_arr = []
    for i in range(max_val):
        sorted_arr += [i] * counts[i]
    return sorted_arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [num for num in arr[1:] if num <= pivot]
    right = [num for num in arr[1:] if num > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged

# Measure the execution time of each sorting algorithm
ns = [1000,2000,3000,4000,5000]
times = {"insertion": [], "counting": [], "quick": [], "merge": []}
for n in ns:
    generate_input(n)
    arr = read_input()

    start_time = time.time()
    insertion_sort(arr.copy())
    end_time = time.time()
    times["insertion"].append(end_time - start_time)

    start_time = time.time()
    counting_sort(arr.copy())
    end_time = time.time()
    times["counting"].append(end_time - start_time)

    start_time = time.time()
    quick_sort(arr.copy())
    end_time = time.time()
    times["quick"].append(end_time - start_time)

    start_time = time.time()
    merge_sort(arr.copy())
    end_time = time.time()
    times["merge"].append(end_time - start_time)

# Plot the graph
plt.plot(ns, times["insertion"], label="Insertion sort")
plt.plot(ns, times["counting"], label="Counting sort")
plt.plot(ns, times["quick"], label="Quick sort")
plt.plot(ns, times["merge"], label="Merge sort")
plt.xlabel("n")
plt.ylabel("Time taken (seconds)")
plt.legend()
plt.show()
