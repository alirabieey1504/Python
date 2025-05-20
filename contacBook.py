print("welcome to your contact book")

concat = []
while 1:
    print("1. add a new contact")
    print("2. show all contacts")
    print("3. search contacts")
    print("4. delete contacts")
    print("5. exit")
    number = int(input("choose an option (1-5) :"))
    if number == 1:
        name = input("please enter name :")
        phone = int(input("please enter phone :"))

        concat.append({"name": name, "phone": phone})
    elif number == 2:
        print(concat)
    elif number == 3:
        basedOn = int(
            input("do you wanna to be based on name or phone (name==1/phone==2)")
        )
        if basedOn == 1:
            nameSearch = input("please enter the name you are looking for ")
            results = [c for c in concat if c["name"] == nameSearch]
            print(results)
        elif basedOn == 2:
            phoneSearch = int(
                input("please enter the phone you are looking for whitout ziro")
            )
            results = [c for c in concat if c["phone"] == phoneSearch]
            print(results)

        else:
            print("wrongly")
    elif number == 4:
        dodelete = input("do you wanna all delete ?if yes please enter y/n :")
        if dodelete == "y":
            concat.clear()
        else:
            name = input("please enter the desired name to be deleted  :")
            index_list = [i for i, c in enumerate(concat) if c["name"] == name]
            if index_list is not None:
                del concat[index_list[0]]
            else:

                print(concat)

    elif number == 5:
        break
    # print(concat)
