from flask import Flask ,render_template,url_for,request

app = Flask(__name__) 

@app.route('/') # http://127.0.0.1:5000/
def home():
    return render_template('home.html')


@app.route('/userdata')   # http://127.0.0.1:5000/userdata
def userdata():
    # return "Hey this is url for project.html" 
    return render_template('project.html')

@app.route('/predict',methods=['GET','POST'])
def  predict(): 
    if request.method == 'POST':
        age = request.form['age']
        flight_distance  = request.form['flight_distance']
        inflight_entertainment  = request.form['inflight_entertainment']
        baggage_handling  = request.form['baggage_handling']
        cleanliness  = request.form['cleanliness']
        departure_delay  = request.form['departure_delay']
        arrival_delay  = request.form['arrival_delay']
        gender  = request.form['gender']
        customer_type  = request.form['customer_type']
        travel_type  = request.form['travel_type']
        class_type  = request.form['class_type']

        UNSEEN_DATA = [age,flight_distance,inflight_entertainment,baggage_handling,cleanliness,
                        departure_delay,arrival_delay,gender,customer_type,travel_type,class_type]


        # X_train variables  
        # Age	Flight Distance	Inflight entertainment	Baggage handling	Cleanliness	Departure Delay in Minutes
        # 	Arrival Delay in Minutes	Gender_Male	Customer Type_disloyal Customer	Type of Travel_Personal Travel	
        # Class_Eco	Class_Eco Plus
        return UNSEEN_DATA









if __name__ == "__main__": 
    app.run(debug=True)