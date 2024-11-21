# 1. Bubble Sort using Classes and Methods
class BubbleSort:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]

    def display(self):
        print("Bubble Sorted Data:", self.data)

# Example of Bubble Sort
bubble_sort = BubbleSort([64, 34, 25, 12, 22, 11, 90])
bubble_sort.sort()
bubble_sort.display()

print("\n" + "=" * 50 + "\n")


# 2. Insertion Sort
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Example of Insertion Sort
data = [64, 25, 12, 22, 11]
print("Insertion Sorted Data:", insertion_sort(data))

print("\n" + "=" * 50 + "\n")


# 3. Selection Sort
def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

# Example of Selection Sort
data = [64, 25, 12, 22, 11]
print("Selection Sorted Data:", selection_sort(data))

print("\n" + "=" * 50 + "\n")


# 4. Merge Sort
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

    return data

# Example of Merge Sort
data = [38, 27, 43, 3, 9, 82, 10]
print("Merge Sorted Data:", merge_sort(data))

print("\n" + "=" * 50 + "\n")


# 5. Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i  # Return index of target
    return -1  # Target not found

# Example of Linear Search
data = [64, 25, 12, 22, 11]
target = 22
result = linear_search(data, target)
print(f"Linear Search Result: {'Found at index ' + str(result) if result != -1 else 'Not Found'}")

print("\n" + "=" * 50 + "\n")


# 6. Binary Search (Requires sorted data)
def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example of Binary Search
data = [11, 12, 22, 25, 34, 64, 90]  # Sorted data
target = 25
result = binary_search(data, target)
print(f"Binary Search Result: {'Found at index ' + str(result) if result != -1 else 'Not Found'}")

print("\n" + "=" * 50 + "\n")


# 7. Binary Tree Implementation
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

# Example of Binary Tree
binary_tree = BinaryTree()
binary_tree.insert(50)
binary_tree.insert(30)
binary_tree.insert(20)
binary_tree.insert(40)
binary_tree.insert(70)
binary_tree.insert(60)
binary_tree.insert(80)

print("Inorder Traversal of Binary Tree: ")
binary_tree.inorder(binary_tree.root)
