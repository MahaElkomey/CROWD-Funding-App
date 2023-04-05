from Registration import userReg
from Login import userLogin
from projectMenu import projectMenu

def mainMenu():
    
    while True :
        print("######################## Welcom to user projects system #######################")
        print("choose one of the list : ")
        print("r ---> Registration")
        print("l ---> Login")
        choice = input("your choice : ")
        if choice == 'r':
            userReg()
            userInfo = userLogin()
            continue
        elif choice == 'l':
            userInfo = userLogin()
            projectMenu(userInfo)
            continue
        else :
            print("Invalid input")
            continue

mainMenu()