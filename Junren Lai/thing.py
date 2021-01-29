"""Thing class"""


class Thing:
    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def process(self, i):
        self.value += len(self.name) * i

    def __str__(self):
        return "I'm {} ({})".format(self.name, self.value)
