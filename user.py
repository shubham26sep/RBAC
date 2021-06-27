class User:
    def __init__(self, username, is_admin=False):
        self.username = username  # username is unique across all users
        self.is_admin = is_admin
        self.roles = []  # an user will have multiple roles
