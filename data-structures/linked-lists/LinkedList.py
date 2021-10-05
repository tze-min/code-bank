'''
Time complexity
- inserting/deleting at start: O(1)
- inserting/deleting before/after a node or at the end: O(n)

'''


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

    def insert_after_node(self, node_val, after_val): # 3-4-5-7 # insert 6 after 5
        '''Asssumptions:
        - Each node in the linked list has a unique value, or we're simply adding the new node after the first node that's found to contain after_val
        - Linked list contains after_val
        '''
        if self.head is None:
            raise Exception("Empty list")
        curr = self.head
        while curr.val != after_val: # curr: 5
            curr = curr.next
        inserted = Node(node_val)
        inserted.next = curr.next
        curr.next = inserted 

    def insert_before_node(self, node_val, before_val): # 3-4-6-7 # insert 5 before 6
        '''Asssumptions:
        - Each node in the linked list has a unique value, or we're simply adding the new node after the first node that's found to contain after_val
        - Linked list contains after_val
        '''
        if self.head is None:
            raise Exception("Empty list")
        curr = self.head
        while curr.next.val != before_val: # curr: 4
            curr = curr.next
        inserted = Node(node_val)
        inserted.next = curr.next
        curr.next = inserted

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

    def remove(self, node_val): # 3-4-5-6 # remove 5
        '''Assumptions:
        - Linked list contains node_val
        '''
        if self.head is None:
            raise Exception("Empty list")
        if self.head.val == node_val: # if you're removing at start
           self.head = self.head.next
           return
        curr = self.head
        while curr.next.val != node_val: # curr: 4
            curr = curr.next
        curr.next = curr.next.next

        

if __name__ == "__main__":
    ll = LinkedList(["a", "b", "c"])
    print(ll)

    ll.insert_at_start("start")
    ll.insert_at_end("end")

    ll.remove_at_start()
    ll.remove_at_end()

    ll.insert_after_node("a1", "a")
    print(ll)
    ll.insert_before_node("b1", "c")
    print(ll)
    ll.remove("a")
    print(ll)