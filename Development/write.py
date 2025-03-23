#importing DataTime 
import datetime 
def rent_bill(customer_name, customer_number, customer_address, rent_data):
    # Get the current date and time
    dateTimeNow = datetime.datetime.now()
     # Initialize the middle section of the bill
    billMiddle = ""
     # Initialize serial number and total
    sn=1
    total=0.0
    # for loop to get data form rent_data and store in a varible rent_land 
    for rent_land in rent_data:
        # Calculate the price for each rented land
        price=int(rent_land[3])*rent_land[4]
         # Add a formatted row to the middle section of the bill
        billMiddle+=f"\n|{sn:<8}|{rent_land[0]:<14}|{rent_land[1]:<16}|{rent_land[4]:<15}|{rent_land[2]:<10}|{price:<16}| {rent_land[5]:<12}|" 
         # Update the total price and Convert the calculated price to a float
        total = total + float(price)
        # Increment the serial number
        sn+=1
    # Calculate grand total including VAT
    gTotal=total+(0.13*total)
    # Construct the top section of the bill
    billTop = f"""
                                        Techno Property Nepal
                                Hospital chowk - 10, Pokhara, Nepal
    VAT : 91823789                                                              phone : 9846845542

    Name : {customer_name:<20}                                                 Date : {dateTimeNow.date()}
    Address : {customer_address}
    Phone : {customer_number}
----------------------------------------------------------------------------------------------------
|   SN   | kitta number |      city      |    Duration   |   anna   |     Price      |  Direction  |
----------------------------------------------------------------------------------------------------"""
     # Construct the bottom section of the bill
    billBottom = f"""
----------------------------------------------------------------------------------------------------
                                                                            Total : {total}
                                                                            Grand Total : {gTotal}
    """
    # Combine top, middle, and bottom sections to form the complete bill
    bill = billTop + billMiddle + billBottom
    # Print the bill
    print(bill)
    # Write the bill to a text file with the current timestamp as its name
    file=open(f"bill/rent_{dateTimeNow.strftime('%Y-%m-%d_%H-%M-%S')}.txt","w")
    file.write(bill)
   # Close the file after writing
    file.close()


def return_bill(name,number,address,return_data):
    # Get the current date and time.
    date_time_now = datetime.datetime.now()
     # Initialize the middle section of the bill
    billMiddle = ""
    # Initialize serial number and gtotal
    sn=1
    gtotal=0
    # for loop to get data form return_data and store in a varible return_land 
    for return_land in return_data:
        #Making fine 0 at first 
        fine=0
        # making price 0 at first 
        price=0
        rent_month = return_land[4]
        return_month = return_land[5]
        month_delay = return_month-rent_month
        # If rent month is equal to return month it will not charge and amount
        if month_delay>0:
            fine=month_delay*1000
            price=month_delay*int(return_land[2]) #file read garda string ma huxa
        total=price+fine
        gtotal+=total
        # Format details of the returned land and add to billMiddle.
        billMiddle+=f"\n|{sn:<8}|{return_land[0]:<14}|{return_land[1]:<16}|{return_land[3]:<8}|{rent_month:<14}|{return_month:<14}|{fine:<15}|{price:<17}|{total:<13}|"
        # Increment serial number.
        sn+=1
    # Calculate grand total with VAT.
    gTotal_v=gtotal+(0.13*gtotal)
    # Construct the top section of the bill
    billTop = f"""
                                                Techno Property Nepal
                                        Hospital chowk - 10, Pokhara, Nepal
    VAT : 91823789                                                                            Phone : 9846845542

    Name : {name:<20}                                                                         Date : {date_time_now.date()}
    Address : {address}
    Phone : {number}
---------------------------------------------------------------------------------------------------------------------------------
|   SN   | kitta number |      city      |  Anna  |     rent     |    return    |     fine      |       price     |     total   |      
---------------------------------------------------------------------------------------------------------------------------------"""

    billBottom = f"""
---------------------------------------------------------------------------------------------------------------------------------
                                                                                                    Total : {gtotal}
                                                                                                    Grand Total : {gTotal_v}
    """
    # Combine top, middle, and bottom sections to form the complete bill
    bill = billTop + billMiddle + billBottom
    print(bill)

    file=open(f"bill/return_{date_time_now.strftime('%Y-%m-%d_%H-%M-%S')}.txt","w")
    # Print the bill
    file.write(bill)
    # Close the file after writing
    file.close()    