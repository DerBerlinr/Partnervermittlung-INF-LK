import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()
print("Opened database successfully")

c.execute('CREATE TABLE IF NOT EXISTS testtable(name TEXT, vorname TEXT, geburtsdatum TEXT, geschlecht TEXT, groesse TEXT, figur TEXT, rauchverhalten TEXT, orientierung TEXT, hobby TEXT, adresse TEXT, telefonnummer TEXT, email TEXT, benachichtigung TEXT, zahlungsart TEXT, iban TEXT, kontaktaufnahme TEXT)')

print("Table created successfully")

c.execute("INSERT INTO testtable VALUES('Hoffmann', 'Peter', '01.01.0001', 'm', '1.68', 'vollschlank', 'nichtraucher', 'heterosexuell', 'fernsehen', 'Musterweg 12; 34567 Musterstadt', '98437659', 'a.a@a.com', 'chiffre', 'lastschrift', '12756', 'post')")

conn.commit()
c.close()
conn.close()
