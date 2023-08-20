class Node:
    def __init__(self):
        self.value = None
        self.next = None
class LinkedList:
    def __init__(self):
            self.head = Node() 
    def add(self,value):
        if self.head.value is None:
                self.head.value = value
                return
            
        temp = Node()
        temp.value = value
        current_node = self.head
            # 1 variant
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = temp

        # 2 variant
        #temp.next = self.head
        #self.head = temp    
    
    def length(self):
        if self.head.value is None:
            size = 0
        else:
            size = 1
        current_node = self.head    
        while current_node.next is not None:
            current_node = current_node.next
            size += 1
        return size  

    def find(self, value):  
        if self.head.value is not None:
            if self.head.value == value:
                return True 
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            if current_node.value == value:
                return True
        return False
    
    def find_node(self,value):
        pass

    def print(self):
        if self.head.value is None:
            print("Empty Linked List")
            return
        
        print(self.head.value, end=" ")    
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            print(current_node.value, end=" ")
        print()     

ll = LinkedList()
print (ll.length())
print(ll.find(0), ll.find(9), ll.find(6))
ll.print()
ll.add(9)
print (ll.length())
print(ll.find(0), ll.find(9), ll.find(6))
ll.print()
ll.add(7)
print (ll.length())
print(ll.find(0), ll.find(9), ll.find(6))
ll.print()
ll.add(6)
print (ll.length())
print(ll.find(0), ll.find(9), ll.find(6))
ll.print()
ll.add(4)
print (ll.length())
print(ll.find(0), ll.find(9), ll.find(6))
ll.print()
ll.add(9)
print (ll.length())
print(ll.find(0), ll.find(9), ll.find(6))
ll.print()
ll.add(19)
print (ll.length())
print(ll.find(0), ll.find(9), ll.find(6))
ll.print()
ll.add(0)
print (ll.length())
print(ll.find(0), ll.find(9), ll.find(6))
ll.print()
a = 10