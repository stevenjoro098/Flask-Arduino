import sqlite3
states_dict = {}
def fetch():
    conn = sqlite3.connect('states.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM CONTROLTABLE''')
    result = cur.fetchall()
    #print(result)
    conn.commit()
    conn.close()
    return result
for values in fetch():
    #print(values[1],values[2])
    states_dict[str(values[1])] = values[2]
    #remapping the states
for items in states_dict.values():
        #print(items)
    if items == "False":
        print(0)
    else:
        print(1)
#print(states_dict.values())
import serial
ser = serial.Serial('COM3')
ser.write(b'2')