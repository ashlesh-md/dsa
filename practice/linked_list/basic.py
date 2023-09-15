class Node:
    def __init__(self , data , next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self , data):
        node = Node(data , self.head)
        self.head = node

    def insert_at_end(self , data):
        node = self.head
        while node:
            if not node.next:
                node.next = Node(data)
                break
            node = node.next

    def print(self):
        node = self.head
        if not node:
            print("Linked List is empty")
        result = ""
        while node:
            result += str(node.data) + '-->'
            node = node.next

        print(result[:-3])

    def length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def remove_at(self , index):
        node = self.head
        count = 0
        if self.length() < index:
            print("Invalid Index")
            return

        if self.length() == 0:
            print("Empty")
            return

        if index == 0:
            self.head = self.head.next
            return
        while node:
            if count == index - 1:
                node.next = node.next.next
                break
            count += 1
            node = node.next

    def insert_at(self , index , data):
        node = self.head
        count = 0
        if self.length() < index:
            print("Invalid Index")
            return

        if index == 0:
            self.insert_at_beginning(data)
            return

        while node:
            if count == index - 1:
                node.next = Node(data , node.next)
                return
            count += 1
            node = node.next

    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev


    def reverse_recursion(self, head):
        if not head or not head.next:
            return head

        rest = self.reverse_recursion(head.next)

        head.next.next = head
        head.next = None

        return rest


    def rotateRight(self, k):
        if k == 0 or not self.head:
            return self.head

        temp = self.head
        length = 1

        while temp.next:
            temp = temp.next
            length += 1

        temp.next = self.head

        k = k % length

        for _ in range(length - k):
            temp = temp.next

        self.head = temp.next
        temp.next = None

        return self.head



if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(30)
    linked_list.insert_at_end(40)
    linked_list.insert_at_end(50)
    linked_list.insert_at_end(60)

    linked_list.print()

    linked_list.rotateRight(2)

    linked_list.print()

    # linked_list.reverse()
    # linked_list.print()


    # linked_list.head  =  linked_list.reverse_recursion(linked_list.head)
    # linked_list.print()

