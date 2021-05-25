from flask import Flask,render_template,request
import joblib
model=joblib.load("model.sav")



app=Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/prediction' , methods=['POST'])
def result():
    expe=float(request.form['exp'])
    pred=model.predict([[expe]])
    return render_template("index.html",predi=pred[0])





if __name__=="__main__":
    app.run(debug=True)