import re
import datetime

def askforInt(message):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("--- invalid number please enter it again ---")

def askforString(message):
    while True:
        val = input(message)
        if val.isalpha():
            return val
        print("--- invalid string please enter it again ---")

# Define a function for validating an Email
def checkEmail(message):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    while True:
        email = input(message)
        if(re.fullmatch(regex, email)):
            return email
        print("--- invalid email please enter it again ---")
    
def ConfirmPasswordFun(password,message):
    while True:
        ConfirmPassword = input(message)
        if password == ConfirmPassword:
            return ConfirmPassword
        print("--- your password dose not match ---")

def validatedPhoneNum(message):
    while True:
        phone = input(message)
        if phone.isdigit() and len(phone) == 11 :
            if phone[:3] == '010' or phone[:3] == '011' or phone[:3] == '012' or phone[:3] == '014' or phone[:3] == '015':
                return phone
              
        print("--- invalid phone number please enter it again ---")

def dateValidated(message) :
    date_format = '%Y-%m-%d'
    while True :
        date = input(message)
        date_string = date
        try:
            dateObject = datetime.datetime.strptime(date_string, date_format)
            return date
        except ValueError:
            print("Incorrect data format, should be YYYY-MM-DD")

