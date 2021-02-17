to_do_list = []
loop = True


def option_sorter(x):
    task_input = ""
    if x == 1:
        while True:
            print("You have choosen adding task.. ")
            task_input = input("Please enter an item into the list: ")
            to_do_list.append(task_input)
            if task_input == "End":
                x = True
                break
    elif x == 2:
        print("You have choosen view list.. ")
        print("###LIST###")
        for i in range(0, len(to_do_list)):
            print("{}: {}".format(i+1, to_do_list[i]))
        print("##########")
        x = True
        return x
    elif x == 3:
        print("You have exited the program")
        loop = False
    return x
        
        
name = input("What is your name? : ")
print("Greetings {}, here i your list".format(name)) 
while loop == True:

    print("1: Add a task \n2: View lit \n3: Exit")
    option = int(input("Please enter a number to excute an action: "))
    loop = option_sorter(option)

