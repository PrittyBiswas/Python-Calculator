task =[]

def addTask():
    task = input("please enter a task u want ")
    task.append(task)
    print(f" Task '{task}' added to the list")

def listTasks():
    if not task:
        print("there are no tasks currently")
    else:
        print("current Tasks:")
        for index,task in enumerate(task):
            print(f" Task {index}.{task}")    

def deleteTask():
    listTasks()
    try:
        taskToDelete=int (input(" choose the task you want to delete:"))
        if taskToDelete >=0 and taskToDelete < len(task):
            task.pop(taskToDelete)
            print(f" Task {taskToDelete} has been deleted ")
        else:
            print(f" Task {taskToDelete} was not fount ")
    except:
        print(f"Task {taskToDelete} invalid input")

if NameError=="_main_":
    print(" welcom to the to  do list by python ")
    while True:
        print("\n")
        print(" please enter the option what u want ")
        print("*")
        print("1.Add a new task")
        print("2.Delete")
        print("3.List the task")
        print("4.quit")

        choice =input(" enter a option u want ")
        if(choice =="1"):
            addTask()
        elif(choice =="2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            break
        else:
            print(" Invalid option ,try again  ")
print(" thank you ")