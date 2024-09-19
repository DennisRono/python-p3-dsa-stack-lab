class Stack:
    def __init__(self, items=None, limit=None):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.limit is not None and len(self.items) >= self.limit:
            raise IndexError("Push to full stack")
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) == self.limit

    def search(self, target):
        try:
            index_from_top = len(self.items) - 1 - self.items[::-1].index(target)
            return len(self.items) - 1 - index_from_top
        except ValueError:
            return -1
