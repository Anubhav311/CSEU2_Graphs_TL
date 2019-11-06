class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.storage > 0:
            return self.storage.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.storage)


def earliest_ancestor(ancestors, starting_node):
    pass