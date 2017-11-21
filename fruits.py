class Fruit:

    count = 1

    def __init__(self, name, sweetness):
        self.name = name
        self.sweetness = sweetness
        self.id = Fruit.count
        Fruit.count += 1

    def __repr__(self):
        return f"Fruit #{self.id}; Name: {self.name}; Sweetness: {self.sweetness}"