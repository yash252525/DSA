import sys 

# L = []

# print(f"{sys.getsizeof(L)} Starting size")
# L.append("Yash")
# print(sys.getsizeof(L))
# L.append("Zore")
# print(sys.getsizeof(L))
# L.append("1")
# print(sys.getsizeof(L))
# L.append("2")
# print(sys.getsizeof(L))
# L.append("3")
# print(sys.getsizeof(L))
############

# list = []

# for i in range(1,101):
#     print(i, sys.getsizeof(list))
#     list.append(i)

############

import ctypes

class MyList:
    def __init__(self):
        self.size = 1  # maximum items you can store
        self.n = 0  # present items in dynamic array
        self.A = self.__make_array(self.size)
    ## magic method __len__            
    def __len__(self):
        return self.n
    ## magic method __str__
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        
        return '[' + result[:-1] + ']'
    
    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'Index Error - Index out of range.'
    
    def append(self,item):
        if self.n == self.size:
            # resize
            self.__resize(self.size*2)

        #append
        self.A[self.n] = item
        self.n = self.n + 1 

    def pop(self):
        if self.n == 0:
            return 'Empty List'
        
        print(self.A[self.n - 1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def remove(self,item):
        pos = self.find(item)

        if type(pos) == int:
            #delete
            self.__delitem__(pos)
        else:
            return pos

    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        
        return 'ValueError - item not in list'

    def __resize(self,new_capacity):
        # create a array with new capacity 
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        #copy the previous array to new array
        for i in range(self.n):  
            B[i] = self.A[i]
        self.A = B

    def insert(self,position,item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,position,-1):
            self.A[i] = self.A[i-1]

        self.A[position] = item
        self.n = self.n + 1

    def __delitem__(self,position):
        if 0 <= position < self.n :
            for i in range(position,self.n-1):
                self.A[i] = self.A[i+1]
        
        self.n = self.n - 1


    def __make_array(self,capacity):
        # creates a C type array(static,referential) with size capacity
        return(capacity*ctypes.py_object)()
    
Object_List = MyList()
print(Object_List)
print(type(Object_List))
print(f"Length of list before adding any object in array {len(Object_List)}")
Object_List.append("Hello")
Object_List.append("Yash")
Object_List.append("25")
Object_List.append("True")
print(f"Length of list after adding 4 objects in array {len(Object_List)}")

print(Object_List)
print(Object_List[1])
print(f"{Object_List} before popping, having {len(Object_List)} elements")
Object_List.pop()
print(f"{Object_List} after popping, having {len(Object_List)} elements")

print("Clearing list")
print(f"length of list before is {len(Object_List)}")
Object_List.clear()
print(f"length of list after is {len(Object_List)}")

Object_List.append("Hello")
Object_List.append("Yash")
Object_List.append("25")
Object_List.append("True")

print('Finding in list')
print(len(Object_List))
print(f"Value found in list at index {Object_List.find('Yash')}")

print('Insertion in list ')
Object_List.insert(1,"World")
print(Object_List)

print('Deletion of an element from list.')
print(Object_List)
del Object_List[2]
print(Object_List)



