
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        pos = 1
        if self.head:
            while pos <= position:
                if pos == position:
                    return current
                if current.next:
                    current = current.next
                    pos += 1
        return None

    def insert(self, new_element, position):
        cur = self.head
        prev = self.head
        pos = 1
        while cur:
            if pos == position:
                if cur == self.head:
                    self.head = new_element
                    new_element.next = cur
                if cur == None:
                    prev.next = new_element
                else:
                    new_element.next = cur
                    prev.next = new_element
                break
            else:
                prev = cur
                cur = cur.next
                pos += 1

    def delete(self, value):
        cur = self.head
        while cur:
            if self.head.value == value:
                self.head = cur.next
            elif cur.next and cur.next.value == value:
                if cur.next.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
            cur = cur.next



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
