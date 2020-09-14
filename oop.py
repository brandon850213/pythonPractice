class PlayerName:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(
            f'Player {self.name} is playing, he/ she is {self.age} years old.')


Player1 = PlayerName('brandon', 24)

Player1.shout()
