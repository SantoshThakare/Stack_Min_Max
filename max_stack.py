class MaxStack:
    def __init__(self):
        self.stack = []
        self.stack_max = []

    def push(self, x: int):
        self.stack.append(x)
        if not self.stack_max or x > self.stack_max[-1][0]:
            self.stack_max.append([x, 1])
        elif x == self.stack_max[-1][0]:
            self.stack_max[-1][1] += 1
        else:
            self.stack_max.append(self.stack_max[-1])

    def pop(self):
        if not self.stack_max or self.stack:
            return
        if self.stack_max[-1][0] == self.stack[-1]:
            self.stack_max[-1][1] -= 1
        if self.stack_max[-1][1] == 0:
            del self.stack_max[-1]
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def peekMax(self):
        if self.stack_max:
            return self.stack_max[-1][0]

    def popMax(self):
        if self.stack_max:
            return self.stack_max.pop()[0]


if __name__ == '__main__':
    obj = MaxStack()
    obj.push(1)
    obj.push(5)
    obj.push(4)
    obj.push(3)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.peekMax()
    param_5 = obj.popMax()
    print(param_3)
    print(param_4)
    print(param_5)