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
        print("Task created")
        index +=1
    except: 
        print("Something went wrong in the addition of this task")
    print(db)

def editTask(idTask):
    global index
    editedTask = input("Introduce the task you want to replace with: ")
    db['task'][idTask] = editedTask
    print(db['task'][idTask])

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
                    print("Ask for the task id to show it")
                case "5":
                    print("Ask for the task id to delete")
                case "6":
                    print("Ask for confirmation to erase all the tasks")
                case "7":
                    print("Goodbye, see you soon")
                    exit()
                
    print("Invalid option. Please choose an option from 1 to 6")
