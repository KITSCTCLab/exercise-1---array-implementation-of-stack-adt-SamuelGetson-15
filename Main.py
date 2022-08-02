class Stack:
    def __init__(self, size):
       self.size = size
       self.lst = [None]*size
       self.top = -1 

    def is_empty(self):
        # Write code here
        if self.top == -1 :
            return 1
        else :
            return 0

    def is_full(self):
        # Write code here
        if self.top == (self.size - 1) :
            return 1
        else :
            return 0

    def push(self, data):
        if not self.is_full():
            # Write code here
            self.top+=1
            self.lst[self.top]=data

    def pop(self):
        if not self.is_empty():
            # Write code here
            del self.lst[self.top]
            self.top-=1
            

    def status(self):
        # Write code here
         if not self.is_empty():
            for i in range(0,self.top+1):
                print(self.lst[i])

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
