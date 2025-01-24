from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary storage for registered users
registered_users = []

@app.route('/')
def index():    
    return render_template('do.html')

@app.route('/register', methods=['POST'])
def register():    
    if request.method == 'POST':        
        # Get user input from the form        
        username = request.form['username']        
        email = request.form['email']        

        # Validate the input (you can add more validation as needed)        
        if not username or not email:
            return "Please fill out all fields."        

        # Add the user to the list of registered users        
        registered_users.append({'username': username, 'email': email})        
        return f"Registration successful for {username} with email {email}!"

if __name__ == '__main__':    
    app.run(debug=True)
