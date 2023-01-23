#MY NOTES:
#1: save user.txt and tasks.txt to files
#2: open each of these files

#=====importing libraries===========
'''This is the section where you will import libraries'''


#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

username = input("Please enter your username:\n")
password = input("Please enter your password:\n")

with open("user.txt", "r") as userfile:

    for line in userfile:

        logindetails = line.split(", ") #this creates split list of object details that can be called

        if username != logindetails[0]: #won't allow non registered user to log in
            print("Username not recognised, please try again: \n")

        elif username != logindetails[0]: #prints 'username recognised' if username on users file
            print("Username recognised")
            break

while True:
    #presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    #creates separate menu for admin with more choices
    if username == "admin":
        menu = input("Select one of the following Options below:\n"
                 "r - Registering a user\n"
                 "a - Adding a task\n"
                 "va - View all tasks\n"
                 "vm - view my task\n"
                 "st- view statistics\n"
                 "e - Exit\n"
                 ).lower()
    else:
        #create menu for non-admin with fewer options
        menu = input("Select one of the following Options below:\n"
    "r - Registering a user\n"
    "a - Adding a task\n"
    "va - View all tasks\n"
    "vm - view my task\n"
    "e - Exit\n"
    ).lower()

#registering a user
    if menu == 'r':
        if username == 'admin':
            new_username = input("Please enter a new username:")
            new_password = input("Please enter a new password:")
            new_password_confirmation = input("Please confirm your new password")
            if new_password == new_password_confirmation:
                user = open('user.txt','r+')
                user.write(f"{new_username}, {new_password}")
                print("Thank you, new password and username added to user.txt file")
            else: print("Passwords do not match, start again")
        else: print("Sorry, only admin can register a user")
#adding a task
    elif menu == 'a':
        task_username = input("Please enter the username of the person assigned to this task:")
        task_title = input("Please enter the title of this task")
        task_description = input("Please enter a description of this task")
        task_due_date = input("Please enter a due date for this task")
        current_date = input("Please enter the current date:")
        task_complete = "No"
        with open('tasks.txt', 'a') as task_list:
            task_list.write(f"\n{task_username}, {task_title}, {task_description}, {task_due_date}, {current_date}, {task_complete}")
            task_list.close()
#viewing all tasks
    elif menu == 'va':
        #create empty task list to populate later
        tasks_all= ""
        with open("tasks.txt", "r") as task_list:
            for line in task_list:
                tasks_all = tasks_all + line
            tasks_all= tasks_all.split("\n")

            #performs this operation for all tasks in list by looping through them
        for i in range(0, len(tasks_all)):
            task= tasks_all[i]
            task= task.split(", ")
            #prints all components of the task
            print("__________")
            print(f"\n task:          {task[1]}")
            print(f" task username:          {task[0]}")
            print(f" task date assigned:          {task[3]}")
            print(f" task date due:          {task[4]}")
            print(f" task completion status:          {task[5]}")
            print(f" {task [2]}")

#viewing 'my tasks'
    elif menu == 'vm':
        # create empty task list to populate later
        tasks_all = ""
        with open("tasks.txt", "r") as task_list:
            for line in task_list:
                tasks_all = tasks_all + line
            tasks_all = tasks_all.split("\n")
            #adds split up tasks onto new line in file
        counter =0
        #put in to check there are tasks to view
        for i in range(0, len(tasks_all)):
            task= tasks_all[i]
            task= task.split(", ")
            #split tasks so can print out components as below
            if username == task[0]:
                counter += 1
                print("Here are your assigned tasks:\n")
                print("__________")
                print(f"\n task:          {task[1]}")
                print(f" task username:          {task[0]}")
                print(f" task date assigned:          {task[3]}")
                print(f" task date due:          {task[4]}")
                print(f" task completion status:          {task[5]}")
                print(f" {task[2]}")
        #if no tasks to view
        if counter==0:
            print("No tasks assigned to your user")
#for choice 'statistics' (admin only allowed)
    elif menu == 'st' and username == 'admin':
        with open("user.txt", "r") as userlist:
            with open("tasks.txt", "r") as tasklist:
                #get user and task lists
                userlist=userlist.readlines()
                tasklist=tasklist.readlines()
                #print length of user and task list
                print(f"the total number of users is {len(userlist)}")
                print(f"the total number of tasks is {len(tasklist)}")
#for choice 'exit'
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
#for incorrect choice- i.e. not an option presented in the menu
    else:
        print("You have made a wrong choice, Please Try again")


