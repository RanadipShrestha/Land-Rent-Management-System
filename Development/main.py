#Importing operation.py as op
import operation as op
# Creating funaction main
def main(): 
#Company Banner 
    banner =  """

████████╗███████╗░█████╗░██╗░░██╗███╗░░██╗░█████╗░    ██████╗░██████╗░░█████╗░██████╗░███████╗██████╗░████████╗██╗░░░██╗
╚══██╔══╝██╔════╝██╔══██╗██║░░██║████╗░██║██╔══██╗    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝╚██╗░██╔╝
░░░██║░░░█████╗░░██║░░╚═╝███████║██╔██╗██║██║░░██║    ██████╔╝██████╔╝██║░░██║██████╔╝█████╗░░██████╔╝░░░██║░░░░╚████╔╝░
░░░██║░░░██╔══╝░░██║░░██╗██╔══██║██║╚████║██║░░██║    ██╔═══╝░██╔══██╗██║░░██║██╔═══╝░██╔══╝░░██╔══██╗░░░██║░░░░░╚██╔╝░░
░░░██║░░░███████╗╚█████╔╝██║░░██║██║░╚███║╚█████╔╝    ██║░░░░░██║░░██║╚█████╔╝██║░░░░░███████╗██║░░██║░░░██║░░░░░░██║░░░
░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░

███╗░░██╗███████╗██████╗░░█████╗░██╗░░░░░
████╗░██║██╔════╝██╔══██╗██╔══██╗██║░░░░░
██╔██╗██║█████╗░░██████╔╝███████║██║░░░░░
██║╚████║██╔══╝░░██╔═══╝░██╔══██║██║░░░░░
██║░╚███║███████╗██║░░░░░██║░░██║███████╗
╚═╝░░╚══╝╚══════╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝

"""
    print(banner)
    # Using While loop 
    while True:
        print("""
            1. Display Land
            2. Rent Land
            3. Return Land
            4. Exit
            """)
        
        try:
            #Take user input and converting it into an integer. 
            choice = int(input("Enter a number here: "))
            #Creating if else statement
            if choice == 1: 
                #Calling the display_land fucation form the operation module
                op.display_land()
            elif choice == 2:
                #Calling the rent_land fucation form the operation module
                op.rent_land()
            elif choice == 3:
                #Calling the return_land fucation form the operation module
                op.return_land() 
            elif choice == 4:
                print("Thank you for visiting")
                #if choice 4 breaking the loop
                break
            else:
                print("Please enter a valid choice from 1-4")
        #Exception handling for non-integer inputs
        except:
            print("Please input number between 1 to 4")
#Calling the function
main()           