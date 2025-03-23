def readFile(path = "data.txt"): # Creating readFile funcation 
    """
    Function read the data from data.txt and converts it into a list of lists.

    """
    # Open the file located at the given path in read mode
    file = open(path, "r")
    # Read the contents of the file into a string variable
    contents = file.read() 
    #Closeing the file
    file.close()
    # Split the contents into a list of strings, each string representing a line of data
    data = contents.strip().split("\n")
    # Create an empty list 
    lstData = []
    # Iterate through each line of data
    for row in data:
        # Remove whitespace and split the line into a list 
        clean_row = row.strip().split(",")
        # Append date in lstData 
        lstData.append(clean_row)
        # Return the list 
    return lstData

