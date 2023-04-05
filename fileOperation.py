def saveUserInFile(userData) :
    try:
        fileObj = open('users.txt','a')
    except Exception as e :
        print("sorry can not find the file !!")
    else :
        fileObj.write(userData)

def getAllUsers():
    try:
        fileObj = open('users.txt','r')
    except Exception as e :
        print("sorry can not find the file !!")
    else :
        return fileObj.readlines()

def userLoginSearch(email,password):
    users = getAllUsers()
    for user in users :
        if email == user.strip("\n").split(":")[3] and password == user.strip("\n").split(":")[4] :
            return user.strip("\n").split(":")[0],user.strip("\n").split(":")[1]
    print("user email or password incorrect")
    return False

def saveProjectInFile(projectData) :
    try:
        fileObj = open('projects.txt','a')
    except Exception as e :
        print("sorry can not find the file !!")
    else :
        fileObj.write(projectData)

def clearProjectInFile() :
    try:
        fileObj = open('projects.txt','w')
    except Exception as e :
        print("sorry can not find the file !!")
    else :
        fileObj.write('')

def getAllProjectForAllUsers():
    try:
        fileObj = open('projects.txt','r')
    except Exception as e :
        print("sorry can not find the file !!")
    else :
        return fileObj.readlines()

def getAllUserProjects(userID):
    AllUsersProjects = getAllProjectForAllUsers()
    userProjects = []
    for project in AllUsersProjects :
        if userID == project.strip("\n").split(":")[6] :
            print(project)
            userProjects.append(project)
    return userProjects

def searchProjectByID(userID, projectID) :
    AllUsersProjects = getAllProjectForAllUsers()
    for project in AllUsersProjects :
        if projectID == project.strip("\n").split(":")[0] and userID == project.strip("\n").split(":")[6] :
            return project
    print("There is no project match this id !! ")

def deleteUserProject(userID,projectID):
    targetProject = searchProjectByID(userID, projectID)
    AllUsersProjects = getAllProjectForAllUsers()
    clearProjectInFile()
    for project in AllUsersProjects :
        if not project == targetProject :
            saveProjectInFile(project)
    

def editUserProject(userID,projectID):
    AllUsersProjects = getAllProjectForAllUsers()
    targetProject = searchProjectByID(userID, projectID)
    newProject = ''
    while True :
        print("choose one of the field to update : ")
        print("t ---> titel")
        print("d ---> Details")
        print("tt ---> Total target")
        print("st ---> start time")
        print("et ---> end time")
        print("end ---> to save the updated values ")
        choice = input("your choice : ")
        id = targetProject.strip("\n").split(":")[0]
        title = targetProject.strip("\n").split(":")[1]
        details = targetProject.strip("\n").split(":")[2]
        totalTarget = targetProject.strip("\n").split(":")[3]
        startTime = targetProject.strip("\n").split(":")[4]
        endTime = targetProject.strip("\n").split(":")[5]
        userId = targetProject.strip("\n").split(":")[6]
        
        if choice == 't':
            Title = input("enter the project title : ")
            title = Title
            continue
        elif choice == 'd':
            Details = input("enter the project Details : ")
            details = Details
            continue
        elif choice == 'tt':
            TotalTarget = askforInt("enter the project total target : ")
            totalTarget = TotalTarget
            continue
        elif choice == 'st':
            StartTime = dateValidated("enter the starting time of your project : ")
            startTime = StartTime
            continue
        elif choice == 'et':
            EndTime = dateValidated("enter the end time of your project : ")
            endTime = EndTime
            continue
        elif choice == 'end' :
            newProject = f"{id}:{Title}:{Details}:{totalTarget}:{startTime}:{endTime}:{userId}\n"
            deleteUserProject(userID,projectID)
            saveProjectInFile(newProject)
            return
