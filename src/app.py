import os
import datetime

# Empty diccionary
db = {"id":[],"task":[],"created_at":[]}

index = 0


def addTask():
    global index
    task = input("Please introduce the task that you'll do: ")
    time = datetime.date.today()
    
    try:
        db["id"].append(index)
        db["task"].append(task)
        db["created_at"].append(time)
        os.system('clear')
        print("Task created")
        index +=1
    except: 
        print("Something went wrong in the addition of this task")
    # print(db)

def editTask(idTask):
    global index
    editedTask = input("Introduce the task you want to replace with: ")
    os.system('clear')
    try: 
        db['task'][idTask] = editedTask
        print(db['task'][idTask])
    except:
        print("Something fail while editing the task, FIX IT!!")

def showOneTask(searchId):
    int(searchId)
    oneTaskId = db["id"][searchId]
    oneTaskTask = db["task"][searchId]
    oneTaskDate= db["created_at"][searchId]
    wholeTaskArray = [oneTaskId, oneTaskTask, oneTaskDate]
    os.system('clear')
    print(wholeTaskArray)

def deleteOneTask(idToDelete):
    try:
        del db["id"][idToDelete],db["created_at"][idToDelete],db["task"][idToDelete]
        os.system('clear')
        print("Task succesfully deleted")
    except:
        print("Something fail while deleting this task")

def deleteAllTasks():
    db = {"id":[],"task":[],"created_at":[]}
    print("Entire tasks have been succesfully deleted =)")

while True:

    print("(1). Add Task")
    print("(2). Edit task")
    print("(3). See all tasks")
    print("(4). See 1 specific task")
    print("(5). Delete 1 specific task")
    print("(6). Delete all tasks")
    print("(7). Exit application")
    option = input("Select the option you wish to do: ")
    match option:
                case "1":
                    print("Going to addition mode....")
                    addTask()
                case "2":
                    print("Going to edit mode")
                    idTask = int(input("What task do you want to edit? "))
                    editTask(idTask)
                case "3":
                    print("Show all tasks")
                    print(db)
                case "4":
                    searchIdTask= int(input("Introduce the id of the task please: "))
                    showOneTask(searchIdTask)
                case "5":
                    idToDelete = int(input("Ask for the task id to delete"))
                case "6":
                    confirmation = input("Type 'Yes' if your sure to delete all the tasks. Anything else will cancel the request: ")
                    if(confirmation == "Yes" or confirmation == "yes"):
                            deleteAllTasks()
                    else:
                        print("Task deletion canceled")
                case "7":
                    print("Goodbye, see you soon")
                    exit()
                case _:
                    print("Invalid option. Please choose an option from 1 to 6")
