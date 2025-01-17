from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'tested_devices'

mysql = MySQL(app)

@app.route('/')
def index():
    # Create a cursor to interact with the database
    cur = mysql.connection.cursor()
    
    # Execute a query
    cur.execute("SELECT * FROM tested_devices")
    
    # Fetch all rows
    devices = cur.fetchall()
    
    # Close the cursor
    cur.close()
    
    return render_template('index.html', devices=devices)

if __name__ == '__main__':
    app.run(debug=True)
