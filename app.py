from flask import Flask, request, render_template_string, redirect, url_for, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_super_secret_key_here'


def init_db():
    conn = sqlite3.connect('secure_app.db')
    c = conn.cursor()
    # SQL Injection prevention: Using proper table creation
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

init_db()

# JWT Token Verification Decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return "Alert: Token is missing! Please login.", 403
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return "Alert: Token is invalid or expired!", 403
        return f(*args, **kwargs)
    return decorated


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Secure Web App</title></head>
<body style="font-family: Arial; padding: 50px; text-align: center;">
    <h2>Secure Web Application (OWASP Guidelines)</h2>
    <hr>
    <h3>Register</h3>
    <form action="/register" method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Register</button>
    </form>
    <br>
    <h3>Login</h3>
    <form action="/login" method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
    <br><br>
    <p style="color: green;">{{ message }}</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, message="Welcome! Please Register or Login.")

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    # Secure Password Hashing (Never store plain text passwords)
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    
    conn = sqlite3.connect('secure_app.db')
    c = conn.cursor()
    try:
        # Parameterized Query (Prevents SQL Injection)
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        msg = "Registration Successful! You can now login."
    except sqlite3.IntegrityError:
        msg = "Username already exists!"
    finally:
        conn.close()
        
    return render_template_string(HTML_TEMPLATE, message=msg)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('secure_app.db')
    c = conn.cursor()
    # Parameterized Query
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    
    if user and check_password_hash(user[0], password):
        # Generate JWT Token (Authorization)
        token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm="HS256")
        
        resp = make_response(redirect(url_for('dashboard')))
        resp.set_cookie('token', token)
        return resp
    else:
        return render_template_string(HTML_TEMPLATE, message="Invalid Credentials!")

@app.route('/dashboard')
@token_required
def dashboard():
    return "<h2 style='color:green; text-align:center; margin-top:50px;'>Welcome to the Secure Dashboard!</h2><p style='text-align:center;'>You have successfully bypassed authorization using a secure JWT token.</p><center><a href='/logout'>Logout</a></center>"

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('home')))
    resp.set_cookie('token', '', expires=0) # Delete token
    return resp

if __name__ == '__main__':
    app.run(debug=True)