class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)

print(a.data)
print(a.next)
# print(a)
# print(int(0x0000025EF8316A50)) # this value came from print(a)
print(id(a))

print(b.data)
print(b.next)
# print(b)
#print(int(0x000002B2063ACCD0))
print(id(b))

print(c.data)
print(c.next)
# print(c) 
# print(int(0x000002B2063ACE10))
print(id(c))

#After creation with linked list
a.next = b
b.next = c
print(a.next)
print(b.next)
print(c.next)