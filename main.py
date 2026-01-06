from service import user_service

username = input("username: ")
password = input("password: ")

auth = user_service(username,password)
auth.login()