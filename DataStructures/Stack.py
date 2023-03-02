class Stack():
    def __init__(self,size):
        self.size=size
        self._stack=[None]*self.size
        self.top=-1
    
    def is_full(self):
        return self.top == self.size-1
    
    def is_empty(self):
        return self.top == -1
    
    def show(self):
        if not self.is_empty():
            print(self._stack,self._stack[:self.top+1],self.top)
        else:
            print(self._stack,"Stack is empty")
    
    def push(self,item):
        if not self.is_full():
            self.top+=1
            self._stack[self.top]=item
            print(f"{item} added to Stack")
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            item=self._stack[self.top]
            self.top-=1
            print(f"{item} removed from Stack")
        else:
            print("Stack is empty")
            


# s=Stack(5)
# s.show()
# s.is_full()
# s.is_empty()
# s.pop()
# s.push(1)
# s.push(2)
# s.show()
# s.push(3)
# s.push(9)
# s.show()
# s.pop()
# s.show()
# s.push(4)
# s.push(5)
# s.push(6)
