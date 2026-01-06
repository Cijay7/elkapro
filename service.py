class user_service:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.data = {
            "justin" : {
            "username" : "justin",
            "password" : "12345",
            "role" : "member"
            },
            "obin" : {
            "username" : "obin",
            "password" : "12345",
            "role" : "atmin"
            }
        }


    def check_password(self):
        for value in self.data:
            if value == self.username:
                get_data_user = self.data[value]
        if self.password == get_data_user['password']:
            return get_data_user
        else:
            return False

    def login(self):
        data = self.check_password()
        if data:
            print("\nWelcome", data['username'])
            print("Logged in as:", data['role'])
        else:
            print("\nInvalid Login!\n")