
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        count = 0
        while cur.next != None:
            cur = cur.next
            count += 1
        return count

    def display(self):
        cur = self.head
        ll_text = "[head]-->"
        while cur.next != None:
            cur = cur.next
            ll_text += f"[{cur.data}]-->"
        ll_text += "None"
        print(ll_text)

    def get(self, pos):
        if pos > self.length():
            return "The index exceeds the maximum index of the Linked List"
        i = 0
        cur = self.head
        while True:
            cur = cur.next
            if i == pos:
                return cur.data
            i += 1

    def erase(self, pos):
        if pos > self.length():
            return "The index exceeds the maximum index of the Linked List"
        i = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if i == pos:
                last_node.next = cur.next
                return
            i += 1


if __name__ == '__main__':
    ll = linked_list()
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    print(ll.length())
    ll.display()
    print(ll.get(3))
    print(ll.get(5))
    ll.erase(1)
    ll.display()
