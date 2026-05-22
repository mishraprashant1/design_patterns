class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'{self.key}: {self.value}'


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, key, value):
        node = _Node(key, value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            temp = self.head
            node.next = temp
            temp.prev = node
            self.head = node
        return node

    def remove_tail(self):
        if not self.tail:
            return None

        tail = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = tail.prev
            self.tail.next = None
            tail.prev = None

        return tail

    def move_to_front(self, node):
        if self.head == node:
            return
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        if node_next:
            node_next.prev = node_prev
        else:
            self.tail = node_prev
        node.next = self.head
        self.head.prev = node
        node.prev = None
        self.head = node

    def delete_node(self, node):
        if not node:
            return
        if node == self.head:
            # h -> 1>2>3
            new_head = self.head.next
            if new_head:
                new_head.prev = None
            self.head = new_head
            return
        if node == self.tail:
            new_tail = self.tail.prev
            if new_tail:
                new_tail.next = None
            self.tail = new_tail
            return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def traverse_by_tail(self):
        temp = self.tail
        while temp:
            yield temp
            temp = temp.prev

    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        else:
            temp = self.current_node
            self.current_node = self.current_node.next
            return temp


class BaseCache(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def clear_cache(self):
        pass


class LRUCache(BaseCache):
    def __init__(self, size=3, linked_list=None):
        if size < 1:
            raise ValueError("size must be >= 1")
        if linked_list is None:
            linked_list = DoublyLinkedList()
        self.ll = linked_list
        self.size = size
        self.cache = {}
        self._lock = RLock()

    def set(self, key, value):
        """
        insert the element in cache dict
        put it in the linked list
        """
        with self._lock:
            if key in self.cache:
                node = self.cache[key]
                node.value = value
                self.ll.move_to_front(node)
                return
            if len(self.cache) >= self.size:
                tail = self.ll.remove_tail()
                key = tail.key
                del self.cache[key]
            node = self.ll.prepend(key, value)
            self.cache[key] = node

    def get(self, key):
        """
        fetch the element from the cache dict
        put the node of the key at the start
        """
        with self._lock:
            node = self.cache.get(key)
            if node:
                self.ll.move_to_front(node)
                return node.value
            return None

    def delete(self, key):
        with self._lock:
            node = self.cache.get(key)
            if not node:
                return
            self.ll.delete_node(node)
            del self.cache[key]

    def clear_cache(self):
        with self._lock:
            for key in self.cache.keys():
                self.delete(self.cache[key])
            self.ll = DoublyLinkedList()
            self.cache = {}

    def __contains__(self, key):
        return key in self.cache

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __len__(self):
        return len(self.cache)


cache = LRUCache(5)
cache.set(3, 30)
cache.set(4, 40)
cache.set(5, 50)
cache.set(6, 60)
cache.set(7, 70)
cache.set(8, 80)
print(cache.get(3))
print('-' * 10)
for i in cache.ll.traverse_by_tail():
    print(i)
