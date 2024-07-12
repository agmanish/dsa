class Heap:
    def __init__(self):
        """
        Initialize an empty heap with attributes:
        - arr: List to store elements of the heap.
        - arr_size: Current size of the heap.
        """
        self.arr = []
        self.arr_size = 0

    def max_heapify_util(self, i):
        """
        Perform max-heapify operation on subtree rooted at index i in the heap.

        Args:
        - i (int): Index of the root of the subtree to heapify.
        """
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2
        largest = i

        if (
            left_child_idx < self.arr_size
            and self.arr[left_child_idx] > self.arr[largest]
        ):
            largest = left_child_idx

        if (
            right_child_idx < self.arr_size
            and self.arr[right_child_idx] > self.arr[largest]
        ):
            largest = right_child_idx

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify_util(largest)

    def min_heapify_util(self, i):
        """
        Perform min-heapify operation on subtree rooted at index i in the heap.

        Args:
        - i (int): Index of the root of the subtree to heapify.
        """
        left_child_idx = 2 * i + 1
        right_child_idx = 2 * i + 2
        smallest = i

        if (
            left_child_idx < self.arr_size
            and self.arr[left_child_idx] < self.arr[smallest]
        ):
            smallest = left_child_idx

        if (
            right_child_idx < self.arr_size
            and self.arr[right_child_idx] < self.arr[smallest]
        ):
            smallest = right_child_idx

        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify_util(smallest)

    def heapify(self, inp_arr, heap_type="max"):
        """
        Transform input array into a heap.

        Args:
        - inp_arr (list): List of integers to be transformed into a heap.
        - heap_type (str): Type of heap ('max' for max-heap, 'min' for min-heap). Default is 'max'.
        """
        self.arr = inp_arr[:]
        self.arr_size = len(self.arr)
        for i in range(self.arr_size // 2 - 1, -1, -1):
            if heap_type == "max":
                self.max_heapify_util(i)
            elif heap_type == "min":
                self.min_heapify_util(i)

    def heap_sort(self):
        """
        Perform heap sort on the heap.

        This assumes the heap is already built.
        """
        for i in range(self.arr_size - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.arr_size -= 1
            self.max_heapify_util(0)


class RoomAllocation:
    def __init__(self):
        """
        Initialize RoomAllocation with attributes:
        - inp_arrs: List to store input arrays read from file.
        - room_order: Dictionary mapping array index to room type.
        - op_string1: String to accumulate output for part 1 of output file.
        - op_string2: String to accumulate output for part 2 of output file.
        """
        self.inp_arrs = []
        self.room_order = {
            0: "Suite",
            1: "Balcony",
            2: "Outside",
            3: "Ocean View",
            4: "Interior",
        }
        self.op_string1 = ""
        self.op_string2 = ""

    def read_input(self, ip_file_path="inputPS05.txt"):
        """
        Read input data from a file and populate inp_arrs attribute.

        Args:
        - ip_file_path (str): Path to the input file.
        """
        try:
            with open(ip_file_path, "r") as file:
                data = file.readlines()
                for line in data:
                    numbers = []
                    for item in line.strip().split(", "):
                        try:
                            numbers.append(int(item))
                        except ValueError:
                            print(f"Invalid input {item} in file {ip_file_path}.")
                    self.inp_arrs.append(numbers)
        except FileNotFoundError:
            print(f"File {ip_file_path} not found.")

    def assign_rooms(self):
        """
        Assign rooms based on sorted IDs and calculate median for each room type.
        """
        heap = Heap()
        remaining_arr = []
        for arr_num, inp_arr in enumerate(self.inp_arrs):
            room_type = self.room_order[arr_num]
            remaining_arr.extend(inp_arr)
            heap.heapify(remaining_arr)
            heap.heap_sort()
            sorted_arr = heap.arr
            median_index = len(sorted_arr) // 2
            allocated_rooms = sorted_arr[:median_index]
            median = sorted_arr[median_index]
            remaining_arr = sorted_arr[median_index + 1 :]

            self.op_string1 += f"""Sorted ID List: ({room_type})\n{', '.join(map(str, sorted_arr))}\nMedian Element: {median}\n\n"""

            if room_type in ["Suite", "Outside", "Ocean View"]:
                self.op_string2 += f"{self.room_order[arr_num]} rooms were allocated to : {', '.join(map(str, allocated_rooms))}\n"

    def write_output(self, op_file_path="outputPS05.txt"):
        """Write output data to a file.

        Args:
        - op_file_path (str): Path to the input file.
        """
        with open(op_file_path, "w") as file:
            file.write(self.op_string1 + "\n")
            file.write(self.op_string2)


if __name__ == "__main__":
    room_allocation = RoomAllocation()
    room_allocation.read_input()
    room_allocation.assign_rooms()
    room_allocation.write_output()
