class User:
    def __init__(self, userId, username):
        self.id = userId
        self.username = username
        self.followers = 0

user1 = User('2', 'Salad sauce')

print(user1.username)