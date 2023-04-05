from helper import askforInt, dateValidated 
from fileOperation import saveProjectInFile, getAllUserProjects, editUserProject, deleteUserProject
import uuid

def createProjectFun(userInfo) :
    print(f"######################## Hello ${userInfo[1]}$ #######################")
    Title = input("enter the project title : ")
    Details = input("enter the project Details : ")
    TotalTarget = askforInt("enter the project total target : ")
    startTime = dateValidated("enter the starting time of your project : ")
    endTime = dateValidated("enter the end time of your project : ")
    projectData = f"{uuid.uuid1()}:{Title}:{Details}:{TotalTarget}:{startTime}:{endTime}:{userInfo[0]}\n"
    saveProjectInFile(projectData)

def listUserProjects(userInfo) :
    print(f"######################## Hello ${userInfo[1]}$ #######################")
    userProjects = getAllUserProjects(userInfo[0])


def editUserProjects(userInfo) :
    print(f"######################## Hello ${userInfo[1]}$ #######################")
    projectID = input("enter project id to edit it : ")
    editUserProject(userInfo[0],projectID)


def deleteUserProjects(userInfo) :
    print(f"######################## Hello ${userInfo[1]}$ #######################")
    projectID = input("enter project id to detele it : ")
    deleteUserProject(userInfo[0],projectID)