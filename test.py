from models import Users

users = Users.find({})

for user in users:
    print(user)