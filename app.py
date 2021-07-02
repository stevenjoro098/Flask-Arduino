from flask import Flask, render_template, request, jsonify, redirect, url_for
import serial,sqlite3
import pyfirmata
import time,sys
#from .db import fetch,update
state = ''
ser = ''
app = Flask(__name__)
def fetch():
    conn = sqlite3.connect('states.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM CONTROLTABLE''')
    result = cur.fetchall()
    print(result)
    conn.commit()
    conn.close()
    return result
def arduino_communications(pin, state):
    try:
        states = fetch()
        ser = serial.Serial('COM3', 9600, timeout=1)
        # ser.close()
        while ser.is_open == True:
            # var = input('enter value')
            fetchs = fetch
            print(fetch)
            var = str(value)
            print(var)
            ser.write(var.encode('utf-8'))
            print(ser.write(var.encode('utf-8')))
            time.sleep(3)
            # ser.close()

        # print(ser.is_open)
    except:
        pass


@app.route('/')
def main():
    state_dict = {}
    state_data = fetch()
    for data in state_data:
        state_dict[str(data[1])] = data[2]
    print(state_dict)

    return render_template('main.html', state=state_dict)


@app.route('/frontlights',methods=['POST', 'GET'])
def lights():
    if request.method == 'POST':
        decor = ''
        frontlight = request.values #fetch the user input from the browser
        decor = request.values['decor']
        print(frontlight)
        print('frontlight is ',frontlight)
        print('decor is ', decor)
        """ 
        try:
            conn = sqlite3.connect('states.db')
            cur = conn.cursor()
            sql = 'UPDATE CONTROLTABLE SET STATE = ' + "'" + str(frontlight) + "'" + "WHERE NAME = FRONT_LIGHT"
            print(sql)
            print(str(frontlight))
            cur.execute(str(sql))

            conn.commit()
            conn.close()
        except:
            return "Error"
        """


    return redirect(url_for('main'))

@app.route('/api/v1/')
def api_data():

    data = fetch()
    print(data)
    return jsonify(data)
@app.route('/api/v1/control', methods = ['GET','POST'])
def control_api():
    query_param = request.get_json()
    name = query_param.get('name')
    state = query_param.get('state')
    print(query_param, 'Name', name, 'STATE', state)
    arduino_communications(name,state)
    try:
        conn = sqlite3.connect('states.db')
        cur = conn.cursor()
        sql = 'UPDATE CONTROLTABLE SET STATE = ' + "'" + str(state) + "'" + "WHERE NAME = " + "'" + str(name) + "'"
        print(sql)
        cur.execute(str(sql))

        conn.commit()
        conn.close()
        return "Command Executed"
    except:
        return "Error Posting Data"
    return "Successful Received"
@app.route('/api/v1/motion')
def motion():
    motion_data = {"front_gate":True,
                   "front_door":False,
                   "left_wing":False,
                   "right_wing":True,
                   "back_yard":True}
    return jsonify(motion_data)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=800,debug=True) #server runs on IP address and port