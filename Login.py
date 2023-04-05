from helper import askforString, checkEmail, ConfirmPasswordFun, validatedPhoneNum
from fileOperation import saveUserInFile,userLoginSearch

def userLogin():
    while True :
        print("######################## User Login #######################")
        Email = checkEmail("enter your Email : ")
        Password = input("enter your password : ")
        userID = userLoginSearch(Email, Password)
        if userID :
            print("####################### Login success ######################")
            return userID