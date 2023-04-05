from projectOperation import createProjectFun, listUserProjects, editUserProjects, deleteUserProjects

def projectMenu(userInfo):
    while True :
        print("######################## Prjects Operation #######################")
        print("choose one of the list : ")
        print("c ---> Create project")
        print("l ---> view all projects")
        print("e ---> edit your projects")
        print("d ---> delete your projects")
        print("s ---> search for your projects")
        print("exit ---> to exit")
        choice = input("your choice : ")
        if choice == 'c':
            createProjectFun(userInfo)
            continue
        elif choice == 'l':
            listUserProjects(userInfo)
            continue
        elif choice == 'e':
            editUserProjects(userInfo)
            continue
        elif choice == 'd':
            deleteUserProjects(userInfo)
            continue
        elif choice == 's':
            pass
        elif choice == 'exit' :
            return
        else :
            print("Invalid input")
            continue
