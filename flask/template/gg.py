from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import pyodbc
app = Flask(__name__,template_folder='templates',static_folder='templates/static')
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

def connection(query,getResult = True):
    s = 'DESKTOP-EGO85AB\SQLEXPRESS' #Your server name
    d = 'website' # database
    u = 'Jason' #Your login
    p = '123' #Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
    conn = pyodbc.connect(cstr)
    print('CONNECTED!')
    cursor = conn.cursor()
    cursor.execute(query)
    if getResult:
        result = cursor.fetchall()
    else:
        result = None
    conn.commit()
    conn.close()
    return result



@app.route("/", methods=['POST','GET'])
def hello_world():
    # result = connection("insert into customer values ('jason', 'leong', 23, '123000@gmail.com', 'M')",getResult=False)
    if request.method == 'POST':
        result = connection("select email from customer where id = 1", getResult=True)
        session['email'] = result
        return redirect(url_for('result'))
    t = url_for('static', filename='images/AI.jpg')
    return render_template('gg.html',r = {'a':'a','b':'b','testing':t})

@app.route("/result")
def result():
    print(session['email'][0][0])
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)

# pip install pyodbc
# C:\Program Files\Microsoft SQL Server (path of sql servers)
