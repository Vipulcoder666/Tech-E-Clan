from flask import *
from flask_mysqldb import MySQL
from datetime import timedelta
from flask_mail import *

app = Flask(__name__)
app.secret_key = "alam"
# app.permanent_session_lifetime = timedelta(minutes=2)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mdnesar@786'
app.config['MYSQL_DB'] = 'techeclan'
app.config['MYSQL_PORT'] = 3308
mysql = MySQL(app)

mail = Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nesaralam9890@gmail.com'
app.config['MAIL_PASSWORD'] = 'rfqkvtcgmfanacin'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/registration',methods=['GET','POST'])
def registration():
    if request.method == "POST":
        x = request.form
        cur = mysql.connection.cursor()
        cur.execute(f"insert into users(name,email,phone,gender,dob,college,year,course,aadhar) values({x['name']},{x['email']},{x['phone']},{x['gender']},{x['dob']},{x['college']},{x['year']},{x['course']},{x['aadhar']}))")
        mysql.connection.commit()
        cur.close()
        flash("Register Successfull !")
        return redirect(url_for('registration'))
    else:
        return render_template('registration.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/update')
def update():
    return render_template('update.html')


if __name__=="__main__":
    app.run(debug=True)