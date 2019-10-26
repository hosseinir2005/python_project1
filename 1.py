a = dict(name = "hossein" , family = "ghale bandi" , age = 15 , email = "hossein.ir2005@gmail.com")
input1 = input("what do you want?")
while True:
    if input1 in ["name"]:
        print(a.get("name"))
        break
    elif input1 in ["family"]:
        print(a.get("family"))
        break
    elif input1 in ["age"]:
        print(a.get("age"))
        break
    elif input1 in ["email"]:
        print(a.get("email"))
        break
    elif input1 in ["q" , "quit"]:
        break
    else:
        print("wrong cammend!!!")
        break