to_do_list = []
loop = True


def option_sorter(x):
    task_input = ""
    global to_do_list
    #Add/Removes task from the todo list
    if x == 1:
        while task_input != "end":
            print("\nYou have chosen to Add/Remove for your to do list.. ")
            while True:
                try:
                    task_input = int(input("\nWould you like to add or remove an item from the 'To do list'?\n1: Add task\n2: Remove task\n3: Leave\nPlease enter a number from 1-3: "))
                    if task_input == 1:
                        while True:
                            
                            task_input = input("\nPlease enter an item into the list: ")
                            to_do_list.append(task_input)
                            while True:
                                x = input("\nWould you like to add another to your 'to do list'? : (Y/N) ").lower()
                                if x == "y" or x == "n":
                                    break
                                else:
                                    print("Please enter Y or N not '{}'".format(x))
                            if x == "n":
                                break
                    elif task_input == 2:
                        if len(to_do_list) == False:
                            print("\nThere is no task present to remove in your to do list")
                        else:
                            while True:
                                try:
                                    print("\n###LIST###")
                                    for i in range(0, len(to_do_list)):
                                        print("{}: {}".format(i+1, to_do_list[i]))
                                    print("##########")
                                    task_input = int(input("Please enter in the number from 1-{} of the item you would like to remove: ".format(len(to_do_list))))
                                    if task_input <= len(to_do_list):
                                        print("Removed Task, {}: {}".format(task_input, to_do_list[task_input - 1]))
                                        to_do_list.pop(task_input - 1)

                                    elif task_input <= 0 or task_input > len(to_do_list):
                                        print("Please enter a number from 1-{} only, no letters or Negative numbers".format(len(to_do_list)))
                                    if len(to_do_list) == False:
                                        print("\nYou have removed all task from your to do list!")
                                        break
                                    else:
                                        while True:
                                            x = input("Would you like to remove another task? (Y/N) :").lower()
                                            if x == "y" or x == "n":
                                                break
                                            else:
                                                print("Please enter Y or N, not '{}'".format(x))
                                    if x == "n":
                                        break
                                except ValueError:
                                    print("Please enter a number from 1-{} only, no letters".format(len(to_do_list)))
                    elif task_input == 3:
                        print("\nLeaving list manager..")
                        x = True
                        return x
                        break
                    else:
                        print("Please enter 1: Add task or 2: Remove task or 3: to leave editing\n")
                except ValueError:
                    print("Please enter 1: Add task or 2: Remove task  or 3: to leave editing\n")
            

    #View to do list
    elif x == 2:
        print("\nYou have choosen view list.. ")
        print("###LIST###")
        for i in range(0, len(to_do_list)):
            print("{}: {}".format(i+1, to_do_list[i]))
        print("##########")
        x = True
        return x

    #Exits the to do list program
    elif x == 3:
        print("\nYou have exited the program")
        loop = False
        return loop
        




name = input("What is your name? : ")
print("Greetings {}, please enter a corrisponding number for the action: \n".format(name))

while loop == True:
    try:
        print("\n1: Edit 'to do list' \n2: View list \n3: Exit")
        option = int(input("Please enter a number to excute an action: "))
        if option <= 3:
            loop = option_sorter(option)
        else:
            print("Please enter a number from 1-3 only\n")
    except ValueError:
        print("Please enter a number from 1-3 only, no letters\n")

