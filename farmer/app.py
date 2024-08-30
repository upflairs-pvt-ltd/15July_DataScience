from flask import Flask , render_template,url_for,request
import pandas as pd 
import joblib 
std_scaler = joblib.load('./models/std_scaler.lb')
kmeans_model = joblib.load('./models/kmeans_model.lb')
df = pd.read_csv("./models/filter_crops.csv")

app = Flask(__name__) 

#<password>  replaced with your    
mongodb+srv://ankitk2002121:PEpfghfsCbMYgqYQ@farmerproject.1ytnv.mongodb.net/?retryWrites=true&w=majority&appName=farmerproject

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/predict',methods=['GET','POST'])
def predict(): 
    if request.method == 'POST': 
        N = int(request.form['N'])
        PH = float(request.form['PH'])
        P = int(request.form['P'])
        K = int(request.form['K'])
        humidity = float(request.form['humidity'])
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])   # type == number >> text 
        UNSEEN_DATA = [[N,P,K,temperature,humidity,PH,rainfall]] 
        transformed_data = std_scaler.transform(UNSEEN_DATA)
        cluster = kmeans_model.predict(transformed_data)[0]
        suggestion_crops = list(df[df['cluster_no'] == cluster]['label'].unique())
        return f"suggessted crops : {suggestion_crops}"


if __name__ =="__main__":
    app.run(debug=True) 