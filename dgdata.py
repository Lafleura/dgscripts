import sqlite3

conn = sqlite3.connect('dgscripts')

c = conn.cursor()

def getCourses():
    while True:
        cname = input('Course name: ')
        cdist = input('Miles to course: ')
        cdiff = input('Course difficulty: ')
        cfeet = input('Total footage of course: ')
        c.execute("INSERT INTO courses VALUES (?, ?, ?, ?)", (cname, cdist, cdiff, cfeet, ))
        again = input("Do you want to add another entry? (Y/N) ")
        if again == "N":
            break
