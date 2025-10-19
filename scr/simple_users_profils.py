# create simple users

class simple_user():
    def __init__(self,name:str,surname:str,tags:list):
        self.name = name
        self.surname = surname
        self.tags = tags

    def display_users(self):
        print(f'User {self.name} {self.surname} is intrested in articles {self.tags}\n')

    # recommenting articles

