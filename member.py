class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def display_info(self):
        print(f"Name: {self.name}, Member ID: {self.member_id}")
