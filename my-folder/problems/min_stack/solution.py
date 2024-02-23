class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]

min_stack = MinStack()
result = []

commands = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
values = [[], [-2], [0], [-3], [], [], [], []]

for i in range(len(commands)):
    if commands[i] == "MinStack":
        min_stack = MinStack()
        result.append(None)
    elif commands[i] == "push":
        min_stack.push(values[i][0])
        result.append(None)
    elif commands[i] == "pop":
        min_stack.pop()
        result.append(None)
    elif commands[i] == "top":
        result.append(min_stack.top())
    elif commands[i] == "getMin":
        result.append(min_stack.getMin())
