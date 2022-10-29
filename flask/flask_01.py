from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='template',static_folder='template/static')


# @app.route('/')
# @app.route('/index')
@app.route('/testing', methods=['GET', 'POST'])
def index():
	if request.method =='POST':
		print(request.form.get('first_name'))
	return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():

	return render_template('upload.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        very_bad= 0
        bad = 0
        average = 0
        good = 0
        very_good = 0
        feedback = 0
        print(request.form)
        
        if "one" in request.form:
            very_bad = request.form["one"]
            
        elif "two" in request.form:
            bad = request.form["two"]
        
        elif "three" in request.form:
            average = request.form["three"]
                
        elif "four" in request.form:
            good = request.form["four"]
        
        elif "five" in request.form:
            very_good = request.form["five"]
        
        elif "subject" in request.form:
            feedback = request.form["subject"]
            
        

        

    return render_template('contact.html')


@app.route('/account', methods=['GET', 'POST'])
def createaccount():
    if request.method =="POST":
        first_name = 0
        last_name = 0
        age = 0
        email = 0
        password = 0
        new_password_1 = 0
        sign_in = 0
        male = 0 
        female = 0
        prefer_not_to_say = 0
        print(request.form)
       
        if "first-name" in request.form:
            first_name = request.form["first-name"]
            
        elif "last-name" in request.form:
            last_name = request.form["last-name"]
       
        elif "age" in request.form:
            age = request.form["age"]

        elif "email" in request.form:
            email = request.form["email"]

        elif "psw" in request.form:
            password = request.form["psw"]
        
        elif "psw-repeat" in request.form:
            new_password_1 = request.form["psw-repeat"]

        elif "male" in request.form:
            male = request.form["male"]

        elif "female" in request.form:
            female = request.form["female"]
        
        elif "prefer not to say" in request.form:
            new_password_1 = request.form["prefer not to say"]

   
        return redirect(url_for('login'))
    return render_template('createaccount.html')


@app.route('/forgot', methods=['GET', 'POST'])
def forgot():

    return render_template('forgot.html')


@app.route('/library', methods=['GET', 'POST'])
def library():

	return render_template('library.html')




"""@app.route('/table', methods=['GET', 'POST'])
def table():

	return render_template('table.html')
"""

@app.route('/index', methods=['GET', 'POST'])
def index12():
    if request.method =="POST":

       
        if request.form.get("library") == "Library":
            return redirect(url_for('library'))
            
        elif request.form.get("upload") == "Upload":
            return redirect(url_for('upload'))
        
        elif request.form.get("contact") == "Contact Us":
            return redirect(url_for('contact'))
        
        
        elif request.form.get("settings") == "Settings":
            return redirect(url_for('settings'))
            
        elif request.form.get("loginnew") == "Log out":
            return redirect(url_for('login'))    
    
    return render_template('index12.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    
   if request.method =="POST":
       
        if "first-name" in request.form:
            first_name = request.form["first-name"]
            
        elif "last-name" in request.form:
            last_name = request.form["last-name"]
       
        elif "age" in request.form:
            age = request.form["age"]

        elif "email" in request.form:
            email = request.form["email"]





       if request.form.get("sign_in") == "Sign in":
           return redirect(url_for('index12'))
       
       elif request.form.get("forgot") == "Forgot Password":
       
           return redirect(url_for('forgot'))
       
       elif request.form.get("create_account") == "Create new Account":
           return redirect(url_for('createaccount'))
          
           redirect(url_for('index12'))
      
       
   return render_template('loginnew.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method =="POST":
        enter_email = 0
        current_password = 0
        new_password = 0
        save = 0
        print(request.form)
       
        if "enter email" in request.form:
            enter_email = request.form["enter email"]
           
        elif "current password" in request.form:
            current_password = request.form["current password"]
       
        elif "repeat new password" in request.form:
            new_password = request.form["repeat new password"]
        
        elif "save" in request.form:
            save = request.form["save"]

        return redirect(url_for('login'))
    return render_template('settings.html')


# this is so the app won't run if the file is imported somewhere, run using a different methed, etc.
if __name__ == '__main__':
	app.run('127.0.0.1', port=8080, debug=True)  #
    
    
