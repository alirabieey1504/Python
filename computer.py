class computer:
    count = 0

    def __init__(self, ram, hard, cpu):
        self.ram = ram
        self.hard = hard
        self.cpu = cpu

    def value(self):
        return self.ram + self.hard + self.cpu


class laptop(computer):
    adapter = 1

    # overwrite in value method
    def value(self):
        return self.ram + self.hard + self.cpu + self.size


pc1 = computer(12, 2, 4)
pc2 = computer(8, 4, 11)
print(pc2.value())
print(pc1.value())
laptop1 = laptop(123, 4143, 14)
laptop1.size = 12
print(laptop1.value())
