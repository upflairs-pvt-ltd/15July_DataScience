from flask import Flask, render_template,request 
import joblib 
import sqlite3

model = joblib.load("./models/linear_model.lb")
app = Flask(__name__) 


@app.route('/') 
def home(): 
    return render_template('home.html') 


@app.route("/predict", methods=['GET','POST']) 
def predict():
    if request.method =="POST": 
        brand_name = int(request.form["brand_name"]) 
        kms_driven = int(request.form["Kms_Driven"] )
        owner = int(request.form["owner"] )
        age = int(request.form["age"] )
        power = int(request.form["power"] )
        brand_dict = {'Bajaj': 1,'Royal Enfield': 2,'Hero': 3,'Honda': 4,'Yamaha': 5,'TVS': 6,
                        'KTM': 7,'Suzuki': 8,'Harley-Davidson': 9,'Kawasaki': 10,'Hyosung': 11,
                        'Mahindra': 12,'Benelli': 13,'Triumph': 14,'Ducati': 15,'BMW': 16}
                
        brand_dict2 = {value:key  for key, value in brand_dict.items()}
        
        UNSEEN_DATA = [[kms_driven,owner,age,power,brand_name]]   # user input data 
        PREDICTION = model.predict(UNSEEN_DATA)[0][0]   # array([25421.25421])

        ## inserting data into database  

        query_to_insert = """
        Insert into BikeDetails values(?,?,?,?,?,?)
        """
        conn  =  sqlite3.connect('bikedata.db')
        cur = conn.cursor() 
        data  = (owner,brand_dict2[brand_name],kms_driven,power,age,int(round(PREDICTION,2)))
        cur.execute(query_to_insert, data)
        conn.commit() 
        print("Your record has been stored in database")
        cur.close() 
        conn.close()

        return render_template('home.html' , prediction_text= str(round(PREDICTION,2))) 


if __name__ == "__main__": 
    app.run(debug=True) 