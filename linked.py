class Node:
    def __init__(self, item=None, id_element=None, next_item=None):
        self.items = item
        self.id = id_element
        self.next = next_item


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        self.id_element = 0


    def add(self, item):
        node = Node(item, self.id_element)

        if self.head:
            current = self.head

            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
        self.length += 1
        self.id_element += 1


    def __str__(self):
        res = ''

        nodes = self.head
        while nodes:
            res += str(nodes.items) + ', '
            nodes = nodes.next

        return 'LinkedList [' + res + ']'

    
    def __len__(self):
        return self.length


    def get_item(self, id_element):
        nodes = self.head

        while nodes:
            item = nodes.items
            if id_element == nodes.id:
                return item
            nodes = nodes.next


    def reverse(self):
        res = ''

        for num in range(self.id_element-1, -1, -1):
            res += str(self.get_item(num)) + ', '
            
        return 'LinkedList ['+res+']'
        


linked = LinkedList()
linked.add(1)
linked.add(2)


print(linked) # LinkedList [1,2, ]
print(linked.reverse()) # LinkedList [2,1, ]
print(linked.get_item(0)) # 1


