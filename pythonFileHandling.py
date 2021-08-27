#date=20/8/2021
#author= karthikeyan B
#Batch= D11

import re
# method to display Menu
def displayMenu():
    print(""" 
                MENU 
           1.Register
           2.LogIn
           3.Exit
           """)

# method to print invalid msgs
def invalid():
    print("INVALID CHOICE! Please select between 1 to 3")

# method to check given Email Id is valid or not
def checkEmail(email,regex):
    res = True
    if (re.fullmatch(regex, email)):
        reg = r'\b[_%#$+-]\b'
        firstChar = email[0]
        if not(firstChar.isnumeric() and re.fullmatch(reg,firstChar)):
            #print("Valid Email")
            res = True
        else:
           print("Invalid Email, Please enter a valid one")
           res = False
    else:
        print("Invalid Email, Please enter a valid one")
        res = False
    return res
# method to get input for forgot password
def getInputId():
    try:
        idvalue = int(input("please enter 1 if you have to go with FORGOT PASSSWORD option, enter 2 to go with exit "))
    except:
        print("Input value error : value provided by user has error")
    else:
        return idvalue
# method to get Email id from user
def getUserEmailId():
    try:
        idvalue = input("Enter the User Email id ")
    except:
        print("Input value error : Id provided by user has error")
    else:
        return idvalue

def getUserId():
    while True:
        regex = r'\b[A-Za-z0-9_%#$+-]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b'
        emailid = getUserEmailId()
        if checkEmail(emailid,regex):
            return emailid

def checkPwd(password):
    flag = 0
    while True:
        if (len(password) < 5):
            flag = -1
            break
        elif (len(password) > 16):
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]", password):
            flag = -1
            break
        elif re.search("\s", password):
            flag = -1
            break
        else:
            flag = 0
            #print("Valid Password")
            return password
    if flag == -1:
        print("Given password didnt match the criteria, Please enter avalid one")
        return "fail"

def getPwd():
    while True:
        password = input("Enter the Password")
        #password = getpass.getpass(prompt='Enter the Password')
        res = checkPwd(password)
        if res != "fail":
            return res

def userValidation(userChoice):
    if userChoice == 1:
        registerAction()
    elif userChoice == 2:
        loginAction()

def searchEmailId(emailid):
    fn = "UsersListFile"
    file = open(fn, 'r')
    for line in file:
        if emailid in line:
            return True
    return False

def searchEmailIdandGetPwd(emailid):
    fn = "UsersListFile"
    file = open(fn, 'r')
    for line in file:
        if emailid in line:
            pwd = line.split(" ")
            return pwd[1]
    return "0"

def registerAction ():
    #file = createUserListFile()
    uId = getUserId()
    try:
        fn = "UsersListFile"
        file = open(fn, 'a+')
        if searchEmailId(uId):
            print("Given Email Id is already registed, Please use Login option")
        else:
            pwd = getPwd()
            file.writelines(uId + " " + pwd + "\n" )
    except IOError:
        print("error while writingin file")
    else:
        file.close()

def loginAction ():
    eId = getUserEmailId()
    if searchEmailId(eId):
        password = input("Enter the Password")
        if searchEmailId(eId+" "+password):
            print("Given Email id and password are valid")
            print(''' 
            *************************************
                    Here is the login page
            *************************************      
            ''')
        else:
            forgotPwd(getInputId(),eId)
    else:
        print("Given Email id does not exist, please proceed with option 1 for register")

def forgotPwd(choice,eId):
    if choice == 1:
        val = searchEmailIdandGetPwd(eId)
        if val != "0":
            print("your password is :"+val)
    elif choice != 1:
        print("Exit from forget password")

def userOperation():
    while True:
        displayMenu()
        try:
            ans = input("Please press 1 for Register & 2 for Login ")
            userChoice = int(ans)
        except:
            print("Given value is not int")
        else:
            if userChoice == 1 or userChoice == 2:
                print('User selected option is {}.'.format(userChoice))
                userValidation(userChoice)
            elif userChoice == 3:
                print("EXIT -----")
                break
            else:
                invalid()

userOperation()
