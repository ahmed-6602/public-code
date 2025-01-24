from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Ahmed@6602@localhost/studentsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable SQLAlchemy event system

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        
        if not username or not email:
            return "Please fill out all fields."
        
        # Store user data in MySQL database
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        
        return f"Registration successful for {username} with email {email}!"

if __name__ == '__main__':
    app.run(debug=True)
