# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        return hash(key)

    def _hash_djb2(self, key):
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash

    def _hash_mod(self, key):
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        brownie = self._hash_mod(key)
        node = self.storage[brownie]

        #if no node is found create a new node
        #or if key is the same, overwrite current node with new node
        if node is None or node.key == key:
            self.storage[brownie] = LinkedPair(key, value)
        else:
            while True:
                if node.next is None or node.key == key:
                    node.next = LinkedPair(key, value)
                    break
                node = node.next

    def remove(self, key):
        brownie = self._hash_mod(key)
        node = self.storage[brownie]
        prev = None
        while node.next is not None and node.key != key:
            prev = node
            node = node.next
        if prev is None:
            self.storage[brownie] = node.next
        else:
            prev.next = node.next

    def retrieve(self, key):
        brownie = self._hash_mod(key)
        node = self.storage[brownie]
        if node == None: return None
        while True:
            if node.key == key:
                return node.value
            node = node.next

    def resize(self):
        self.capacity *= 2
        old = self.storage
        self.storage = [None] * self.capacity
        for o in old:
            node = o
            while node is not None:
                self.insert(node.key, node.value)
                node = node.next

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
