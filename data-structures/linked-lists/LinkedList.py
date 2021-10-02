class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 

    def __repr__(self):
        return "Node({})".format(self.val)



class LinkedList:
    def __init__(self, nodes = None):
        self.head = None # first node of list
        if nodes is not None:
            curr = Node(val = nodes.pop(0))
            self.head = curr
            for e in nodes:
                curr.next = Node(val = e)
                curr = curr.next

    def __repr__(self):
        curr = self.head
        nodes = []
        while curr is not None:
            nodes.append(curr.val)
            curr = curr.next
        return " -> ".join(nodes)

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr
            curr = curr.next

    def insert_at_start(self, node_val):
        node = Node(node_val)
        node.next = self.head
        self.head = node
    
    def insert_at_end(self, node_val):
        node = Node(node_val)
        if self.head is None: # if linked list is empty
            self.head = node
            return
        for curr in self:
            pass
        curr.next = node

    def remove_at_start(self):
        if self.head is None:
            raise Exception("Emtpy list")
        self.head = self.head.next

    def remove_at_end(self):
        if self.head is None:
            raise Exception("Empty list")
        curr = self.head
        while curr.next.next is not None: # iterate to the second last node
            curr = curr.next
        curr.next = None 


if __name__ == "__main__":
    ll = LinkedList(["a", "b", "c"])
    print(ll)

    ll.insert_at_start("start")
    ll.insert_at_end("end")
    print(ll)

    ll.remove_at_start()
    ll.remove_at_end()
    print(ll)