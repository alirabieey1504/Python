print("welcome to your app(manage password user)")

username = input("please enter username :")
password = input("please enter password :")
print("saved")
usernamel = input("please enter username :")
passwordl = input("please enter password :")
if username == usernamel and password == passwordl:
    print("login with success")
elif username != usernamel:
    print("username wrongly!")
elif password != passwordl:
    print("password wrongly!")
