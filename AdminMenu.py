from tabulate import tabulate
import logo
import cake
import AdminLogin
import UserLogin

class CakeShop:
    def addCake(self):
        try:
            cake_id = int(input("Enter cake id: "))
            flavor = input("Enter cake flavor: ")
            size = input("Enter cake size: ")
            quantity = int(input("Number of Quantity: "))
            price = float(input("Enter cake price: "))
            CAKE_info = cake.Cake(cake_id, flavor, size, quantity, price)

            with open("cakeData.txt", "a") as fp:
                data = f"{CAKE_info.cake_id},{CAKE_info.flavor},{CAKE_info.size},{CAKE_info.quantity},{CAKE_info.price:.2f}"
                fp.write(data)
                fp.write("\n")
        except ValueError:
            print("Invalid Input...")
        except Exception as e:
            print("An error occurred:", e)
        except:
            print("Error 404: Error Not Found.")

    def displayCake(self):
        try:
            with open("cakeData.txt", "r") as fp:
                data = fp.readlines()

            headers = ["Cake ID", "Cake Name", "Size", "Quantity", "Price"]
            table_data = []
            for line in data:
                cake_info = line.strip().split(",")
                if len(cake_info) == 5:  
                    table_data.append(cake_info)
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        except FileNotFoundError:
            print("File does not exist....")
        except Exception as e:
            print("An error occurred:", e)
        except:
            print("Error 404: Error Not Found.")

    def searchByFlavor(self):
        try:
            flavor = input("Enter cake flavor: ")
            with open("cakeData.txt", "r") as fp:
                data = fp.readlines()
            headers = ["Cake ID", "Cake Name", "Size", "Quantity", "Price"]
            table_data = []
            for line in data:
                cake_info = line.strip().split(",")
                if cake_info[1] == flavor:
                    table_data.append(cake_info)
            if table_data:
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
            else:
                print("Cake is not available...")
        except FileNotFoundError:
            print("File doesn't exist......")
        except Exception as e:
            print("An error occurred:", e)
        except:
            print("Error 404: Error Not Found.")

    def removeById(self):
        try:
            self.displayCake()
            cake_id = int(input("Enter cake id: "))
            allCakes = []
            found = False
            with open("cakeData.txt", "r+") as fp:
                for line in fp:
                    data = line.split(",")
                    if data[0] == str(cake_id):
                        found = True
                        print("Cake with ID {} has been deleted.".format(cake_id))
                    else:
                        allCakes.append(line)
            with open("cakeData.txt", "w") as fp:
                fp.write("".join(allCakes))
            if not found:
                print("Cake with ID {} not found.".format(cake_id))
        except FileNotFoundError:
            print("An error occurred while deleting the Cake.")
        except Exception as e:
            print("An error occurred:", e)
        except:
            print("Error 404: Error Not Found.")

    def updateByID(self):
        try:
            self.displayCake()
            cake_id = int(input("Enter cake id: "))
            allcake = []
            found = False
            with open("cakeData.txt", "r+") as fp:
                for line in fp:
                    data = line.split(",")
                    if data[0] == str(cake_id):
                        found = True
                        print("Cake is found...")
                        update_price = float(input("Enter a new price of Cake: "))
                        data[4] = f"{update_price:.2f}"
                    allcake.append(",".join(data))
            if found:
                print("Price of cake updated.")
            else:
                print("Cake with ID {} not found.".format(cake_id))
            with open("cakeData.txt", "w") as fp:
                fp.write("\n".join(allcake))
        except FileNotFoundError:
            print("An error occurred while updating the Cake.")
        except Exception as e:
            print("An error occurred:", e)
        except:
            print("Error 404: Error Not Found.")

    def paymentHistory(self):
        try:
            with open("payment_history.txt", "r") as fp:
                data = fp.readlines()
            headers = ["User ID", "Payment Mode", "Total Price"]
            table_data = []
            for line in data:
                bill_info = line.strip().split(",")  
                if len(bill_info) == 3: 
                    table_data.append(bill_info)
            if table_data:
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
            else:
                print("Payment history is empty.")
        except FileNotFoundError:
            print("File does not exist....")
        except Exception as e:
            print("An error occurred:", e)
        except:
            print("Error 404: Error Not Found.")

def admin_Menu():
    cake_shop = CakeShop()  
    while True:
        logo.logo_icon()
        print("\t\t1.  Add New Cake.")
        print("\t\t2.  Display All Cakes.")
        print("\t\t3.  Search Cake By Flavor.")
        print("\t\t4.  Remove Cake.")  
        print("\t\t5.  Update Cake Price.")
        print("\t\t6.  View Payment History.")
        print("\t\t7.  Add Admin.")
        print("\t\t8.  Display Admin.")
        print("\t\t9.  Remove Admin.")
        print("\t\t10. Add User.")
        print("\t\t11. Display Users.")
        print("\t\t12. Remove User.")
        print("\t\t13. Exit.")
        try:
            choice = int(input("Enter your Choice (1 to 13): "))
        except ValueError:
            print("Invalid Input...")
        except Exception as e:
            print("An error occurred:", e)
        except:
            print("Error 404: Error Not Found.")
        else:
            if choice == 1:
                cake_shop.addCake()  
            elif choice == 2:
                cake_shop.displayCake() 
            elif choice == 3:
                cake_shop.searchByFlavor()
            elif choice == 4:
                cake_shop.removeById()
            elif choice == 5:
                cake_shop.updateByID()
            elif choice==6:
                cake_shop.paymentHistory()
            elif choice == 7:
                AdminLogin.addAdmin()
            elif choice == 8:
                AdminLogin.displayAdmin()
            elif choice == 9:
                AdminLogin.removeAdmin()
            elif choice == 10:
                UserLogin.addUser()
            elif choice==11:
                UserLogin.displayUsers()
            elif choice == 12:
                UserLogin.removeUser()
            elif choice == 13:
                print("\nThank You.\n")
                break