class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):

        # create an empty linked list
        # when we have a empty linked list we have head = None
        self.head = None
        # n is number of nodes in a linked list 
        self.n = 0

    # get length of a linked list (here the length is the number of nodes in a liked list)
    # we will use the magical method __len__ to get the length
    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        # creation of a new node
        new_node = Node(value)
        # create connection
        new_node.next = self.head
        # reassign head
        self.head = new_node
        # increment node count
        self.n = self.n + 1 

    def append(self,value,):
        # assigning new node 
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return

        current = self.head
        # travesing in loop until nth node where current.next i.e. for eg we have 1,2,3,4
        # it will run as 1 checks if 1.next i.e. 2 has none if not continue at last
        # when it runs for 3 it observes that 4th node current.next = None 
        # then the 4th node is considered as current 
        while current.next != None:
            current = current.next
        # you are at the last node
        current.next = new_node
        self.n = self.n + 1
        
    def insert_after(self,after,value):
        new_node = Node(value)

        current = self.head
        while current != None:
            if current.data == after:
                break
            current = current.next
        # if we find the value in linked list then we enter this loop
        if current != None:
            new_node.next = current.next
            current.next = new_node
            self.n = self.n + 1
        else:  # for eg we have 4 elements in list but you insert_after(20,8) in this case you will not find the index
            # as self.n = 4 so to avoid this 
            return 'Item not found in list.'

    def clear(self):
        self.head = None
        self.n = 0
    
    def delete_head(self):
        if self.head == None:
            return 'Empty linked list'
    
        self.head = self.head.next
        self.n = self.n - 1

    def pop(self):
        current = self.head

        if self.head == None:
            return 'Empty Linked list'

        # only one element in linked list
        if current.next == None:
            return self.delete_head()

        while current.next.next != None:
            current = current.next

        # current = 2nd last node
        current.next = None
        self.n = self.n - 1

    def remove(self,value):

        current = self.head
        
        if self.head == None:
            return 'Empty linked list'

        if self.head.data == value:
            return self.delete_head()

        while current.next != None:
            if current.next.data == value:
                break
            current = current.next

        # 2 cases
        # if item not found
        if current.next == None:
            return 'Item not found'
        else: # if item found for eg we have 3,4,5 and we want to remvoe 4
            # to achieve this we need to wait at 3 i.e. 
            current.next = current.next.next

    def search(self,item):
        current = self.head
        pos = 0
        while  current != None:
            if current.data == item:
                return pos
            current = current.next
            pos = pos + 1

        return 'Item not found'


    def __getitem__(self,index):

        current = self.head
        pos = 0

        while current != None:
            if pos == index:
                return pos
            current = current.next
            pos = pos + 1

        return 'IndexError'


    # question
    def replace_max_withValue(self,value):
        temp = self.head
        max =  temp
        while temp != None:
            if temp.data > max.data :
                max = temp
            temp = temp.next
        max.data = value

    #
    def sum_odd_nodes(self):
        temp = self.head
        counter = 0
        result = 0
        while temp != None:
            if counter % 2 != 0:
                result = result + temp.data
            counter += 1
            temp = temp.next
        
        print(result)

    def __str__(self):

        current = self.head
        result = ''
        while current != None:
            result = result + str(current.data) + '->'
            current = current.next

        return result[:-2]


L = LinkedList()
print("Current length of linked list is",len(L))
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
print(len(L))
print("As we are using insert head we inserted a new head everytime so it shows 4 ,3, 2, 1 in in descending range")
print(L)

L.append(3)
print("Appending i.e. at the end of line")
print(L)
print("new length appending is ",len(L))
L.insert_after(3,15)
print('using insert_after')
print("new length after using insert_after is ",len(L))
print(L)
L.clear()
print('clearing the list')
print(L)
print("new length of list is ",len(L))

L.insert_head(5)
L.insert_head(4)
L.insert_head(3)
L.insert_head(2)
L.insert_head(1)

print('deleting head from linked list') 
L.delete_head()

print(L)
print('popping linked list')
L.pop()
print
