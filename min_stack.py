class MinStack:
    def __init__(self):
        self.min = []
        self.dList = []

    def push(self, x):
        self.dList.append(x)

        if not self.min:
            self.min.append(x)
        elif saelf.min[-1] > x:
            self.min.append(x)

    def pop(self):
        if not self.dList:
            return -1
        else:
            node = self.dList.pop()
            if node == self.min[-1]:
                self.min.pop()

            new_list = self.dList.copy()
            self.dList = new_list

            return node

    def top(self):
        if not self.dList:
            return -1
        else:
            return self.dList[-1]

    def get_min(self):
        if not self.min:
            return -1
        else:
            return self.min[-1]


if __name__ == '__main__':
    stack = MinStack()

    # stack.push(1)

    # stack.push(2)
    # stack.push(3)
    # stack.push(4)
    # stack.push(5)
    print(stack.pop())
    # print(stack.top())
    # print(stack.get_min())
