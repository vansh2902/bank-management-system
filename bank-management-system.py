print("----Welcome to Vansh Bank----")
print("")

customers = []
manager = []

while True:

    print("1. sing up")
    print("2. already have an account log in")
    print("3. log in as manager")
    print("4. exit")

    choice = int(input("enter your choice : "))

    if choice == 1:

        print("----sign up----")

        name = input("enter your full name : ")

        while True:
            phone_no = input("enter your phone no. : ")

            if phone_no.isdigit() and len(phone_no) == 10:
                break
            else:
                print("please enter valid phone number")

        address = input("enter your address : ")

        while True:
            type_of_ac = input(
                "enter your type of account Saving or Current : "
            ).upper()

            if type_of_ac == "SAVING" or type_of_ac == "CURRENT":
                break
            else:
                print("enter valid type of account")

        while True:

            user_name = input("create user name : ")

            user_name_exists = False

            for customer in customers:
                if user_name == customer["user name"]:
                    user_name_exists = True
                    break

            if user_name_exists:
                print("user name already exists, try another")
            else:
                break

        while True:

            user_pass = input("create password : ")
            re_pass = input("enter your pass again : ")

            if user_pass == re_pass:
                break
            else:
                print("password mismatch")

        customer = {
            "name": name,
            "phone no": phone_no,
            "address": address,
            "type of account": type_of_ac,
            "user name": user_name,
            "user pass": user_pass,
            "balance": 0,
            "transactions": []
        }

        customers.append(customer)

        print("successfully create an account")


    elif choice == 2:

        print("----Log In----")

        while True:

            log_in_user_name = input("enter your user name : ")
            log_in_pass = input("enter your pass : ")

            logged_in_customer = None

            for customer in customers:

                if (
                    log_in_user_name == customer["user name"]
                    and log_in_pass == customer["user pass"]
                ):
                    logged_in_customer = customer
                    break

            if logged_in_customer is not None:
                print("log in successful")
                break
            else:
                print("wrong username or password")


        while True:

            print("\n1.profile")
            print("2.deposit")
            print("3.withdrawl")
            print("4.check balance")
            print("5.transfer money")
            print("6.transaction history")
            print("7.logout")

            choice = int(input("enter your choice : "))


            if choice == 1:

                print("Name:", logged_in_customer["name"])
                print("Phone:", logged_in_customer["phone no"])
                print("Address:", logged_in_customer["address"])
                print("Account Type:", logged_in_customer["type of account"])
                print("Balance:", logged_in_customer["balance"])


            elif choice == 2:

                amount = float(input("how much amount do you want to deposit : "))

                if amount <= 0:
                    print("enter valid amount")
                else:
                    logged_in_customer["balance"] += amount

                    logged_in_customer["transactions"].append(
                        f"deposited {amount}"
                    )

                    print("amount added successfully")


            elif choice == 3:

                amount = float(input("how much amount do you want to withdraw : "))

                if amount <= 0:
                    print("enter valid amount")

                elif logged_in_customer["balance"] < amount:
                    print("insufficient balance")

                else:
                    logged_in_customer["balance"] -= amount

                    logged_in_customer["transactions"].append(
                        f"withdrawn {amount}"
                    )

                    print("withdrawl successfully")


            elif choice == 4:

                print("your balance :", logged_in_customer["balance"])


            elif choice == 5:

                user_name = input(
                    "enter user name for whome to transfer money : "
                )

                amount = float(
                    input("how much amount do you want to transfer : ")
                )

                if amount <= 0:
                    print("enter valid amount")

                elif amount > logged_in_customer["balance"]:
                    print("insufficient balance")

                elif user_name == logged_in_customer["user name"]:
                    print("you cannot transfer money to yourself")

                else:

                    receiver_found = False

                    for customer in customers:

                        if customer["user name"] == user_name:

                            customer["balance"] += amount
                            logged_in_customer["balance"] -= amount

                            logged_in_customer["transactions"].append(
                                f"transferred {amount} to {user_name}"
                            )

                            customer["transactions"].append(
                                f"received {amount} from "
                                f"{logged_in_customer['user name']}"
                            )

                            receiver_found = True

                            print("successfully transfer money")
                            print(
                                "your balance :",
                                logged_in_customer["balance"]
                            )

                            break

                    if receiver_found == False:
                        print("customer not found")


            elif choice == 6:

                print("----Transaction History----")

                if len(logged_in_customer["transactions"]) == 0:
                    print("no transactions yet")

                else:

                    for transaction in logged_in_customer["transactions"]:
                        print("-", transaction)


            elif choice == 7:

                print("customer logged out")
                break

            else:
                print("invalid choice")


    elif choice == 3:

        print("----Manager log in----")
        print("1. signup")
        print("2. already a manager log in")

        manager_choice = int(input("enter your choice : "))


        if manager_choice == 1:

            manager_name = input("enter manager name : ")

            while True:

                manager_phone = input("enter manager phone no : ")

                if manager_phone.isdigit() and len(manager_phone) == 10:
                    break
                else:
                    print("please enter valid phone no")


            while True:

                manager_user_name = input("enter user name : ")

                manager_exists = False

                for manager_dict in manager:

                    if manager_user_name == manager_dict["manager user name"]:
                        manager_exists = True
                        break

                if manager_exists:
                    print("user name already exists")
                else:
                    break


            while True:

                manager_user_pass = input("enter pass : ")
                re_pass = input("enter pass again : ")

                if manager_user_pass == re_pass:
                    break
                else:
                    print("password mismatch")


            manager_dict = {
                "manager name": manager_name,
                "manager phone": manager_phone,
                "manager user name": manager_user_name,
                "manager user password": manager_user_pass
            }

            manager.append(manager_dict)

            print("manager signup successfully")


        elif manager_choice == 2:

            manager_log_username = input("enter manager user name : ")
            manager_log_pass = input("enter manager user pass : ")

            logged_in_manager = None

            for manager_dict in manager:

                if (
                    manager_dict["manager user name"] == manager_log_username
                    and manager_dict["manager user password"] == manager_log_pass
                ):
                    logged_in_manager = manager_dict
                    break

            if logged_in_manager is None:
                print("wrong user name and password")

            else:

                print("log in successfully")

                while True:

                    print(
                        f"---welcome {logged_in_manager['manager name']}---"
                    )

                    print("1.view all customers")
                    print("2.search customer")
                    print("3.delete customer account")
                    print("4.view total bank balance")
                    print("5.view all transactions")
                    print("6.logout")

                    manager_choice = int(input("enter your choice : "))


                    if manager_choice == 1:

                        if len(customers) == 0:
                            print("no customers")

                        else:

                            for customer in customers:

                                print("----------------")
                                print("Name:", customer["name"])
                                print("Username:", customer["user name"])
                                print("Phone:", customer["phone no"])
                                print(
                                    "Account Type:",
                                    customer["type of account"]
                                )
                                print("Balance:", customer["balance"])


                    elif manager_choice == 2:

                        customer_name = input(
                            "enter customer user name : "
                        )

                        customer_found = False

                        for customer in customers:

                            if customer_name == customer["user name"]:

                                print("Name:", customer["name"])
                                print("Phone:", customer["phone no"])
                                print(
                                    "Account Type:",
                                    customer["type of account"]
                                )
                                print("Balance:", customer["balance"])

                                customer_found = True
                                break

                        if customer_found == False:
                            print("customer not found")


                    elif manager_choice == 3:

                        remove_customer = input(
                            "enter customer user name : "
                        )

                        customer_found = False

                        for customer in customers:

                            if remove_customer == customer["user name"]:

                                customers.remove(customer)

                                customer_found = True

                                print("customer account deleted")
                                break

                        if customer_found == False:
                            print("customer not found")


                    elif manager_choice == 4:

                        total_balance = 0

                        for customer in customers:
                            total_balance += customer["balance"]

                        print("bank total balance :", total_balance)


                    elif manager_choice == 5:

                        transaction_found = False

                        for customer in customers:

                            if len(customer["transactions"]) > 0:

                                transaction_found = True

                                print("----------------")
                                print(
                                    "Customer:",
                                    customer["user name"]
                                )

                                for transaction in customer["transactions"]:
                                    print("-", transaction)

                        if transaction_found == False:
                            print("no transactions found")


                    elif manager_choice == 6:

                        print("manager logged out")
                        break

                    else:
                        print("invalid choice")


    elif choice == 4:

        print("thank you for using Vansh Bank")
        break


    else:

        print("invalid choice")
