"""
import random

arr = random.sample(range(1, 101), 5)
arr_insertion = arr.copy()
arr_selection = arr.copy()


count_bubble = 0
def bubble_sort(arr, count_bubble):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count_bubble += 1
                print(arr)
                print("Number of bubble swaps:", count_bubble)
    return arr, count_bubble

arr_b, c_b = (bubble_sort(arr, count_bubble))

count_insertion = 0
def insertion_sort(arr_insertion, count_insertion):
    for i in range(1, len(arr_insertion)):
        key = arr_insertion[i]
        j = i - 1
        while j >= 0 and key < arr_insertion[j]:
            arr_insertion[j + 1] = arr_insertion[j]
            j -= 1
        arr_insertion[j + 1] = key
        print(arr_insertion)
        count_insertion += 1
        print("Number of insertion swaps:", count_insertion)
    return arr_insertion, count_insertion

arr_i, c_i =(insertion_sort(arr_insertion, count_insertion))
print(arr_i)

count_selection = 0
def selection_sort(arr_selection, count_selection):
    n = len(arr_selection)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr_selection[j] < arr_selection[min_index]:
                min_index = j
        arr_selection[i], arr_selection[min_index] = arr_selection[min_index], arr_selection[i]
        count_selection += 1
        print(arr_selection)
        print("Number of selection swaps:", count_selection)
    return arr_selection, count_selection
    

arr_s, c_s = selection_sort(arr_selection, count_selection)
print(arr_s)

def compare_sort(arr, arr_insertion, arr_selection, count_bubble, count_insertion, count_selection):
    if c_b < c_i and c_b < c_s:
        print("Bubble sort is the most efficient with", c_b, "swaps.")
    elif c_i < c_b and c_i < c_s:
        print("Insertion sort is the most efficient with", c_i, "swaps.")
    else:
        print("Selection sort is the most efficient with", c_s, "swaps.")

compare_sort(arr, arr_insertion, arr_selection, count_bubble, count_insertion, count_selection)
"""
