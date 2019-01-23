import sqlite3

def datab(name, college, address, phone):

    connection = sqlite3.connect('student.db') #file name
    print("Database Opened Successfully !")
    TABLE_NAME = "student_table"
    STUDENT_ID = "student_id"
    STUDENT_NAME = "student_name"
    STUDENT_COLLEGE = "student_college"
    STUDENT_ADDRESS = "student_address"
    STUDENT_PHONE = "student_phone"

    connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " +STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT," + STUDENT_COLLEGE + " TEXT, "+
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")

    print("Table is created Successfully.")

    '''
    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                   STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                   STUDENT_PHONE + " ) VALUES ('"+name+"', '"+college+"', "
                   "'"+address+"', "+str(phone)+"); ")
    '''


## Retrieve Record
def ret():
    connection = sqlite3.connect('student.db')  # file name
    print("Database Opened Successfully !")
    TABLE_NAME = "student_table"
    cursor =connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    for row in cursor:
        print("Student id is: ", row[0])
        print("Student name is: ", row[1])
        print("Student college is: ", row[2])

    connection.commit()
