from flask import Flask,render_template,request,url_for
from datetime import datetime
import pymysql
import pymysql.cursors


app=Flask(__name__)
app.config['SECRET_KEY'] = '123'

def setup_connection():
    user = 'admin'
    DB_PASSWORD = 'welcome123'
    DB_PORT = 3306
    passw = DB_PASSWORD
    host =  'database1.co7vv5vbws2n.ap-south-1.rds.amazonaws.com'
    port = DB_PORT
    database = 'startupsupport'
    conn = pymysql.connect(host=host,port=port,user=user,passwd=passw,db=database,cursorclass = pymysql.cursors.DictCursor)
    return conn

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form  :
        username = request.form['username']
        password=request.form['password']
        comp_name = request.form['comp_name']
        address = request.form['address']
        comp_email = request.form['company_email']
        phone = request.form['phone']
        prod = request.form['product_desc']    
        email = request.form['contact_person_email'] 
        support=request.form['Support_needed']
        website=request.form['Website']
        conn = setup_connection()
        print("connected")
        cur = conn.cursor()
        cur.execute('SELECT * FROM startupdetails WHERE username = % s', (username, ))
        account = cur.fetchone()
        if account:
            msg = 'Account already exists !'
        
        else:
            cur.execute('INSERT INTO startupdetails VALUES (NULL, % s,%s, % s, % s, % s, % s, % s, % s, % s, % s)', (username, password,comp_name, address, comp_email, phone, prod, email,support,website ))
            conn.commit()
            msg = 'You have successfully registered !'
        cur.close()
        conn.close()
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
        
    return render_template('register1.html', msg = msg)

@app.route('/register_helper', methods =['GET', 'POST'])
def register_helper():
    msg = ''
    if request.method == 'POST' and 'username' in request.form  :
        username = request.form['username']
        password=request.form['password']
        comp_name = request.form['comp_name']
        address = request.form['address']
        email = request.form['email']
        phone = request.form['phone']
        conn = setup_connection()
        print("connected")
        cur = conn.cursor()
        cur.execute('SELECT * FROM helperdetails WHERE username = % s', (username, ))
        account = cur.fetchone()
        if account:
            msg = 'Account already exists !'

        else:
            cur.execute('INSERT INTO helperdetails VALUES (NULL, % s,%s, % s, % s, % s, % s)', (username, password,comp_name, address, email, phone ))
            conn.commit()
            msg = 'You have successfully registered !'
        cur.close()
        conn.close()
    elif request.method == 'POST':
        msg = 'Please fill out the form !'

    return render_template('register_helper.html', msg = msg)


#start page
@app.route('/', methods =['GET', 'POST'])
@app.route('/index', methods =['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'Startup Login':
            pass

        elif  request.form.get('action2') == 'Helper Login':
            pass
    elif request.method == 'GET':
        return render_template('index.html')
    return render_template('index.html')

@app.route('/get_about')
def get_about():
    return render_template('about.html')

@app.route('/startup_ideas')
def startup_ideas():
    return render_template('startup_ideas.html')

@app.route('/get_contact')
def get_contact():
    return render_template('contact.html')


@app.route('/get_details/<name>', methods =['GET', 'POST'])
def get_details(name):
        conn = setup_connection()
        print("connected")
        username={name}
        cur = conn.cursor()
        cur.execute('SELECT * FROM startupdetails WHERE username = % s', (username, ))
        data = cur.fetchone()
        msg=''
        return render_template('display1.html', msg = msg,data=data)


@app.route('/login_helper', methods =['GET', 'POST'])
def login_helper():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = setup_connection()
        print("connected")
        cur = conn.cursor()
        cur.execute('SELECT * FROM helperdetails  WHERE username = % s and password = %s', (username,password ))
        account = cur.fetchone()
        if account:
            msg = 'Logged in successfully !'
            return render_template('startup_ideas.html' )
        else:
            msg = 'Incorrect username / password !'
            return render_template('login2.html', msg = msg)
        cur.close()
        conn.close()
    return render_template('login2.html', msg = msg)


@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = setup_connection()
        print("connected")
        cur = conn.cursor()
        cur.execute('SELECT * FROM startupdetails WHERE username = % s and password= %s', (username,password ))

        account = cur.fetchone()
        if account:
            msg = 'Logged in successfully !'
            cur.execute('SELECT * FROM startupdetails WHERE username = % s', (username, ))
            data = cur.fetchone()
            return render_template('display1.html', msg = msg,data=data)
        else:
            msg = 'Incorrect username / password !'
        cur.close()
        conn.close()
    return render_template('login1.html', msg = msg)
