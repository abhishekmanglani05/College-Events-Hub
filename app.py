from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
  
  
app = Flask(__name__)
  
  
app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'college_evenets'
  
mysql = MySQL(app)
  
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connect.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        # cursor.execute(f'SELECT * FROM user WHERE email = "{email}" AND password = "{password}"')
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            # session['userid'] = user['userid']
            session['name'] = user['name']
            email_a = user['email']
            # branch= user['Branch']
            # roll_no= user['Roll_no']
            # score_10= user['10th_Score']
            # score_12= user['12th_Score']
            # cgpa= user['CGPA']
            # attendence= user['Attendance']
            mesage = 'Logged in successfully !'
            cursor = mysql.connect.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM events")
            myresult=cursor.fetchall()

            # return render_template('search01.html', a = myresult)
            return render_template('user.html', d=email_a, a=myresult)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)
  
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))
  
@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']

        try:
            conn = mysql.connect

            if conn:
                cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        # cursor = mysql.connect.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
                account = cursor.fetchone()
                if account:
                    mesage = 'Account already exists !'
                elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                    mesage = 'Invalid email address !'
                elif not userName or not password or not email:
                    mesage = 'Please fill out the form !'
                else:
                    cursor.execute('INSERT INTO user (name, email, password) VALUES (% s, % s, % s)', (userName, email, password ))
                    # cursor.execute(f'INSERT INTO user (name, email, password) VALUES ({userName}, {email}, {password})')
                    conn.commit()
                    cursor.close()
                    mesage = 'You have successfully registered !'

            else:
                return "Connection not established."
            
        except Exception as e:
            return f"An error occurred: {str(e)}"
                
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)

@app.route('/login01')
def login01():
    return render_template('login01.html')

@app.route('/login01a', methods =['GET', 'POST'])
def login01a():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connect.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM usersss WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            # session['userid'] = user['userid']
            session['name'] = user['name']
            email_a = user['email']
            # branch= user['Branch']
            # roll_no= user['Roll_no']
            # score_10= user['10th_Score']
            # score_12= user['12th_Score']
            # cgpa= user['CGPA']
            # attendence= user['Attendance']
            # mesage = 'Logged in successfully !'

            #get data
            # cursor = mysql.connect.cursor(MySQLdb.cursors.DictCursor)
            # cursor.execute("SELECT name, email FROM user WHERE Branch='AIML';")
            # myresult=cursor.fetchall()
            return render_template('user01.html', d=email_a)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login01.html', mesage = mesage)

@app.route('/register01', methods =['GET', 'POST'])
def register01():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']

        try:
            conn = mysql.connect

            if conn:
                cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        # cursor = mysql.connect.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM usersss WHERE email = % s', (email, ))
                account = cursor.fetchone()
                if account:
                    mesage = 'Account already exists !'
                elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                    mesage = 'Invalid email address !'
                elif not userName or not password or not email:
                    mesage = 'Please fill out the form !'
                else:
                    cursor.execute('INSERT INTO usersss (name, email, password) VALUES (% s, % s, % s)', (userName, email, password ))
                    conn.commit()
                    cursor.close()
                    mesage = 'You have successfully registered !'

            else:
                return "Connection not established."
            
        except Exception as e:
            return f"An error occurred: {str(e)}"
                
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register01.html', mesage = mesage)


@app.route('/edit', methods =['GET', 'POST'])
def edit():
    # message=""
    data1 = request.form['eventname']
    data2 = request.form['eventdetail']
    data3 = request.form['contact']
    data4 = request.form['link']
    try:
        conn = mysql.connect
        if conn:
                cursor = conn.cursor(MySQLdb.cursors.DictCursor)
        # cursor = mysql.connect.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('INSERT into events values(%s,%s,%s,%s)', (data1, data2, data3, data4) )
                conn.commit()
                cursor.close()
                return render_template("success.html")
                # message="success"
        else:
            return "connection not extablished"
    
    except Exception as e:
            return f"An error occurred: {str(e)}"
    
if __name__ == "__main__":
    app.run(debug=True)