class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):

        self.top = None


    def isempty(self):
        return self.top == None  # will return true or false
    
    def push(self,value):

        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node 

    def traverse(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next

    def peek(self):
        if(self.isempty()):
            return 'Empty Stack'
        else:
            return self.top.data
        
    def pop(self):
        if(self.isempty()):
            return 'Empty Stack'
        else:
            self.top = self.top.next

    


def reverse_string(text):
    s = Stack()

    for i in text:
        s.push(i)
        
    

# s = Stack()
# print(s.isempty())
# s.push(3)
# print(s.isempty())
# s.push(4)
# s.push(5)
# s.push(6)
# s.traverse()


# def reservse_string(text):
#     s = Stack()
#     for i in range(text):
#         s.push(i)

#     result = ""
#     for i in range (len(text)):
#         result = result + s.pop()

#     print(result)

# reservse_string("Hello")

# string = 'hello'
# empty = []
# for i in range (len(string)):
#     empty.append(string[i])

# print(empty)
        

       
        
    









