from flask import Flask,render_template,request
import pandas as pd
import pickle


app=Flask(__name__,template_folder="template")
data=pd.read_csv('Cleaned_data.csv')
pipe=pickle.load(open("RidgeModel.pk","rb"))

@app.route('/agents')
def agents():
    # Render the agent.html template
    return render_template('agent.html')



@app.route('/')
def index():
    
    locations=sorted(data['location'].unique())
    return render_template('index.html',locations=locations)


@app.route('/predict', methods=['POST'])
def predict():
    location=request.form.get('location')
    bhk=request.form.get("bhk")
    bath=request.form.get("bath")
    sqft=request.form.get("total_sqft")
    
    print(location,bhk,bath,sqft)
    input = pd.DataFrame([[location, sqft, bath, bhk]], columns=["location", "total_sqft", "bath", "bhk"])

    prediction=pipe.predict(input)[0]
    result=prediction   
    return str(result)



if __name__=="__main__":
     app.run(debug=True,port=5001) 
