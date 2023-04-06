from debug import debug


class Scoreboard:
    def __init__(self):
        self.count = 0
        self.score = 0

    def tick(self):
        self.count += 1
        self.score = int(self.count / 60)

    def display(self):
        debug(self.score)

    def increase_difficulty(self):
        pass
