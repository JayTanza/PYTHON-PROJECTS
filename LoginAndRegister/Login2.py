import sqlite3

conn = sqlite3.connect('Database/maindatabase.db')
query = ('''CREATE TABLE INFORMATION
        (NAME   TEXT    NOT NULL,
        AGE     INT     NOT NULL,
        ADDRESS     CHAR(50),
        SALARY      REAL);''')
conn.execute(query)
conn.close()