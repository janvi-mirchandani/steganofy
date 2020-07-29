from flask import Flask, redirect, url_for, request, render_template, session, escape, flash
from flaskext.mysql import MySQL
from stegano import lsb
import os

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] ='root'
app.config['MYSQL_DATABASE_DB'] = 'steganography'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
app = Flask(__name__, instance_path='C:\\Users\\janvi\\PycharmProjects\\Steganography\\venv\\Lib\\static\\uploads\\')
app.secret_key = 'namsonkimbaesungjoo'

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/signin')
def signin():
   return render_template('signin_page.html')
@app.route('/signup')
def signup():
   return render_template('signup_page.html')
@app.route('/add_user',methods = ['POST', 'GET'])
def add_user():
   if request.method == 'POST':
      result = request.form
      username = request.form['username']
      password = request.form['password']
      conn = mysql.connect()
      cursor = conn.cursor()
      sql = "SELECT * FROM users WHERE username = %s"
      cursor.execute(sql, (username,))
      if cursor.fetchone() is not None:
          flash('Username already taken')
          return render_template('signup_page.html')
      else:
        sql = "INSERT INTO users(username, password) VALUES(%s, %s)"
        data = (username,password)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        flash('You were registered successfully')
        return render_template('signin_page.html')
@app.route('/encrypt')
def encrypt():
   return render_template('encryption_page.html')
@app.route('/backtohome')
def backtohome():
    if 'username' in session:
        username = session['username']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT imagepath from images where username='" + username + "'")
    images_data = cursor.fetchall()
    images_list = []
    for row in images_data:
        image = str(row)
        image1 = image.replace("\\\\", "\\")
        image2 = image1.replace("\\r\\n", "")
        image3 = image2.replace("C:\\Users\\janvi\\PycharmProjects\\Steganography\\venv\\Lib\\static\\uploads\\",
                                "")
        image4 = image3[2:-3]
        images_list.append(image4)
    return render_template("home_page.html", images_list=images_list)
@app.route('/message/<name>')
def message(name):
    img_decrypt_dir = os.path.join(
        os.path.dirname(app.instance_path), ''
    )
    final_path = os.path.join(img_decrypt_dir, name)
    message = lsb.reveal(final_path)
    flash('Decrypted Successfully')
    return render_template('message_display.html',decrpt_message = message)
@app.route('/decrypt')
def decrypt():
    if 'username' in session:
        username = session['username']
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT imagepath from images where username='" + username + "'")
    images_data = cursor.fetchall()
    images_list = []
    for row in images_data:
        image = str(row)
        image1 = image.replace("\\\\", "\\")
        image2 = image1.replace("\\r\\n", "")
        image3 = image2.replace("C:\\Users\\janvi\\PycharmProjects\\Steganography\\venv\\Lib\\static\\uploads\\",
                                "")
        image4 = image3[2:-3]
        images_list.append(image4)
    return render_template("decryption_page.html", images_list=images_list)
@app.route('/encryption',methods = ['POST', 'GET'])
def encryption():
    if request.method == 'POST':
        result = request.form
        oldpath = request.files['oldpath']
        msg = request.form['msg']
        newpath = request.form['newpath']
        newpath = newpath+'.png'
        img_upload_dir = os.path.join(
            os.path.dirname(app.instance_path), ''
        )
        lsb.hide(oldpath, message=msg).save(os.path.join(img_upload_dir,newpath))
        if 'username' in session:
            username = session['username']
        sql = "INSERT INTO images(username, imagepath) VALUES(%s, %s)"
        data = (username, newpath)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        cursor.execute("SELECT imagepath from images where username='" + username + "'")
        images_data = cursor.fetchall()
        images_list = []
        for row in images_data:
            image = str(row)
            image1 = image.replace("\\\\", "\\")
            image2 = image1.replace("\\r\\n", "")
            image3 = image2.replace("C:\\Users\\janvi\\PycharmProjects\\Steganography\\venv\\Lib\\static\\uploads\\",
                                    "")
            image4 = image3[2:-3]
            images_list.append(image4)
        flash('Encrypted Successfully')
        return render_template("home_page.html",images_list=images_list)
@app.route('/home',methods = ['POST', 'GET'])
def home():
   if request.method == 'POST':
      result = request.form
      session['username'] = request.form['username']
      username = request.form['username']
      password = request.form['password']
      cursor = mysql.connect().cursor()
      cursor.execute("SELECT * from users where username='" + username + "' and password='" + password + "'")
      data = cursor.fetchone()
      if data is None:
         return render_template("error_page.html", result=result)
      else:
         cursor.execute("SELECT imagepath from images where username='" + username + "'")
         images_data = cursor.fetchall()
         images_list = []
         for row in images_data:
            image = str(row)
            image1 = image.replace("\\\\", "\\")
            image2 = image1.replace("\\r\\n","")
            image3 = image2.replace("C:\\Users\\janvi\\PycharmProjects\\Steganography\\venv\\Lib\\static\\uploads\\", "")
            image4 = image3[2:-3]
            images_list.append(image4)
         flash('You were successfully logged in')
         return render_template("home_page.html", result=result, images_list = images_list )
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return render_template('welcome_page.html')

if __name__ == '__main__':
   app.run(debug = True)
