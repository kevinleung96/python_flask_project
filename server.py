from flask import Flask, render_template, redirect, url_for,request
import mysql.connector
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './upload'

conn = mysql.connector.connect(
   host = "hostname",
   user = 'username',
   password = 'password',
   database = 'databasename'
)

cursor = conn.cursor()


# create routes
@app.route("/")  #decorator
@app.route("/home")  #decorator
def home():
    return render_template('home.html')


@app.route('/market')
def market():
   items = [
      {'id': 1, 'name': 'phone', 'barcode': '232as', 'price': 200},
      {'id': 2, 'name': 'laptop', 'barcode': '12ds', 'price': 120},
      {'id': 3, 'name': 'keyboard', 'barcode': '4ds', 'price': 100},
   ]
   return render_template('market.html', items = items)


@app.route('/add_user', methods = ['POST', 'GET'])
def add_user():
   if request.method == 'POST':
      user_name = request.form.get('user_name')
      email = request.form.get('email')
      city = request.form.get('city')
      hobby = request.form.get('hobby')
      cursor.execute(
         "INSERT INTO users(user_name, email, city, hobby) Values(%s, %s, %s, %s)",
         (user_name, email, city, hobby)
      )
      conn.commit()
      return redirect(url_for('get_users'))
   return render_template('add_user.html')

@app.route('/upload_file', methods = ['POST', 'GET'])
def upload_file():
   if request.method == 'POST':
      user_file = request.files['user_file']
      if user_file:
         file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(user_file.filename))
         user_file.save(file_path)
         return render_template('success.html', operation = 'File Uploading', method = 'upload_file')
      return 'File Uploading Failed!'
   else:
      return render_template('upload_file.html')

@app.route('/user_profile/<int:id>', methods = ['GET'])
def user_profile(id):
   cursor.execute("select * from users where id = %s", (id,))
   user = cursor.fetchone()
   return render_template("user_profile.html", user = user)

@app.route('/delete_user/<int:id>', methods = ['POST'])
def delete_user(id):
   cursor.execute("DELETE FROM users WHERE id = %s", (id,))
   conn.commit()
   return render_template('success.html', operation = "User Deleted", method = 'get_users')

@app.route('/update_user/<int:id>', methods = ['POST', 'GET'])
def update_user(id):
      if request.method == 'POST':
         user_name = request.form.get('user_name')
         email = request.form.get('email')
         city = request.form.get('city')
         hobby = request.form.get('hobby')
         cursor.execute("""
         UPDATE users 
         SET user_name = %s, email = %s, city = %s, hobby = %s
         WHERE id = %s
         """, (user_name, email, city, hobby, id)
         )
         conn.commit()
         return render_template('success.html', operation = 'User Updated', method = 'user_profile', id = id)
      
      cursor.execute("""
         SELECT *
         FROM users
         WHERE id = %s
         """, (id,))
      user = cursor.fetchone()
      return render_template("update_user.html", user = user)

@app.route('/users')
def get_users():
   cursor.execute("select count(id) from users")
   count= cursor.fetchone()[0]
   
   cursor.execute("select * from users")
   rows = cursor.fetchall()
   return render_template('users.html', users = rows, count = count)

if __name__ == '__main__': 
 app.run(port=8000, debug=True)