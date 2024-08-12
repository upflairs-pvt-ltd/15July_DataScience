from flask import Flask ,render_template,url_for,request
app = Flask(__name__) 

@app.route('/')  # http://127.0.0.1:5000/
def home(): 
    # return "Hii this is home page "
    return render_template('home_page.html')


@app.route('/courses')  # http://127.0.0.1:5000/courses
def courses(): 
    # return "Hii this is home page "
    return render_template('courses.html')

@app.route('/contact')  # http://127.0.0.1:5000/contact
def contact(): 
    # return "Hii this is home page "
    return render_template('contact.html')


@app.route('/userdata',methods=['GET','POST'])
def userdata():
    if request.method == 'POST': 
        username = request.form['username']
        useremail = request.form['useremail']
        usersubject = request.form['usersubject']
        usermessage = request.form['usermessage']
        user_recieved_data = [username,useremail,usersubject,usermessage]
        
        return user_recieved_data



        # return "Hiii i am ready to return your data"


if __name__ =="__main__": 
    app.run(debug=True)