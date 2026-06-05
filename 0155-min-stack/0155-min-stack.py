class MinStack:

    def __init__(self):
        self.st = []
        self.st2 = []

    def push(self, val: int) -> None:
        self.st.append(val)

        if not self.st2 or val <= self.st2[-1]:
            self.st2.append(val)

    def pop(self) -> None:
        if not self.st:
            return

        ele = self.st.pop()

        if ele == self.st2[-1]:
            self.st2.pop()

    def top(self) -> int:
        if not self.st:
            return -1

        return self.st[-1]

    def getMin(self) -> int:
        if not self.st2:
            return -1

        return self.st2[-1]