"""
COMPULSORY TASK PART 2 -
Now format your program so that:
a. Only the user with the username 'admin' is allowed to register users.
b. The admin user is provided new menu option that allows them to display statistics. When this menu is selected, the
total number of tasks and the total number of users should be displayed.
"""

# Import 'date' from 'datetime'.
from datetime import date

# Open "user.txt" with .open() and use 'r+' to read and write.
# Use .readlines() to return each line as list item and store in the variable 'lines'.
# Create two empty lists called 'username_list' to store usernames and 'password_list' to store passwords.
file = open("user.txt", "r+", encoding="utf-8")
lines = file.readlines()
username_list = []
password_list = []

# For loop begin, for 'line' in 'lines'.
# Use .strip() function to strip \n and any empty spaces from beginning and end and store it in variable 'temp'.
# Use .split() function to split the 'temp' into list.
# Append username to 'username_list' and  password to 'password_list' each loop.
for line in lines:
    temp = line.strip()
    temp = temp.split(", ")
    username_list.append(temp[0])
    password_list.append(temp[1])

# Print the message directing user to enter their username and password.
print("Please enter your username and password to login")

# While loop begin and continue as long as the condition is true.
# Request input of username and store in 'user_login' variable.
# Request input of password and store in 'password_login' variable.
while True:
    user_login = input("Enter Username: ")
    password_login = input("Enter Password: ")

    # Use 'if' statement to validate username and password.
    # If the input matches the username and password in their respective list,
    # Print 'You have successfully logged in!' and break.
    if user_login in username_list and password_login in password_list:
        print("You have successfully logged in!")
        break

    # Else, print 'Error! Incorrect username or password. Please try again!'
    else:
        print("ERROR! Incorrect username or password. Please try again!")

# Use .close() to close the file.
file.close()

# While loop begin and continue as long as the condition is true.
# Present menu to the user and ensure that the input is converted to lowercase.
while True:
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - statistics (admin only)
e - Exit
: ''').lower()

    # If 'menu' input is equal to "r",
    # Open 'user.txt' with .open() and use 'a' to append, and store it in variable 'reg_file'.
    # If 'user_login' is equal to 'admin',
    # Request input of new username and new password and store them in 'new_username' and 'new_password' respectively.
    # Request input of the password one more time to check 'new_password' and 'confirm_pw' are the same.
    if menu == "r":
        reg_file = open("user.txt", "a", encoding="utf-8")
        if user_login == "admin":
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            confirm_pw = input("Confirm your password: ")

            # If 'new_password' is equal to 'confirm_pw',write them to 'user.txt'.
            # Print successful new user registration message.
            if new_password == confirm_pw:
                reg_file.write(f"\n{new_username}, {new_password}")
                print("New user successfully registered! Thank You.")

            # Else, print 'Error! Passwords do not match!'.
            else:
                print("Error! Passwords do NOT match!")

        # Else, print 'You do not have the required authorization!'.
        else:
            print("You do not have the required authorization!")

        # Close 'reg_file' using .close()
        reg_file.close()

    # Else if menu input is equal to "a",
    # Open 'tasks.txt' with .open() and use 'a' to append, and store it in variable 'new_task'.
    elif menu == "a":
        new_task = open("tasks.txt", "a", encoding="utf-8")

        # Request user to input details of the new tasks and write to 'tasks.txt' using .write()
        assigned_user = input("Enter username of the person whom the task is assigned to: ")
        title = input("Enter title of the task: ")
        description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of the task (DD/MM/YYYY): ")
        current_date = date.today().strftime('%d/%m/%Y')
        complete = "NO"
        new_task.write(f"\n{assigned_user}, {title}, {description}, {current_date}, {due_date}, {complete}")
        new_task.close()

    # Else if menu input is equal to "va",
    # Open "tasks.txt" with .open() and use 'r+' to read and write.
    # Use .readlines() to return each line as list item and store in the variable 'lines_va'.
    elif menu == "va":
        all_tasks = open("tasks.txt", "r+", encoding="utf-8")
        lines_va = all_tasks.readlines()

        # For loop begin, for 'line_va' in 'lines_va'.
        # Use .strip() function to strip \n and any empty spaces from beginning and end and store it in 'temp_va'.
        # Use .split() function to split the 'temp_va' into list.
        # Print the all the tasks to the console in the format of Output 2 presented in the L1T19 pdf file page 6.
        for line_va in lines_va:
            temp_va = line_va.strip()
            temp_va = temp_va.split(", ")
            print(f"""
——————————————————————————————————————————————
Task:                   {temp_va[1]}
Assigned to:            {temp_va[0]}
Date assigned:          {temp_va[3]}
Due date:               {temp_va[4]}
Task Complete?          {temp_va[-1]}
Task Description:     \n {temp_va[2]}
———————————————————————————————————————————————""")

        # Close the file using .close()
        all_tasks.close()

    # Else if menu input is equal to "vm",
    # Open "tasks.txt" with .open() and use 'r+' to read and write.
    # Use .readlines() to return each line as list item and store in the variable 'lines_vm'.
    elif menu == "vm":
        user_task = open("tasks.txt", "r+", encoding="utf-8")
        lines_vm = user_task.readlines()

        # For loop begin, for 'line_vm' in 'lines_vm'.
        # Use .strip() function to strip \n and any empty spaces from beginning and end and store it in 'temp_vm'.
        # Use .split() function to split the 'temp_vm' into list.
        for line_vm in lines_vm:
            temp_vm = line_vm.strip()
            temp_vm = temp_vm.split(", ")

            # If the username of the person logged in is same as the username read from the file,
            # i.e. 'user_login' == 'temp_vn[0]',
            # Print the task in the format of output 2 om L1T19 pdf.
            if user_login == temp_vm[0]:
                print(f"""
——————————————————————————————————————————————
Task:                   {temp_vm[1]}
Assigned to:            {temp_vm[0]}
Date assigned:          {temp_vm[3]}
Due date:               {temp_vm[4]}
Task Complete?          {temp_vm[-1]}
Task Description:     \n {temp_vm[2]}
———————————————————————————————————————————————""")

        # Close the file using .close()
        user_task.close()

    # Else if 'menu' input is equal to "s",
    # If 'user_login' == 'admin',
    elif menu == "s":
        if user_login == "admin":

            # Open "tasks.txt" with .open() and use 'r+' to read and write.
            # Read lines in 'tasks.txt' using .readlines() and calculate the length of tasks, each line consist of
            # one task and store it in 'tasks_num'
            tasks_stats = open("tasks.txt", "r+", encoding="utf-8")
            tasks_num = len(tasks_stats.readlines())

            # Close the file using .close()
            tasks_stats.close()

            # Open "user.txt" with .open() and use 'r+' to read and write.
            # Calculate the length of 'username_list' and store it in 'total_users'.
            user_stats = open("user.txt", "r+", encoding="utf-8")
            total_users = len(username_list)

            # Close the file using .close()
            user_stats.close()

            # Print the total number of tasks 'tasks_num' and the total number of users 'total_users'.
            print(f"""
            Statistics
——————————————————————————————————————————————
            Total tasks:
            {tasks_num}

            Total number of users:
            {total_users}
——————————————————————————————————————————————
""")

        else:
            print("You do not have the required authorization!")

    # Else if 'menu' input is equal to "e", print 'Goodbye!!!' and exit using exit().
    elif menu == "e":
        print("Goodbye!!!")
        exit()

    # Else, print 'You have made a wrong choice, Please Try again.'
    else:
        print("You have made a wrong choice, Please Try again")