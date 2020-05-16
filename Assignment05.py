# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog:
# RRoot,1.1.2030,Created started script
# Laura Truong,5/13/2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
loadFile = open(objFile, "r")
for row in loadFile:
    lstRow= row.split(",") # Returns a list!
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
    #print(dicRow)
loadFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("** Showing current data: **")
        for row in lstTable:
            print(row["Task"] + "," + row["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("** Adding a new item: **")
        strTask = input("Enter a task: ")
        strPriority = input("Enter the priority level: ")
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove an item from the list/Table
    elif (strChoice.strip() == '3'):
        print("** Here are your current tasks: **") #Print current tasks for end user.
        for row in lstTable:
            print(row["Task"])
        print('') #Add a space in between

        strRemove = str(input("Enter a task to remove: "))  # Item to remove

        for row in lstTable:
            if row["Task"].lower() == strRemove.lower():
                lstTable.remove(row)
                print(strRemove  + " has been removed. ")
        if row["Task"].lower() != strRemove.lower():
                print("Task not in the list")
        else:
            continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Saving data to file: ")
        loadFile =open(objFile, "w")
        for row in lstTable:
            loadFile.write(str(row["Task"] + "," + row["Priority"] + "\n"))
        loadFile.close()
        print("Data Saved!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Exiting program.")
        input("Hit enter to end program.") #Prompt user to hit 'Enter' to end the program.
        break  # and Exit the program
    else:
        print("** Please only choose a number 1-5! **") #Else statement in case user enters something that is not in the menu.