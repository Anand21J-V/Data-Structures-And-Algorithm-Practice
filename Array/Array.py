class ArrayManipulator:
    def __init__(self, arr):
        self.arr = arr

    def insert_beginning(self, element):
        self.arr = [element] + self.arr

    def insert_end(self, element):
        self.arr.append(element)

    def insert_at_position(self, element, position):
        # position is 1-based index
        if position < 1 or position > len(self.arr) + 1:
            print("Invalid position!")
        else:
            self.arr = self.arr[:position-1] + [element] + self.arr[position-1:]

    def get_array(self):
        return self.arr


# Example usage
arr = [1, 2, 3, 4, 5]
manipulator = ArrayManipulator(arr)

manipulator.insert_beginning(6)   # Add 6 at the beginning
manipulator.insert_end(7)         # Add 7 at the end
manipulator.insert_at_position(8, 4)  # Add 8 at position 4 (1-based index)

# Final Output
print("Output:", manipulator.get_array())
