from flask import Flask,render_template,request,redirect,url_for
import joblib
from feverGUI import predict_medicine
#app=Flask(__name__,template_folder='C:\\Users\\raghu\\Desktop\\Medicine')
app=Flask(__name__,template_folder='C:\\Users\\raghu\\Desktop\\new file\\templates')

@app.route('/send',methods=['GET','POST'])
def send():
    if request.method=='POST':
        name=request.form['name']
        gender=request.form['gender']
        age=request.form['age']
        temperature=request.form['temperature']
        cold=request.form['cold']
        if cold.lower() == "yes":
            cold=1
        else:
            cold=0
        if age in range(1, 12):
            age=0
        elif age in range(13, 18):
            age=1
        else:
            age=2
        c=predict_medicine(name,gender,age,temperature,cold)
        return render_template("category.html",c=c)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['password']
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            return redirect(url_for('error'))
        else:
            return redirect(url_for('predict'))
    return render_template('login.html')
    
@app.route('/aboutus',methods=['GET'])
def aboutus(): 
    return render_template('aboutus.html')       
                   
@app.route('/predict',methods=['GET','POST'])
def predict(): 
    return render_template('predict.html')
    
@app.route('/error',methods=['GET','POST'])
def error(): 
    return render_template('error.html')   

@app.route('/')
def runit():
    return render_template('index.html')
if (__name__=='__main__'):
    nb=joblib.load('feverGUI.pkl')
    app.run()
