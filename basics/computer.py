class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config : ", self.cpu, self.ram)


if __name__ == "__main__":
    comp1 = Computer("i5", 16)
    comp2 = Computer("i3", 8)

    comp1.config()
    comp2.config()
