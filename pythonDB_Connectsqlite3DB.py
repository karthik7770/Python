import sqlite3
# method to indicate invalid choice
from sqlite3 import OperationalError, Error

# method to print invalid msgs
def invalid():
    print("INVALID CHOICE! Please select between 1 to 6")

# method to display Menu
def displayMenu():
    print(""" 
                MENU 
           1.Add a Student
           2.Edit  a Student
           3.Delete Student
           4.Get all Student
           5.Get a Student
           6.Exit
           """)

# method to create new table
def createtable(dbcon):
    # dbConnect.execute("drop table if exists StudentsD")
    try:
        dbcon.execute(
            "Create table StudentsD  (id int, name txt, department text, subject1Mark int, subject2Mark int, "
            "subject3Mark "
            "int, subject4Mark int, subject5Mark int, Total int, Average int, Grade text)")
        dbcon.commit()
    except OperationalError:
        print("Table already exist")

# method to do add operation
def addStudent(db):
    print("ADD NEW STUDENT DATA ")
    userInputs = getInputs()

    insertQuery = 'insert into StudentsD (id, name, department, subject1Mark, subject2Mark, subject3Mark, ' \
                  'subject4Mark, subject5Mark,Total, Average, Grade) values ({0},"'"{1}"'","'"{2}"'",{3},{4},{5},{6},' \
                  '{7},{8},{9},"'"{10}"'")'.format(
        userInputs['id'], userInputs['name'], userInputs['department'],
        userInputs['subject1Mark'], userInputs['subject2Mark'], userInputs['subject3Mark'],
        userInputs['subject4Mark'], userInputs['subject5Mark'], userInputs['Total'],
        userInputs['Average'], userInputs['Grade'])
    print("below is the query for insert \n" + insertQuery)
    createtable(db)
    db.execute(insertQuery)
    db.commit()
    print("successfully added")

# method to find student id is present in db or not
def checkIdPresent(id, db):
    check = False
    query = "select * from StudentsD where id =" + str(id)
    result = db.execute(query)
    if result.rowcount != 0:
        print(result.fetchall())
        check = True
    return check

# method to do update operation (edit)
def editStudent(dbcon):
    print("EDIT STUDENT DATA ")
    userInputs = getInputs()
    if checkIdPresent(userInputs['id'], dbcon):
        print("Given student id is present in DB")
        update_query = 'UPDATE StudentsD  SET subject1Mark = {0}, subject2Mark = {1}, subject3Mark = {2}, ' \
                       'subject4Mark = {3}, subject5Mark = {4}, Total = {5}, Average = {6}, Grade = "'"{7}"'"' \
                       ' WHERE  id = {8} '.format(userInputs['subject1Mark'], userInputs['subject2Mark'],
                                                  userInputs['subject3Mark'],
                                                  userInputs['subject4Mark'], userInputs['subject5Mark'],
                                                  userInputs['Total'],
                                                  userInputs['Average'], userInputs['Grade'], userInputs['id'])
        print("below is the query for update query \n" + update_query)
        result = dbcon.execute(update_query)
        dbcon.commit()
        print("Given student id is updated with new values")
    else:
        print("Given student id is not present")

def deleteStudent(dbcon):
    print('User selected option is {}.'.format(3))
    print("EDIT STUDENT DATA ")
    id = getInputId()
    if checkIdPresent(id, dbcon):
        print("Given student id is present in DB")
        query = "delete from StudentsD where id =" + str(id)
        result = dbcon.execute(query)
        dbcon.commit()
    else:
        print("Given student id is not present in DB")

def getAllStudent(dbcon):
    print("GET ALL STUDENT DATA ")
    query = "select * from StudentsD"
    result = dbcon.execute(query)
    for row in result:
        print(row)

def getStudent(dbcon):
    query = "select * from StudentsD where id = " + str(getInputId())
    result = dbcon.execute(query)
    for row in result:
        print(row)

def userValidation(userChoice, db):
    while True:
        if userChoice == 1:
            addStudent(db)
        elif userChoice == 2:
            editStudent(db)
        elif userChoice == 3:
            deleteStudent(db)
        elif userChoice == 4:
            getAllStudent(db)
        elif userChoice == 5:
            getStudent(db)
        break

def userOperation(db):
    while True:
        displayMenu()
        try:
            ans = input("What would you like to do? ")
            userChoice = int(ans)
        except:
            print("Given value is not int")
        else:
            if userChoice <= 5 and userChoice >= 1:
                print('User selected option is {}.'.format(userChoice))
                userValidation(userChoice, db)
            elif userChoice == 6:
                print("EXIT -----")
                break
            else:
                invalid()

def getInputId():
    try:
        idvalue = int(input("Enter the student id "))
    except:
        print("Input value error : Id provided by user has error")
    else:
        return idvalue

def getInputName():
    try:
        name = input("Enter the name of the student ")
    except:
        print("Input value error : name provided by user has error")
    else:
        return name

def getInputDept():
    try:
        department = input("Enter Student Department ")
    except:
        print("Input value error : department provided by user has error")
    else:
        return department

def calcTotal(subject1Mark, subject2Mark, subject3Mark, subject4Mark, subject5Mark):
    total = subject1Mark + subject2Mark + subject3Mark + subject4Mark + subject5Mark
    return total

def calcGrade(avg):
    grade = 'Pass'
    if avg > 90:
        grade = 'S'
    elif avg > 70:
        grade = 'A'
    elif avg > 50:
        grade = 'B'
    return grade

def calcAverage(totalMarks):
    avg = totalMarks / 5
    return avg

def getInputs():
    inputs = {}
    id = getInputId()
    name = getInputName()
    department = getInputDept()
    try:
        subject1Mark = int(input("subject 1 Mark = "))
        subject2Mark = int(input("subject 2 Mark = "))
        subject3Mark = int(input("subject 3 Mark = "))
        subject4Mark = int(input("subject 4 Mark = "))
        subject5Mark = int(input("subject 5 Mark = "))
    except:
        print("Input value provided has error")
    else:
        total = calcTotal(subject1Mark, subject2Mark, subject3Mark, subject4Mark, subject5Mark)
        avg = calcAverage(total)
        grade = calcGrade(avg)
        inputs = {'id': id, 'name': name, 'department': department,
                  'subject1Mark': subject1Mark,
                  'subject2Mark': subject2Mark,
                  'subject3Mark': subject3Mark,
                  'subject4Mark': subject4Mark,
                  'subject5Mark': subject5Mark,
                  'Total': total,
                  'Average': avg,
                  'Grade': grade}
    return inputs

try:
    dbcon = sqlite3.connect("my_database9_8_2021.db")
    userOperation(dbcon)
except Error as e:
    print(e)
else:
    dbcon.close()
finally:
    print("***************************")
