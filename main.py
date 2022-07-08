class User:
    def __init__(self, userId, username):
        self.id = userId
        self.username = username
        self.following = 0
        self.followers = 0
    def follow(self, user):
        user.followers += 1
        self.following +=1

user1 = User('1', 'Salad')
user2 = User('2', "Sauce")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)