from stack import Stack


class Node:
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None


class BST:
    def __init__(self):
        self.root = None
        self.len = 0

    def __len__(self):
        return self.len

    def _get_node_and_father(self, key):
        if self.root is None:
            return None, None
        return self.__get_node_and_father(key, self.root, None)

    def __get_node_and_father(self, key, node, father):
        if key == node.key:
            return node, father
        if key > node.key:
            return self.__get_node_and_father(key, node.right_child, node) if node.right_child else (None, node)
        return self.__get_node_and_father(key, node.left_child, node) if node.left_child else (None, node)

    def _get_max_and_father(self, node):
        if not node.right_child:
            return node, None
        return self.__get_max_and_father(node.right_child, node)

    def __get_max_and_father(self, node, father):
        if not node.right_child:
            return node, father
        return self.__get_max_and_father(node.right_child, node)

    def insert(self, key):
        node, father = self._get_node_and_father(key)
        if node:
            return
        new_node = Node(key)
        self.len += 1
        if not father:
            self.root = new_node
        elif key > father.key:
            father.right_child = new_node
        else:
            father.left_child = new_node

    def __contains__(self, key):
        node, father = self._get_node_and_father(key)
        return node is not None

    def remove(self, key):
        node, father = self._get_node_and_father(key)
        if node is None:
            raise KeyError()
        self.len -= 1
        if node.left_child is not None:
            max_left_node, max_left_father = self._get_max_and_father(node.left_child)
            node.key = max_left_node.key
            if max_left_father is None:
                node.left_child = max_left_node.left_child
            else:
                max_left_father.right_child = max_left_node.left_child
            return

        if node.right_child is not None:
            if not father:
                self.root = node.right_child
            else:
                father.right_child = node.right_child
            return

        if father is None:
            self.root = None
        elif father.right_child == node:
            father.right_child = None
        else:
            father.left_child = None

    def find_max(self):
        max_node = Node
        node = self.root
        while node is not None:
            max_node = node
            node = node.left_child
        return max_node.key

    def clear(self):
        self.root = None

    def __delitem__(self, key):
        self.remove(key)

    def __iter__(self):
        return BSTIterator(self.root)


class BSTIterator:
    def __init__(self, root):
        self.stack = Stack()
        self._push_left_elements(root)

    def _push_left_elements(self, root):
        self.stack.push(root)
        while self.stack.peek().left_child:
            self.stack.push(self.stack.peek().left_child)

    def __next__(self):
        if self.stack.is_empty():
            raise StopIteration
        next_node = self.stack.pop()
        if next_node.right_child:
            self._push_left_elements(next_node.right_child)
        return next_node.key
