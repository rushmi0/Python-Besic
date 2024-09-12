

if __name__ == "__main__":

    u = "Thai"
    p = "Samsung"
    num = 0
    for i in range(3):
        username = input("enter your username : ")
        password = input(" enter your password : ")
        if username == u and password == p:
            print("Success")
            break
        else:
            print("Incorrect")
            num += 1
    if num == 3:
        print("your account is lock")