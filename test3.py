import sqlite3


wunschliste = ['m', '16', '1.65', 'sportlich', 'nichtraucher', 'schwimmen']

conn = sqlite3.connect('test.db')
c = conn.cursor()

count = 0

for i in range(6):
    if count == 0:
        a = "geschlecht"
    elif count == 1:
        a = "walter"
    elif count == 2:
        a = "groesse"
    elif count == 3:
        a = "figur"
    elif count == 4:
        a = "rauchverhalten"
    elif count == 5:
        a = "hobby"

    b = wunschliste[i-1]

    c.execute('SELECT * from benutzer WHERE ?=?', (a, b))

    for row in c.fetchall():
        print row[1]

    count += 1
