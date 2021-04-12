# Zadanie OpenX staz - Wariant 1
import random
import math


class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.child_count = 0
        self.child_sum = 0


class Tree:
    def __init__(self):
        self.root = None

    # needed because it adds new children randomly left, right
    def rand_child(self, node):
        rand = random.randint(1, 2)
        if rand == 1:
            return node.left
        else:
            return node.right

    def insert(self, key):
        x = Node(key)
        prev = None
        curr = self.root

        while curr is not None:
            prev = curr
            curr.child_count += 1
            curr.child_sum += x.key
            # add child randomly left or right
            curr = self.rand_child(curr)

        x.parent = prev
        if self.root is None:
            self.root = x
        else:
            if prev.left is None:
                prev.left = x
            else:
                prev.right = x

    def find(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root
        n = self.find(root.left, key)
        if n:
            return n
        n = self.find(root.right, key)
        if n:
            return n

    def get_array(self, node):
        if node is None:
            return []
        res = [node.key]
        res += self.get_array(node.left)
        res += self.get_array(node.right)
        return res

    # Complexity: O(1)
    def get_sum(self, node):
        return node.child_sum + node.key

    # Complexity: O(1)
    def get_average(self, node):
        return self.get_sum(node) / (node.child_count + 1)

    # Complexity O(N), because i get_array(O(N)) and i use kth_smallest(QuickSelect Algoritm - Complexity: O(N)) => O(N)
    def get_median(self, node):
        arr = self.get_array(node)
        if len(arr) % 2 == 1:
            return self.kth_smallest(arr, 0, len(arr) - 1, math.floor(len(arr) / 2) + 1)
        else:
            mid_left = self.kth_smallest(arr, 0, len(arr) - 1, (len(arr) / 2))
            mid_right = self.kth_smallest(arr, 0, len(arr) - 1, (len(arr) / 2) + 1)
            return (mid_left + mid_right) / 2

    # Complexity: O(N) QuickSelect Algorithm
    def kth_smallest(self, arr, l, r, k):
        if 0 < k <= r - l + 1:
            pos = self.partition(arr, l, r)

            if pos - l == k - 1:
                return arr[pos]
            if pos - l > k - 1:
                return self.kth_smallest(arr, l, pos - 1, k)
            return self.kth_smallest(arr, pos + 1, r, k - pos + l - 1)

    def partition(self, arr, l, r):
        x = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.left, level + 1)
            print(' ' * 4 * level + '->', node.key)
            self.print_tree(node.right, level + 1)

    def create_tree(self):
        while True:
            print(" i - insert(key, val)\n"
                  " m - get median\n"
                  " a - get average\n"
                  " s - get sum\n"
                  " e - end \n")
            opr = input("Podaj komende:")
            if opr == 'i':
                key = int(input("Podaj klucz:"))
                self.insert(key)
            elif opr == 'm':
                key = int(input("Podaj klucz:"))
                node = self.find(self.root, key)
                print("Mediana wezla " + str(key) + " to:" + str(self.get_median(node)))
            elif opr == 'a':
                key = int(input("Podaj klucz:"))
                node = self.find(self.root, key)
                print("Srednia wezla " + str(key) + " to " + str(self.get_average(node)))
            elif opr == 's':
                key = int(input("Podaj klucz:"))
                node = self.find(self.root, key)
                print("Suma wezla " + str(key) + " to " + str(self.get_sum(node)))
            elif opr == 'e':
                break
            else:
                print("Komenda ", opr, " nie istnieje")
            print("Aktualne drzewo:\n")
            self.print_tree(self.root)

    def test(self):
        self.insert(3)
        self.insert(10)
        self.insert(12)
        self.insert(7)
        self.insert(5)
        self.insert(6)
        self.insert(9)
        self.insert(8)
        key = 10
        node = self.find(self.root, key)
        print("Aktualne drzewo: ")
        tree.print_tree(tree.root)
        print("Mediana wezla " + str(key) + " to:" + str(tree.get_median(node)))
        print("Srednia wezla " + str(key) + " to " + str(tree.get_average(node)))
        print("Suma wezla " + str(key) + " to " + str(tree.get_sum(node)))


tree = Tree()
tree.test()
# tree.create_tree()
