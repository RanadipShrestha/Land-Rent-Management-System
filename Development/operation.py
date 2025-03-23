#importing read
import read 
#importing write 
from write import * 
#Creating display_land funaction
def display_land():
    every_land = read.readFile() #Creating variable every_land and calling read.py funcation readFile
    print("+----------+-------------+-----------+------+---------+-----------------+")
    print("| Kitta    | City        | Direction | Anna | Price   | Availability    |")
    print("+----------+-------------+-----------+------+---------+-----------------+")
    
    for each_detail in every_land:
        kitta_number = int(each_detail[0])
        city = each_detail[1]
        direction = each_detail[2]
        anna = each_detail[3]
        price = each_detail[4]
        availability = each_detail[5]

        # Formatting the row to align land
        print(f"| {kitta_number:<8} | {city:<11} | {direction:<9} | {anna:<4} | {price:<7} | {availability:<15} |")
    
    print("+----------+-------------+-----------+------+---------+-----------------+")


def rent_land():
    # Read all land details from the file
    every_land_detail = read.readFile()
    # Asking user to input name  
    customer_name = input("please enter your name :")
    while True:
        try:
        # Asking user to input number 
            customer_number = int(input("Please enter your mobile number :"))
            break
        except: 
            print("Please Enter valid number!")
    customer_address = input("Please enter Your address :")
    # Initialize an empty list to store rented land data
    rent_data = []
    while True:
        # Loop until a valid kitta number is entered
        while True:
            
            kitta_Number =  input("Please enter kitta number you want to rent :")

            if int(kitta_Number) > 0:
                break
            else:
                print("Please enter correct kitta number according to List")
                
        land_found = False
        
        for i in range(len(every_land_detail)): 
            if kitta_Number == every_land_detail[i][0]:
                land_found = True
                # Check if the land is available for rent
                if every_land_detail[i][5] == "Available":
                    #Asking user to input number of month customer want to rent land
                    while True:
                        try:
                            month_time = int(input("please enter how many month you want to rent :"))
                            break
                        except:
                            print("Please enter month in without Decimal number")
                        
                    rent_data.append([kitta_Number, every_land_detail[i][1],every_land_detail[i][3],every_land_detail[i][4],month_time, every_land_detail[i][2]])
                    # Marking the land as not available
                    every_land_detail[i][5] = "Not Available" 
                    # Open file to update land availability 
                    file = open("data.txt", "w")
                    # Writing the updated land data back to the file
                    for row in every_land_detail:
                        # For each land record, convert it into a text format and add a new line
                        file.write(",".join(row) + "\n")
                    # Close the file after writing
                    file.close() 
                else:
                    print("Land is not available.")
                    break
        # If the land land not found
        if not land_found:
            print("Kitta number you enter is not found.")  
        # Ask the user if they want to rent land again, if not, exit the loop
        ask_again = input("Do you want to rent land again? yes (y) and no for any other key): ")
        if ask_again.lower() != "y":
            break
    # Call the function rent_bill
    rent_bill(customer_name,customer_number,customer_address,rent_data)


def return_land():
    # Read all land details from the file
    every_land_lst = read.readFile()
    # Creating an empty list to store rented land data
    return_data = []
    # starting an infinite loop
    while True:
        while True:
            #Asking user to input kitta number and store in a variable kitta_number 
            kitta_Number =  input("Please enter kitta number you want to return :")
            # checking if entered kitta number is greater than 0
            if int(kitta_Number) > 0:
                # breaking the loop if condition is met
                break
            else:
                print("Please enter correct kitta number according to List")
        land_found = False
        for i in range(len(every_land_lst)):
                if kitta_Number == every_land_lst[i][0]:
                    land_found = True
                    # checking if the land is not available for return
                    if every_land_lst[i][5] == "Not Available":
                        # starting another infinite loop
                        while True:
                            # trying to convert input to integer
                            try:
                                rent_month = int(input("Please enter you rent land Month :"))
                                return_month = int(input("please enter you return land month :"))
                                #breaking the loop if conversion is successful
                                break
                            except:
                                print("Please enter month in without Decimal number")
                        return_data.append([kitta_Number, every_land_lst[i][1], every_land_lst[i][4], every_land_lst[i][3],rent_month,return_month])
                        # Marking the land as available
                        every_land_lst[i][5] = "Available"  
                        file = open("data.txt", "w")
                        # Writing the updated land data back to the file
                        for row in every_land_lst:
                            # For each land record, convert it into a text format and add a new line   
                            file.write(",".join(row) + "\n")
                            # closing the file
                        file.close()
                    else:
                        print("Land cannot be return.")
                    break
        if not land_found:
            print("Kitta number you enter is not found.")  
        # Ask the user if they want to rent land again, if not, exit the loop    
        askAgain = input("Do you want to rent land again? yes (y) and no for any other key: ")
        if askAgain.lower() != "y":
            break
    name = input("please enter your name :")
    while True:
        try:
           number = int(input("Please enter number :"))
           break
        except: 
            print("Please Enter valid number")
    address = input("Please enter Your address :")
     # Call the function return_bill
    return_bill(name,number,address,return_data)