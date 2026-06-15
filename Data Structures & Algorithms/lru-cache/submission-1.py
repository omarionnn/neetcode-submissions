class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Maps key -> Node object

        # Initialize sentinel dummy nodes
        self.left = Node(0, 0)   # Least Recently Used (LRU) side
        self.right = Node(0, 0)  # Most Recently Used (MRU) side
        
        # Link sentinels together
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        """Surgically extract a node from its current position in the list."""
        prev_node = node.prev
        nxt_node = node.next
        
        prev_node.next = nxt_node
        nxt_node.prev = prev_node

    def insert(self, node: Node) -> None:
        """Always insert the node at the most recently used position (right before self.right)."""
        prev_node = self.right.prev
        nxt_node = self.right
        
        # 1. Point the new node to its neighbors
        node.prev = prev_node
        node.next = nxt_node
        
        # 2. Update the neighbors to point to the new node
        prev_node.next = node
        nxt_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Since it was accessed, promote it to Most Recently Used
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value in-place and promote it
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            # Create a brand new node and add to cache/list
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert(new_node)

            # Evict the least recently used node if we exceed capacity
            if len(self.cache) > self.cap:
                lru_node = self.left.next
                self.remove(lru_node)
                del self.cache[lru_node.key]