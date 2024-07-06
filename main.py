# Heap Utils


def heapify(arr, arr_size, i):

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < arr_size and arr[i] < arr[left]:
        largest = left

    if right < arr_size and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, arr_size, largest)


def build_heap(arr, arr_size):
    for i in range(arr_size // 2, -1, -1):
        heapify(arr, arr_size, i)


def heap_sort(arr):

    arr_size = len(arr)

    build_heap(arr, arr_size)

    for i in range(arr_size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def find_median(sorted_arr):
    n = len(sorted_arr)
    return sorted_arr[n // 2]


# IO operations


def read_input(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
        initial_list = list(map(int, data[0].strip().split(", ")))
        new_sets = [list(map(int, line.strip().split(", "))) for line in data[1:]]
        return initial_list, new_sets
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return [], []


def write_output(file_path, results):
    with open(file_path, "w") as file:
        file.write("Suite Rooms:\n")
        file.write(" ".join(map(str, results[0])) + "\n")
        file.write("Outside Rooms:\n")
        file.write(" ".join(map(str, results[2])) + "\n")
        file.write("Ocean View Rooms:\n")
        file.write(" ".join(map(str, results[3])) + "\n")


def main():
    input_file = "inputPS05.txt"
    output_file = "outputPS05.txt"

    initial_list, new_sets = read_input(input_file)

    # Step 1: Sort initial list
    heap_sort(initial_list)
    sorted_list = initial_list

    results = []
    # Step 2: Find median and allocate suite rooms
    median = find_median(sorted_list)
    results.append(sorted_list[: sorted_list.index(median) + 1])
    sorted_list = sorted_list[sorted_list.index(median) :]

    # Step 3: Include new sets, sort, and find new medians
    for new_set in new_sets:
        insert_pos = sorted_list.index(median) + 1
        sorted_list = sorted_list[:insert_pos] + new_set + sorted_list[insert_pos:]
        heap_sort(sorted_list)
        median = find_median(sorted_list)

        # Step 4: Allocate other rooms based on new medians
        results.append(sorted_list[: sorted_list.index(median) + 1])
        sorted_list = sorted_list[sorted_list.index(median) :]

    # Write output to file
    write_output(output_file, results)


if __name__ == "__main__":
    main()
