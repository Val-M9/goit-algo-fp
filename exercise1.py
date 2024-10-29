class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse_list(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def sort(self):
        cur = self.head
        while cur:
            next_node = cur.next
            while next_node:
                if cur.data > next_node.data:
                    cur.data, next_node.data = next_node.data, cur.data
                next_node = next_node.next
            cur = cur.next

    def merge_lists(self, income_list):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = income_list
        self.sort()

    def print_list(self):
        current = self.head
        while current:
            print(f'{current.data}', end=' ')
            current = current.next


llist = LinkedList()
llist.insert_at_end(7)
llist.insert_at_end(11)
llist.insert_at_end(8)
llist.insert_at_end(23)
llist.insert_at_end(42)

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)
llist2.insert_at_end(8)
llist2.insert_at_end(10)

llist.print_list()
llist.sort()
print('\nAfter sorting')
llist.print_list()
llist.merge_lists(llist2.head)
print('\nAfter merging')
llist.print_list()
