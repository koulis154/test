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
    if request.method =='POST':
        image = request.form["image"]
        sound = request.form["sound"]

        if image and sound:
            print(image, sound)
        elif image and len(sound) == 0:
            print(image)
        elif sound and len(image) == 0:
            print(sound)

       
        print(request.form)
      
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
        print(request.form)
        first_name = request.form["first-name"]
        last_name = request.form["last-name"]
        age = request.form["age"]
        email = request.form["email"]
        password = request.form["psw"]
        new_password_1 = request.form["psw-repeat"]
        if "male" in request.form:
            male = request.form["male"]
        elif "female" in request.form:
            female = request.form["female"]
        elif "prefer not to say" in request.form:
            prefer_not_to_say = request.form["prefer not to say"]
        return redirect(url_for('login'))

    return render_template('createaccount.html')

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == "POST":
        user_email = request.form["enter email"]
        password_forgot = request.form["new password"]
        repeat_new_psw = request.form["new password"]

        return redirect(url_for('login'))

    return render_template('forgot.html')


@app.route('/library', methods=['GET', 'POST'])
def library():

	return render_template('library.html')


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
       
       email_1 = 0
       psw_1 = 0
       print(request.form)
       sign_in_1 = 0
       cancel_forgot = 0
       email_1 = request.form["email_1"]
       psw_1 = request.form["psw_1"]

       if "sign_in" in request.form:
            return redirect(url_for('index12'))
        
       if "cancel_forgot" in request.form:
            cancel_forgot = request.form["cancel_forgot"]
    
       
       if request.form.get("forgot") == "Forgot Password":
           return redirect(url_for('forgot'))
       
       if request.form.get("create_account") == "Create new Account":
           return redirect(url_for('createaccount'))
          
       
   return render_template('loginnew.html')

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method =="POST":
        #enter_email = 0
       # current_password = 0
        #new_password = 0
        #save = 0
        print(request.form)
        enter_email = request.form["enter email"]
        current_password = request.form["current password"]
        new_password = request.form["repeat new password"]
        #save = request.form["save"]

        return redirect(url_for('index12'))
    return render_template('settings.html')


# this is so the app won't run if the file is imported somewhere, run using a different methed, etc.
if __name__ == '__main__':
	app.run('127.0.0.1', port=8080, debug=True)  #
    
    
