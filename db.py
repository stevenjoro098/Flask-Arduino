import sqlite3
def insert():
    conn = sqlite3.connect('states.db')

    cur = conn.cursor()

    cur.execute('''INSERT INTO CONTROLTABLE(
                    NAME,STATE) VALUES('FRONT_GATE','TRUE')
                    ''')
    conn.commit()
    conn.close()
def update(state,name):
    conn = sqlite3.connect('states.db')
    cur = conn.cursor()
    sql = 'UPDATE CONTROLTABLE SET STATE = ' + "'" + str(state) + "'" + "WHERE NAME = " + "'" + str(name) + "'"
    print(sql)
    cur.execute(str(sql))

    conn.commit()
    conn.close()
def fetch():
    conn = sqlite3.connect('states.db')

    cur = conn.cursor()

    cur.execute('''SELECT * FROM CONTROLTABLE''')
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()
def main():
    conn = sqlite3.connect('states.db')

    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS CONTROLTABLE')

    sql = '''CREATE TABLE CONTROLTABLE(
                ID INTEGER PRIMARY KEY,
                NAME VARCHAR,
                STATE BOOLEAN
                )'''
    cur.execute(sql)
    print("Table created")
    conn.commit()
    conn.close()
if __name__ == '__main__':
    #main()
    #fetch()
    BACKYARD = 'AQUARIUM'
    FALSE = 'FALSE'
    update(FALSE,BACKYARD)
    #insert()

