class Iterator:
    def __init__(items):
        self.index = 0
        self.items = []

    def has_next():
        return self.index < self.items.length - 1

    def next():
        if self.hasNext():
           self.index += 1
        return self.current()

    def songs():
        pass

    def prev():
        if self.index != 0:
            self.index -= 1
        return self.current()

    def current():
        return self.items[self.index]

    

