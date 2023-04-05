from helper import askforString, checkEmail, ConfirmPasswordFun, validatedPhoneNum
from fileOperation import saveUserInFile
import uuid  

def userReg():
    print("######################## User Registration #######################")
    FirstName = askforString("enter your First Name : ")
    LastName = askforString("enter your last Name : ")
    Email = checkEmail("enter your Email : ")
    Password = input("enter your password : ")
    ConfirmPassword = ConfirmPasswordFun(Password, "Confirm your password : ")
    MobilePhone = validatedPhoneNum("enter your Mobile phone : ")
    userData = f"{uuid.uuid1()}:{FirstName}:{LastName}:{Email}:{Password}:{MobilePhone}\n"
    saveUserInFile(userData)
    print("####################### Registration success ######################")
    return

