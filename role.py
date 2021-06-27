class Role:
    def __init__(self, role_id, name):
        self.role_id = role_id
        self.name = name
        self.action_types = set()  # action types valid for a role
        self.resources = set()  # resource access for a role
