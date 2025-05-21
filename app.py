from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    c.execute("INSERT INTO users (username, password) VALUES ('feby', 'feby123')")
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        # SAFE QUERY
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        c.execute(query, (username, password))
        c.execute(query)
        result = c.fetchone()
        conn.close()
        
        if result:
            return f"Welcome, {username}!"
        else:
            error = "Login failed"
    return render_template('login.html', error=error)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)