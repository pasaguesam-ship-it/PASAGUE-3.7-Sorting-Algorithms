def build_name_array(full_name):
    letters = []
    for char in full_name.upper():
        if char.isalpha() and char not in letters:
            letters.append(char)
    return letters


def insertion_sort(array):
    sorted_array = array.copy()
    for i in range(1, len(sorted_array)):
        key = sorted_array[i]
        j = i - 1
        while j >= 0 and sorted_array[j] > key:
            sorted_array[j + 1] = sorted_array[j]
            j -= 1
        sorted_array[j + 1] = key
    return sorted_array


full_name = "Samantha Leonor B. Pasague"

unsorted_array = build_name_array(full_name)
sorted_array = insertion_sort(unsorted_array)

print("Full Name:", full_name)
print("Unsorted Array:", unsorted_array)
print("Sorted Array:", sorted_array)
