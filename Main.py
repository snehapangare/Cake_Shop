import AdminLogin
import AdminMenu
import UserLogin
import UserMenu
import logo

if __name__ == "__main__":
    while True:
        logo.logo_icon()
        try:
            UserType = int(input("\t1. Admin\n\t2. User\n\t3. Exit\nEnter Your Choice(1 or 2 or 3): "))
        except ValueError:
            print("Invalid Input...")
        else:
            if UserType == 1:
                if AdminLogin.admin_login():
                    AdminMenu.admin_Menu()
                    # break
                else:
                    print("Admin login failed.")
            elif UserType == 2:
                try:
                    userType_sub = int(input("\n\t\t1. Exisiting User.\n\t\t2. New User.\nEnter Customer Type (1 or 2): "))
                except ValueError:
                    print("Invalid Inputes...")
                except:
                    print("Error 404: Error Not Found...")
                else:
                    if userType_sub == 1:
                        user_id = UserLogin.user_login()  
                        if user_id:
                            UserMenu.user_Menu(user_id)
                            # break
                        else:
                            print("User login failed.")
                    elif userType_sub == 2:
                        UserLogin.addUser()
                        logo.logo_icon()
                        print("Enter Your New Login ID and Passward.")
                        user_id = UserLogin.user_login()  
                        if user_id:
                            UserMenu.user_Menu(user_id)
                            # break
            elif UserType == 3:
                print("\t\tThank You....!\n")
                break
            else:
                print("Invalid Input...")
