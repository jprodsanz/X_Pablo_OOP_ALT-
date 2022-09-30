class Player:
    def __init__(self, first_name, last_name, rating):
        self.first_name = first_name
        self.last_name = last_name
        self.rating = rating

player1 = Player('Cristiano', 'Ronaldo', 99)
print(player1.first_name)
print(player1.last_name)
print(player1.rating)

