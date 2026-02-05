def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print("--- Bubble Sort Program ---")
user_input = input("Enter numbers separated by space: ")
numbers = [float(x) for x in user_input.split()]

print(f"Original: {numbers}")
sorted_list = bubble_sort(numbers)
print(f"Sorted:   {sorted_list}")