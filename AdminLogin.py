from tabulate import tabulate

def admin_login():
    try:
        admin_user_id=input("\nEnter a Admin User ID: ") 
        with open("admin_user_log.txt", "r") as fp:
            data = fp.readlines()
        for line in data:
            admin_info = line.strip().split(",")
            if admin_info[0] == admin_user_id:
               admin_user_pass=input("Enter a Admin User Password: ")
               if admin_info[1]==admin_user_pass:
                   print("\nWelcome",admin_user_id,"\n")
                   return True
    except FileNotFoundError:
        print("File does not exist....")
    except Exception as e:
        print("An error occurred:", e)

def addAdmin():
    try:
        with open("admin_user_log.txt", "r") as user_file:
            existing_admin_users = [line.strip().split(",")[0] for line in user_file.readlines()]

        while True:
            new_admin_id = input("\nEnter a unique Admin ID: ")
            if new_admin_id in existing_admin_users:
                print("Admin ID already exists. Please enter a unique User ID.")
                continue
            new_password = input("Enter a password: ")

            new_admin_data = f"{new_admin_id},{new_password}"  
            with open("admin_user_log.txt", "a") as user_file:
                user_file.write(new_admin_data + "\n")
            print("User added successfully.")
            break

    except Exception as e:
        print("An error occurred:", e)
    except:
        print("Error 404: Error Not Found...")

def displayAdmin():
    try:
        CEO=input("Enter CEO ID: ")
        CEO_pass=input("Enter CEO Password: ")
        if CEO=="Sneha" and CEO_pass=="4100":
            with open("admin_user_log.txt","r") as admin_file:
                data = admin_file.readlines()
            admin_ids=[line.strip().split(",")[0] for line in data]
            if admin_ids:
                headers=["Admin ID"]
                table_data=[[admin_id] for admin_id in admin_ids]
                new_func(headers, table_data)
            else:
                print("No Admin found.")
    except FileNotFoundError:
        print("File does not exist.")
    except Exception as e:
        print("An error occurred:", e)

def new_func(headers, table_data):
    print(tabulate(table_data,headers=headers,tablefmt="grid"))

def removeAdmin():
    try:
        admin_user_id=input("Enter a Admin User ID: ")
        allAdmin = []
        found = False
        with open("admin_user_log.txt", "r+") as fp:
            for line in fp:
                data = line.split(",")
                if data[0] == str(admin_user_id):
                    found = True
                    print("Admin ID {} has been deleted.".format(admin_user_id))
                else:
                    allAdmin.append(line)

        with open("admin_user_log.txt", "w") as fp:
            fp.write("".join(allAdmin))
        if not found:
            print("Admin ID {} not found.".format(admin_user_id))
    except FileNotFoundError:
        print("An error occurred while deleting the Cake.")
    except Exception as e:
        print("An error occurred:", e)
    except:
        print("Error 404: Error Not Found.")